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
    def detectHands(self,frame):
        result = self.hands.process(
                    cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

        if result.multi_handedness:
            self.vehicleCtrl(result,frame)

    #method vehicleCtr() which processes the frame and issues commands to the vehicle for linear, rotational and speed control
    def vehicleCtrl(self,result,frame):
        for idx,hand in enumerate(result.multi_handedness):
            landmarks = result.multi_hand_landmarks[idx]
            draw_landmarks(frame,landmarks,HAND_CONNECTIONS)
            self.landmarks = array([
                                _normalized_to_pixel_coordinates(
                                    points.x,points.y,frame_shape['width'],frame_shape['height'])
                                        for points in landmarks.landmark])

            if hand.classification[0].label == "Left":
                pass
                self.lnrMotionCtrl(connection)
                self.rotMotionCtrl(connection)
            else:
                pass
                self.speedCtrl(result,idx)