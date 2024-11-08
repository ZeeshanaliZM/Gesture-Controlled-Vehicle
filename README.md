# Gesture Controlled Vehicle

## Introduction
- This Repository contains the source code for the Gesture-Controlled-Vehicle project involving controlling an RC car by gestures using a purely computer based vision.
- The Program for Gesture Recognition is developed in Python and the prototype vehicle is an RC car controlled by ESP8266 microcontroller.

## Details

### Gesture Recognition and Control
- The Program makes use of the [Hand Landmark model](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) present in the [Mediapipe Library developed by Google](https://ai.google.dev/edge/mediapipe/solutions/guide) to detect landmarks of the hand in the camera frame.
- Various kinds of logic is applied for ***Linear Motion, Rotational Motion control and speed control***.
- [***Mutltithreading in Python***](https://docs.python.org/3/library/threading.html) has been implemented in the program to reduce the processing time of the program. This also reduces the number of frames dropped during processing. Multithreading is faster than the traditional sequential implementation. However the Global Interpreter Lock in python prevents parallel processing of threads causing them to be implemented concurrently.
- Although the speed of processing is increased, it can be improved even further using the [***Multi Processing Module***](https://docs.python.org/3/library/multiprocessing.html) in python which allows parallel processing.
- Once the gesture is recognized, HTTP requests are sent to the web server setup on the microcontroller at specific endpoints causing it to control the vehicle.

### RC Car and Microcontroller used
- The chassis of a readymade RC car is used which consists of a pair of DC motors each controlling a pair of wheels. L293D motor driver is used to drive the DC motors to control the wheels of the vehicle.
- [ESP8266](https://github.com/esp8266/Arduino) microcontroller ([documentation](https://arduino-esp8266.readthedocs.io/en/latest/)) is used to control the vehicle. It has a built in Wifi module which is connected to the local network. The Wifi Credentials are stored in the EEPROM of the microcontroller.
- A webserver is setup on the microcontroller to listen to requests from the program at specific endpoints.

### Vehicle Control
See [Gesture-Control README](./Gesture-Controlled-Vehicle-Application-Code/Gesture-Control.md)

### Web Server setup
See [Web-Server README](./Gesture-Controlled-Vehicle-ESP-Code/Web-Server.md)

### Steps to Run the Program
#### Setup Environment for Program
- Contains the source code for Gesture Recognition and Control in Python.
- Setup a Virtual environment using the command **virtualenv "Name of the Environment"**
- Install the depenedencies using the command **pip install -r requirements.txt**

#### Connecting the Hardware
- Connect the DC motor input wires to the L293D motor driver output pins.
- Connect the l293D input pins to the microcontroller PWM pins to allow the speed control and rotational motion control.

#### Store the Wifi Credentials on ESP8266
- Use the function provided in WIFI_EEPROM.h file store the wifi crendentials in the EEPROM.
- The credentials can be stored in the variables ssid and password in main.cpp.
- Remove the credentials from the program once uploaded to the EEPROM.