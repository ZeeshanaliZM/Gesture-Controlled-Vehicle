from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks,_normalized_to_pixel_coordinates

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
        '''
        self.hands = Hands(model_complexity=0,
                             min_detection_confidence=0.5,
                                min_tracking_confidence=0.5)
    
    #method detectHands() which checks for the presence of hands in the frame
    def detectHands(self,frame):
        result = self.hands.process(
                    cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

        if result.multi_handedness:
            self.vehicleCtrl(result,frame)
    
    #method vehicleCtr() which processes the frame and issues commands to the vehicle for linear, rotational and speed control
    def vehicleCtrl(self,result,frame):
        for idx,hand in enumerate(result.multi_handedness):
            draw_landmarks(frame,result.multi_hand_landmarks[idx],HAND_CONNECTIONS)
            if hand.classification[0].label == "Left":
                pass
                self.lnrMotionCtrl(result.multi_hand_landmarks[idx])
                self.rotMotionCtrl(result,idx)
            else:
                pass
                self.speedCtrl(result,idx)