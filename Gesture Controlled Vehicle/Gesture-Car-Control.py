import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)
    while True:
        frame = cv2.flip(camera.read()[1],1)
        cv2.imshow("Live Stream",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()