from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks,_normalized_to_pixel_coordinates
from collections import namedtuple
import numpy as np
import cv2

Point = namedtuple('Point',['x','y'])
FrameShape = namedtuple('Frame Shape',['width','height'])

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

#Class to create the Camera object for Gesture Recognition
class Camera:
    def __init__(self):
        '''
        Data Members:
        frame_shape - Stores the shape of the image (rows,cols)
        camera      - Stores the VideoCapture() object to control the camera, images and videos
        '''
        self.frame_shape = None
        self.camera = initCamera()
    
    #Function initCamera() return the VideoCapture() object instantiated.
    #Tries to detect an external camera first (arg=1), if NOT FOUND, then uses the primary camera (arg=0)
    def initCamera(self):
        try:
            return cv2.VideoCapture(1)
        except:
            return cv2.VideoCapture(0)
    
    #Function getFrameShape() returns the shape of the image frame
    def getFrameShape(self,frame):
        self.frame_shape = FrameShape(frame.shape[0],frame.shape[1])

    #Function processFrame() process the frame to detect Hands 
    def processFrames(self):
        while self.camera.isOpened():
            frame = cv2.flip(camera.read()[1],1)
            if not frame_shape: self.getFrameShape(frame)
            #Perform Hand Detection

            #Perform Hand Detection
            cv2.imshow("Frame Detected",image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.camera.release()
        cv2.destroyAllWindows()

#Class HandDetection to detect and process hands in images and issue commands to μC
class HandDetection:
    def __init__(self,LOW,HIGH):
        '''
        Data Members:
        hands - Stores the Hands() object to use the HandLandmark detection model 
        LOW   - Stores the LOW Point for minimum speed
        HIGH  - Stores the HIGH POint for maximum speed 
        centre - Stores the actual location of the point used for speed control
        '''
        self.hands = Hands(model_complexity=0,
                             min_detection_confidence=0.5,
                                min_tracking_confidence=0.5)

        #Enter LOW and HIGH points for speed Control
        self.LOW = Point(*LOW)
        self.HIGH = Point(*HIGH)
        self.landmarks = None
        self.centre = None
        self.ld_type = [('x',int),('y',int)]

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