# Gesture Control

## Introduction
- This folder contains the logic for the python program that performs gesture recognition.
- The program detects the Hand, processes the landmarks to recognize the gesture according to a predefined logic, and send an HTTP request to the ESP URL to issue a command to it.

## Steps
- The processing of the landmarks involves the following steps:
    1. [**Initialize Connection to µC:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L13)
        - A connection to the µC needs to be established to issue comands to it. For this same purpose a Connection class is developed which contains several data members for establishing and maintaining a connection to the µC. 
    2. [**Get the IP Address of the Microcontroller to connect to it:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L27) 
        - This is done using mDNS feature of ESP8266 which only works when the devices are on the same network. IP address is received unencrypted in request body. The programs continuously sends HTTP requests to the mDNS address until a successfull OK and the IP address of the µC is received. This IP address is used to construct the URL of the µC to send HTTP Requests to it. This works faster than mDNS.
    3.  [**Initialize Hand Detection Mechanism:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L65)
        - Once the connection to the µC has been established, the hand detection mechanism needs to be initialized. This class contains various data memeber for hand detection and gesture recognition. 
    4. [**Initialize Camera:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L41)
        - The Camera class is initialized next which starts recording the frames from the camera and determining the gestures made by the driver.
    5. [**Processing the frames:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L49)
        - The frames are processed by the camera in the ProcessFrame() method present in the Camera Class.
    6. [**Detecting the Hands:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L56)
        - The ProcessFrame() function contains the HandDetection Function of the HandDetection class which is used to detect the hands and recognise the gestures made.
    7. [**Vehicle Control:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L104)
        - The detectHands() method set the frame shape if it has not been set and performs vehicle control which involves linear motion control, direction control and speed control based on a certain predefined logic only if hands have been detected. Each of the control mechanisms are implemented as separate threads using multithreading to improve the speed of the program and reduce latency.
    8. [**Linear Motion Control:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L133)
        - Linear motion control involves controlling forward and backward motion of the vehicle. This is done using some predefined logic and the gesture recognized is used to control the movement of the vehicle by sending an HTTP GET request to a specific URL created for the same purpose. Linear Motion Control is performed by the left hand of the driver.
    9. [**Direction Motion Control:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L145)
        - Direction motion control involves rotation of the wheels of the vehicle to move the car around. THe vehicle should be able to make turns at any angles. The angle of rotation of the wheels is calculated using the gesture made by the driver and the value is sent to the µC at the predefined URL to control the servo attached to the front wheels of the vehicle.
    10. [**Speed Control:**](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-Application-Code/Gesture-Recognition.py#L156)
        - This is performed by the right hand of the driver. A marker is present on the frames displayed to the driver. The driver moves the marker vertically to change the speed of the vehicle.
