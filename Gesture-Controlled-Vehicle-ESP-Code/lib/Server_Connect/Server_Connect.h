#ifndef SERVER_CONNECT_H
#define SERVER_CONNECT_H

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include "Control_Car.h"
#include "WIFI_EEPROM.h"

//Define Macro for the Handlers
#define ROOT "/"
#define FORWARD "/moveForward"
#define BACKWARD "/moveBackward"
#define DIRECTION "/directionControl"
#define SPEED "/speedControl"

//Connect to the Wifi. Retrieve the Wifi Credentials from the EEPROM
void connecttoWifi(int Address);

//Root Handler for webserver
void rootHandle();

//Setup mDNS to the webserver to get the IP address of the vehicle
void setupmDNS();

//Handler to move the car Forward when /moveForward Route is reached
void forwardHandler();

//Handler to move the car backward when /moveBackward Route is reached
void backwardHandler();

//Handler to change the direction of the car when /directionControl Route is reached
void directionControlHandler();

//Handler to change the speed of the car when /speedControl Route is reached
void speedControlHandler();

//Link Endpoints and Handlers together
void URLHandler();

//Object to create and modify webserver on ESP8266
extern ESP8266WebServer server;

#endif