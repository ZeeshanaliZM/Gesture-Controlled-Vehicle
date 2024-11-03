#include "Control_Car.h"
/*Connections for Motor and Driver
Red Wire of Back Motor - M3
Black Wire of Back Motor - M4

Red Wire of Front Motor - M1
Black Wire of Back Motor - M2
*/

//Set the motor pin directions to OUTPUT
void setMotorPinDirection(){
    pinMode(DRIVER_IN1_FRONT,OUTPUT);
    pinMode(DRIVER_IN2_FRONT,OUTPUT);
    pinMode(DRIVER_IN3_BACK,OUTPUT);
    pinMode(DRIVER_IN4_BACK,OUTPUT);
    pinMode(DRIVER_EN1_FRONT_DIRECTION,OUTPUT);
    pinMode(DRIVER_EN2_BACK_SPEED,OUTPUT);
}

//Set the initial state of all the pins to LOW
void initPins(){
    digitalWrite(DRIVER_IN1_FRONT,LOW);
    digitalWrite(DRIVER_IN2_FRONT,LOW);
    digitalWrite(DRIVER_IN3_BACK,LOW);
    digitalWrite(DRIVER_IN4_BACK,LOW);
    digitalWrite(DRIVER_EN1_FRONT_DIRECTION,LOW);
    digitalWrite(DRIVER_EN2_BACK_SPEED,LOW);
}

//Calls the setMotorPinDirection and initPins functions.
void configMotorPins(){
    setMotorPinDirection();
    initPins();
}

//Send PWM value to change speed or direction of wheels
void setMotorSpeed_Direction(uint8_t pin,int motorSpeed_Direction){
    analogWrite(pin,motorSpeed_Direction);
    Serial.println("Reached");
}

//Move the car forward
void moveForward(){
    digitalWrite(DRIVER_IN4_BACK,HIGH);
    digitalWrite(DRIVER_IN3_BACK,LOW);
}

//Move the car backward
void moveBackward(){
    digitalWrite(DRIVER_IN4_BACK,LOW);
    digitalWrite(DRIVER_IN3_BACK,HIGH);
}

//Move the car Left
void moveLeft(int PWM){
    digitalWrite(DRIVER_IN2_FRONT,HIGH);
    digitalWrite(DRIVER_IN1_FRONT,LOW);
    setMotorSpeed_Direction(DRIVER_EN1_FRONT_DIRECTION,PWM);
}

//Move the car right 
void moveRight(int PWM){
    digitalWrite(DRIVER_IN2_FRONT,LOW);
    digitalWrite(DRIVER_IN1_FRONT,HIGH);
    setMotorSpeed_Direction(DRIVER_EN1_FRONT_DIRECTION,PWM);
}