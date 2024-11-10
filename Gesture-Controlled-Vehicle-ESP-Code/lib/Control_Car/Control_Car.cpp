#include "Control_Car.h"
/*Connections for Motor and Driver
Red Wire of Back Motor - M3
Black Wire of Back Motor - M4

Red Wire of Front Motor - M1
Black Wire of Back Motor - M2
*/

Servo FrontWheels;

//Set the motor pin directions to OUTPUT
void setMotorPinDirection(){
    pinMode(DRIVER_IN3_BACK,OUTPUT);
    pinMode(DRIVER_IN4_BACK,OUTPUT);
    pinMode(FRONT_WHEELS,OUTPUT);
    pinMode(DRIVER_EN2_BACK_SPEED,OUTPUT);
}

//Set the initial state of all the pins to LOW
void initPins(){
    digitalWrite(DRIVER_IN3_BACK,LOW);
    digitalWrite(DRIVER_IN4_BACK,LOW);
    digitalWrite(DRIVER_EN2_BACK_SPEED,LOW);
    FrontWheels.attach(FRONT_WHEELS);
}

//Calls the setMotorPinDirection and initPins functions.
void configMotorPins(){
    setMotorPinDirection();
    initPins();
}

//Send PWM value to change speed or direction of wheels
void setMotorSpeed(uint8_t pin,int motorSpeed){
    analogWrite(pin,motorSpeed);
    Serial.println(motorSpeed);
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

//Change the direction of the car
void changeDirection(int PWM){
    FrontWheels.write(PWM);
}