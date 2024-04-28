import cv2
import numpy as np
from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks

ESP8266_URL = "http://192.168.137.122:80/"

def main():
    camera = cv2.VideoCapture(0)
    hands = Hands(model_complexity=0)
    while camera.isOpened():
        frame = cv2.flip(camera.read()[1],1)
        handDetection(frame,hands)
        cv2.imshow("Hands Detected",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

def connecttoVehicle():
    while True:
        try:
            response = get(ESP8266_URL)
        except exceptions.ConnectionError:
            print("Connection Error. Reconnecting...")
            continue
        break
    print(response.text)

def detectLeftHand(result,frame):
    for idx,hand in enumerate(result.multi_handedness):
        if hand.classification[0].label == "Left":
            draw_landmarks(frame,result.multi_hand_landmarks[idx],HAND_CONNECTIONS)
            motionControl(result.multi_hand_landmarks[idx])
        

def getCoordinatesofPoints(hand_landmarks,start,stop,step):
    return {"x": np.array([points.x for points in hand_landmarks.landmark[start:stop:step]]),
            "y": np.array([points.y for points in hand_landmarks.landmark[start:stop:step]]) }

def motionControl(left_hand_landmarks):
    global ESP8266_URL
    fingers_tip_coord = getCoordinatesofPoints(left_hand_landmarks,8,24,4)
    fingers_dip_coord = getCoordinatesofPoints(left_hand_landmarks,7,23,4)
    diff_coord_y = fingers_tip_coord["y"] - fingers_dip_coord["y"]

    if np.all(diff_coord_y>0):
        get(ESP8266_URL+"moveForward")
    if np.all(diff_coord_y<0):
        get(ESP8266_URL+"moveBackward")
        

def handDetection(frame,hands):
    frame_BGR = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    result = hands.process(frame_BGR)
    if result.multi_handedness:
        detectLeftHand(result,frame)

if __name__ == "__main__":
    connecttoVehicle()
    main()