from requests import get, exceptions
from cv2 import VideoCapture, flip, waitKey, destroyAllWindows
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