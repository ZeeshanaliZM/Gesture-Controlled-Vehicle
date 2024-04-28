#ifndef HEADER_DEFINITIONS_H
#define HEADER_DEFINITIONS_H
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid PROGMEM = "LAPTOP-K75VLUOD 3846";
const char* password PROGMEM = "#Su81479";

ESP8266WebServer server(80);
#endif