#ifndef CONTROL_CAR_H
#define CONTROL_CAR_H

#ifndef ARDUINO_H
#include "Arduino.h"
#endif

#include "Pin_Definitions.h"
#include <Servo.h>

//Set the motor pin directions to OUTPUT
void setMotorPinDirection();

//Set the initial state of all the pins to LOW
void initPins();

//Calls the setMotorPinDirection and initPins functions.
void configMotorPins();

//Send PWM value to change speed or direction of wheels
void setMotorSpeed(uint8_t pin,int motorSpeed_Direction);

//Move the car forward
void moveForward();

//Move the car backward
void moveBackward();

//Change the direction of the car
void changeDirection(int PWM);

extern Servo FrontWheels;
#endif 