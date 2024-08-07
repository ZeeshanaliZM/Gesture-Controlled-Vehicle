#include "Header_definitions.h"

/*Connections for Motor and Driver
Red Wire of Back Motor - M3
Black Wire of Back Motor - M4

Red Wire of Front Motor - M1
Black Wire of Back Motor - M2
*/

void setMotorPinDirection(){
    pinMode(DRIVER_IN1_FRONT,OUTPUT);
    pinMode(DRIVER_IN2_FRONT,OUTPUT);
    pinMode(DRIVER_IN3_BACK,OUTPUT);
    pinMode(DRIVER_IN4_BACK,OUTPUT);
    pinMode(DRIVER_EN1_FRONT_DIRECTION,OUTPUT);
    pinMode(DRIVER_EN2_BACK_SPEED,OUTPUT);
}

void initPins(){
    digitalWrite(DRIVER_IN1_FRONT,LOW);
    digitalWrite(DRIVER_IN2_FRONT,LOW);
    digitalWrite(DRIVER_IN3_BACK,LOW);
    digitalWrite(DRIVER_IN4_BACK,LOW);
    digitalWrite(DRIVER_EN1_FRONT_DIRECTION,LOW);
    digitalWrite(DRIVER_EN2_BACK_SPEED,LOW);
}

void configMotorPins(){
    setMotorPinDirection();
    initPins();
}

void setMotorSpeed_Direction(uint8_t pin,int motorSpeed_Direction){
    analogWrite(pin,motorSpeed_Direction);
}

void moveForward(){
    digitalWrite(DRIVER_IN4_BACK,HIGH);
    digitalWrite(DRIVER_IN3_BACK,LOW);
    setMotorSpeed_Direction(DRIVER_EN2_BACK_SPEED,255);
}

void moveBackward(){
    digitalWrite(DRIVER_IN4_BACK,LOW);
    digitalWrite(DRIVER_IN3_BACK,HIGH);
    setMotorSpeed_Direction(DRIVER_EN2_BACK_SPEED,255);
}

void moveLeft(){
    digitalWrite(DRIVER_IN2_FRONT,HIGH);
    digitalWrite(DRIVER_IN1_FRONT,LOW);
    setMotorSpeed_Direction(DRIVER_EN1_FRONT_DIRECTION,255);
}

void moveRight(){
    digitalWrite(DRIVER_IN2_FRONT,LOW);
    digitalWrite(DRIVER_IN1_FRONT,HIGH);
    setMotorSpeed_Direction(DRIVER_EN1_FRONT_DIRECTION,255);
}