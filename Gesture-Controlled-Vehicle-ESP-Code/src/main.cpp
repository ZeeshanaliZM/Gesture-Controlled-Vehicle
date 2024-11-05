#include <Arduino.h>
#include "Server_Connect.h"

//Define the EEPROM address to read the Wifi Credentials from
#define EEPROM_ADDRESS int(0)

// //Store the wifi credentials in EEPROM if not stored. Delete these after they are stored in the EEPROM
// char ssid[30] = "Enter Wifi SSID";
// char password[10] = "Enter Password";

void setup() {
  Serial.begin(9600);
  // // Store Wifi Details in EEPROM (Run only once to Store the address). Uncomment to store credentials in EEPROM
  // storeWifiDetails(ssid,password,EEPROM_ADDRESS);

  // //Connect the the Wifi
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