import cv2
import numpy as np
from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks

ESP8266_URL = "http://esp8266.local:80/"

def main():
    camera = cv2.VideoCapture(0)
    hands = Hands(model_complexity=1)
    left_hand_landmark = None
    while camera.isOpened():
        frame = cv2.flip(camera.read()[1],1)
        left_hand_landmark = handDetection(frame,hands)
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

def detectLeftHand(result):
    if result.multi_handedness:
        for idx,hand in enumerate(result.multi_handedness):
            if hand.classification[0].label == "Left":
                return result.multi_hand_landmarks[idx]


def handDetection(frame,hands):
    frame_BGR = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    result = hands.process(frame_BGR)
    left_hand_landmark = detectLeftHand(result)
    draw_landmarks(frame,left_hand_landmark,HAND_CONNECTIONS)
    return left_hand_landmark

if __name__ == "__main__":
    connecttoVehicle()
    main()