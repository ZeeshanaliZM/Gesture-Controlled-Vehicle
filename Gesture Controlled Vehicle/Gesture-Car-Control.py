import cv2
import numpy as np
import requests

ESP8266_URL = "http://esp8266.local:80/"

def main():
    camera = cv2.VideoCapture(0)
    while True:
        frame = cv2.flip(camera.read()[1],1)
        cv2.imshow("Live Stream",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

def connecttoVehicle():
    while True:
        try:
            response = requests.get(ESP8266_URL)
        except requests.exceptions.ConnectionError:
            print("Connection Error. Reconnecting...")
            continue
        break
    print(response.text)

if __name__ == "__main__":
    connecttoVehicle()
    main()