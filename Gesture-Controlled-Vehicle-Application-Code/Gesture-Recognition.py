from requests import get, exceptions
import cv2
from collections import namedtuple

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