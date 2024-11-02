#include <EEPROM.h>
#include "WIFI_EEPROM.h"

//Function to store the Wifi Details in the EEPROM
void storeWifiDetails(char ssid[50],char password[10],int address){
    WifiDetails Wifi;
    Wifi.SSID = ssid;
    Wifi.password = password;
    EEPROM.put(address,Wifi);
}

//Function to get the wifi details from the EEPROM
WifiDetails* getWifiDetails(int address){
    WifiDetails Wifi;
    EEPROM.get(address,Wifi);
    return &Wifi;
}
