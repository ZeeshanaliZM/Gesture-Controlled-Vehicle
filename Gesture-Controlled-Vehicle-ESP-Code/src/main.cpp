#include <Arduino.h>
#include "Server_Connect.h"

//Define the EEPROM address to read the Wifi Credentials from
#define EEPROM_ADDRESS int(0)

//Store the wifi credentials in EEPROM if not stored. Delete these after they are stored in the EEPROM
// const char* ssid PROGMEM = "Enter the wifi Name";
// const char* password PROGMEM = "Enter the Wifi Password";

void setup() {

  // // Store Wifi Details in EEPROM (Run only once to Store the address). Uncomment to store credentials in EEPROM
  // storeWifiDetails(FPSTR(ssid),FPSTR(password),EEPROM_ADDRESS);
  
  Serial.begin(115200);
  
  //Connect the the Wifi
  connecttoWifi(EEPROM_ADDRESS);

  //Setup mDNS on the server
  setupmDNS();
  
  //Start the server
  server.begin();

  //Configure the server to listen on port 80
  MDNS.addService("http", "tcp", 80);

  //Configure the URLs of the server
  URLHandler(); 

  //Configure the pins of the vehicle
  configMotorPins();
}

void loop() {

  //Update mDNS
  MDNS.update();

  //Configure server to listen and handle requests from client
  server.handleClient();
  
}