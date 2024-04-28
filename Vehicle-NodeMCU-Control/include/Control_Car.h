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