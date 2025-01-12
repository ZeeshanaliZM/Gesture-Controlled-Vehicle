# ESP8266 motion and speed control

## Introduction
- This folder contains the logic implemented to setup a web server on the ESP8266 microcontroller and control the movement of the vehicle based on the command received from the Gesture Recognition Application.

## Details
- Various Steps need to be performed before the vehicle can be controlled by hand gestures.

    1. [**Connection to WIFI:**](./lib/WIFI_EEPROM/WIFI_EEPROM.h)
        - The µC needs to connect to the WIFI. For this purpose the wifi credentials (SSID and password) are needed. These details are stored in the EEPROM of the µC and are retrieved from it whenever the µC is reset. More details about the ESP8266 can be found [here.](https://arduino-esp8266.readthedocs.io/en/latest/)
        - The Details are stored in the EEPROM using the function [***storeWifiDetails().***](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/lib/WIFI_EEPROM/WIFI_EEPROM.h#L17)
        - The details are retrieved from the EEPROM using the function [***getWifiDetials().***](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/lib/WIFI_EEPROM/WIFI_EEPROM.h#L20)
    2. [**Pin Definitions:**](./lib/Pin_Definitions/Pin_Definitions.h)
        - The microncontroller pins are connected to the servo motor to control the front wheels for direction control and the motor driver connected to the rear wheels to control the speed of the car.
    3. [**Server Configuration:**](./lib/Server_Connect/Server_Connect.h)
        - A web server needs to be setup on the µC to communicate with the gesture recognition application running on the computer. The µC first [***connects to the wifi***](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/lib/Server_Connect/Server_Connect.h#L18) and [***sets up the mDNS***](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/lib/Server_Connect/Server_Connect.h#L24) after which various URL handler are defined to perform functions whenver a request is sent to s certain endpoint.
    4. [**Control Logic:**](./lib/Control_Car/Control_Car.h)
        - Finally the control logic is created which will perform control operations based on the command received from the Gesture Recognition Application.
    
## Order of Execution:
- The order of execution can be understood from the [***main.cpp***](./src/main.cpp) file and is given as follows:
    1. [Establish Connection to Wifi](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L17)
    2. [Setup mDNS](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L20)
    3. [Start the Web Server](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L23)
    4. [Configure mDNS to listen on port 80](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L26)
    5. [Define URL handler for various endpoints](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L29)
    6. [Configure motor pins for control](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L32)
    7. [Update mDNS in loop](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L38)
    8. [Configure server to listen to requests from client and handle them](https://github.com/ZeeshanaliZM/Gesture-Controlled-Vehicle/blob/28b1cf65d4753808fe3060bb357af975c18dfb75/Gesture-Controlled-Vehicle-ESP-Code/src/main.cpp#L41)


