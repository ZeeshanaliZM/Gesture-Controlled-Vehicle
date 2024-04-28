#ifndef HEADER_DEFINITIONS_H
#define HEADER_DEFINITIONS_H
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid PROGMEM = "LAPTOP-K75VLUOD 3846";
const char* password PROGMEM = "#Su81479";

#define DRIVER_IN4_BACK D0
#define DRIVER_IN3_BACK D1
#define DRIVER_EN2_BACK_SPEED D2

#define DRIVER_IN2_FRONT D5
#define DRIVER_IN1_FRONT D6
#define DRIVER_EN1_FRONT_DIRECTION D7

ESP8266WebServer server(80);
#endif