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


### Vehicle Control
See [Gesture-Control.md](./Gesture-Controlled-Vehicle-Application-Code/Gesture_Control.md)

### Web Server setup






### Gesture-Controlled-Vehicle-Application Code
- Contains the source code for Gesture Recognition and Control in Python.
- Setup a Virtual environment using the command **virtualenv "Name of the Environment"**
- Install the depenedencies using the command **pip install -r requirements.txt**
