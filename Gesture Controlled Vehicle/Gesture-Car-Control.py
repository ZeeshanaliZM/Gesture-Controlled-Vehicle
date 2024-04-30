import cv2
import numpy as np
from requests import get, exceptions
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks

ESP8266_URL = "http://{}:80/"
frame_shape = {}

def getframeShape(frame):
    if not frame_shape:
        frame_shape["width"] = frame.shape[1]
        frame_shape["height"] = frame.shape[0]

def main():
    camera = cv2.VideoCapture(0)
    hands = Hands(model_complexity=0)
    
    while camera.isOpened():
        frame = cv2.flip(camera.read()[1],1)
        getframeShape(frame)
        handDetection(frame,hands)

        cv2.imshow("Hands Detected",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()

    cv2.destroyAllWindows()

def connecttoVehicle():
    global ESP8266_URL
    while True:
        try:
            response = get("http://esp8266.local:80/")
        except exceptions.ConnectionError:
            print("Connection Error. Reconnecting...")
            continue
        break
    ESP8266_URL = ESP8266_URL.format(response.text)

def detectLeftHand(result,frame):
    for idx,hand in enumerate(result.multi_handedness):
        if hand.classification[0].label == "Left":
            draw_landmarks(frame,result.multi_hand_landmarks[idx],HAND_CONNECTIONS)
            motionControl(result.multi_hand_landmarks[idx])
        else:
            controlSpeed(result,idx)

def controlSpeed(result,idx):
    diff_thumb_index = (diffCoordinates(result.multi_hand_landmarks[idx],[4,5,1],[8,9,1])-19)/22
    diff_thumb_index_norm = abs(round(int((diff_thumb_index*255)/10)))
    if diff_thumb_index_norm<30:
        # print("Set Speed as 0")
        get(ESP8266_URL+"speedControl",params={"speed":0})
    else:
        # print("Set speed as {}".format(diff_thumb_index_norm))
        get(ESP8266_URL+"speedControl",params={"speed":diff_thumb_index_norm})

def getCoordinatesofPoints(hand_landmarks,start,stop,step):
    return {"x": np.multiply(np.array([points.x for points in hand_landmarks.landmark[start:stop:step]]),frame_shape["width"]),
            "y": np.multiply(np.array([points.y for points in hand_landmarks.landmark[start:stop:step]]),frame_shape["height"]) }

def diffCoordinates(landmarks,range1,range2):
    return getCoordinatesofPoints(landmarks,range1[0],
                                  range1[1],range1[2])['y']-getCoordinatesofPoints(landmarks,range2[0],
                                                                                   range2[1],range2[2])['y']

def motionControl(left_hand_landmarks):
    global ESP8266_URL
    tip_dip_diff_coord_y = diffCoordinates(left_hand_landmarks,[8,24,4],[7,23,4])
    tip_mcp_diff_coord_y = diffCoordinates(left_hand_landmarks,[8,24,4],[5,21,4])

    if np.all(tip_dip_diff_coord_y>0):
        # print("Move Forward")
        get(ESP8266_URL+"moveForward")
    if np.all(tip_mcp_diff_coord_y<0):
        # print("Move Backward")
        get(ESP8266_URL+"moveBackward")
        

def handDetection(frame,hands):
    frame_BGR = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    result = hands.process(frame_BGR)
    if result.multi_handedness:
        detectLeftHand(result,frame)

if __name__ == "__main__":
    connecttoVehicle()
    main()
