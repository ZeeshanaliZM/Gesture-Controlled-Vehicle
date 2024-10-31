from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks,_normalized_to_pixel_coordinates
from collections import namedtuple
import numpy as np

Point = namedtuple('Point',['x','y'])
FrameShape = namedtuple('Frame_Shape',['width','height'])

#Creation of class Connection to connect to the μC
class Connection:
    def __init__(self,ESP8266_mDNS_URL,port):
        '''
        Data Members:
        mDNS - Stores the mDNS URL of the μC to connect to it.
        IP   - Stores the IP address of the μC obtained after the first GET request to the mDNS.
        URL  - String to create the URL of the μC with its IP address 
        '''
        self.mDNS = ESP8266_mDNS_URL
        self.IP = None
        self.URL = "http://{}:"+f"{port}"
        self.connectToVehicle()

    #Class method connecttoVehicle to send GET request to the μC using its mDNS URL
    def connectToVehicle(self):
        while True:
            try:
                response = get(self.mDNS)
            except exceptions.ConnectionError:
                print("Connection Error. Reconnecting...")
                continue
            break
        self.IP = response.text
        self.URL = self.URL.format(self.IP)
        print("Connection with vehicle Established")
        print("URL of Server on ESP8266 = "+self.URL)

#Class to create the Camera object for Gesture Recognition
class Camera:
    def __init__(self,type,handDetection,connection):
        '''
        Data Members:
        camera - Stores the VideoCapture() object to control the camera, images and videos
        '''
        #Create VideoCapture Class object to interface to camera
        self.camera = cv2.VideoCapture(type)
        self.processFrames(handDetection,connection)

    #Function processFrame() process the frame to detect Hands 
    def processFrames(self,handDetection,connection):
        while self.camera.isOpened():
            frame = cv2.flip(camera.read()[1],1)
            #Perform Hand Detection
            handDetection.detectHands(frame,connection)
            #Perform Hand Detection
            cv2.imshow("Frame Detected",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.camera.release()
        cv2.destroyAllWindows()
#Class HandDetection to detect and process hands in images and issue commands to μC
class HandDetection:
    def __init__(self):
        '''
        Data Members:
        hands - Stores the Hands() object to use the HandLandmark detection model 
        LOW   - Stores the LOW Point for minimum speed
        HIGH  - Stores the HIGH POint for maximum speed 
        centre - Stores the actual location of the point used for speed control
        frame_shape - To store the shape of the frame
        circle - Contains the equation of the circle evaluated for the speed control condition check
        radius - Contains the radius of the circle used for previous data member
        '''
        self.hands = Hands(model_complexity=0,
                             min_detection_confidence=0.5,
                                min_tracking_confidence=0.5)
        self.LOW = self.HIGH = self.landmarks = self.centre = self.frame_shape = None
        self.circle = "({}-{})**2+({}-{})**2 - {}**2"
        self.radius = 25

    #method getFrameShape() returns the shape of the image frame
    def getFrameShape(self,frame):
        self.frame_shape = FrameShape(frame.shape[1],frame.shape[0])

    #method setSpeedLimits() to set the data members for Speed Control and its limits
    def setSpeedLimit(self):
        self.LOW = Point(int(3*self.frame_shape.width/4),int(6*self.frame_shape.height/8))
        self.HIGH = Point(int(3*self.frame_shape.width/4),int(self.frame_shape.height/8))
        self.centre = np.array([*self.LOW])
        # print(f"Low Speed = {self.LOW} and High Speed = {self.HIGH}")

    #method detectHands() which checks for the presence of hands in the frame
    def detectHands(self,frame,connection):
        result = self.hands.process(
                    cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
        if not self.frame_shape: self.getFrameShape()
        if not self.LOW: self.setSpeedLimit()
        if result.multi_handedness: self.vehicleCtrl(result,frame,connection)

    #method vehicleCtr() which processes the frame and issues commands to the vehicle for linear, rotational and speed control
    def vehicleCtrl(self,result,frame,connection):
        for idx,hand in enumerate(result.multi_handedness):
            landmarks = result.multi_hand_landmarks[idx]
            try:
                self.landmarks = np.array([
                                        _normalized_to_pixel_coordinates(
                                            points.x,points.y,frame_shape['width'],frame_shape['height'])
                                                for points in landmarks.landmark])
            except: print("Landmarks Missing")

            if hand.classification[0].label == "Left":
                self.lnrMotionCtrl(connection)
                self.rotMotionCtrl(connection)
                draw_landmarks(frame,landmarks,HAND_CONNECTIONS)
                pass
            else:
                self.speedCtrl(connection)
                cv2.circle(frame,tuple(self.centre.ravel()),self.radius,color=(0,255,0),thickness=-3)
                pass
    
    #method lnrMotionCtrl() contains the logic for linear motion control
    def lnrMotionCtrl(self,connection):
        tip_dip_diff_coord_y = self.landmarks[8:24:4][1] - self.landmarks[7:23:4][1]
        tip_mcp_diff_coord_y = self.landmarks[8:24:4][1] - self.landmarks[5:21:4][1]

        if np.all(tip_dip_diff_coord_y<0):
            #print("Move Backwards")
            get(connection.URL+"/moveForward")
        if np.all(tip_mcp_diff_coord_y>0):
            #print("Move Forward")
            get(connection.URL+"/moveBackward")
    
    #method rotMotionCtrl() contains the logic for direction contol of the vehicle
    def rotMotionCtrl(self,connection):
        try:
            ref_line = np.array([1,0])
            pf_vector = self.landmarks[17]-self.landmarks[0]
            angle = np.rad2deg(np.arcsin(ref_line.dot(pf_vector)/np.linalg.norm(pf_vector)))
            PWM = np.floor(255*angle/90)
            #print(f"Direction Value = {PWM}")
            get(connection.URL+"/DirectionControl",params={"Direction":PWM})
        except: print("Realign Hand")

    #method speedCtrl() to control the speed of the vehicle
    def speedCtrl(self,connection):
        try:
            point = np.round((self.landmarks[8]+self.landmarks[12])/2)
            circle_pos = eval(self.circle.format(
                            point[0],self.centre[0],
                                point[1],self.centre[1],self.radius))
            if circle_pos <=0 and point[1]<=self.LOW.y and point[1]>=self.HIGH.y: self.centre[1] = point[1]
            PWM = round(255*(self.centre[1] - self.LOW.y)/(self.HIGH.y-self.LOW.y))
            # print(f"Signal Sent to ESP8266 = {PWM}")
            get(connection.URL+"/speedControl",params={"speed":PWM})
        except: pass