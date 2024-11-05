#ifndef WIFI_EEPROM_H
#define WIFI_EEPROM_H

#ifndef ARDUINO_H
#include <Arduino.h>
#endif

#include <EEPROM.h>

//Structure to store the Wifi Details
typedef struct WifiDetails{
    char SSID[30];
    char password[10];
}WifiDetails;

//Function storeWifiDetails stores the wifi details in the EEPROM and can be extracted during runtime
void storeWifiDetails(char ssid[],char password[],int address);

//Function getWifiDetails gets the Wifi details from the EEPROM
WifiDetails getWifiDetails(int address);

#endif

