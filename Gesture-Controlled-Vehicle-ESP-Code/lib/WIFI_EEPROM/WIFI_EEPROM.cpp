#include "WIFI_EEPROM.h"

//Function to store the Wifi Details in the EEPROM
void storeWifiDetails(char ssid[30],char password[10],int address){
    WifiDetails Wifi;
    strcpy(Wifi.SSID,ssid);
    strcpy(Wifi.password,password);
    EEPROM.begin(256);
    EEPROM.put(address,Wifi);
    EEPROM.end();
}

//Function to get the wifi details from the EEPROM
WifiDetails getWifiDetails(int address){
    WifiDetails Wifi;
    EEPROM.begin(256);
    EEPROM.get(address,Wifi);
    EEPROM.end();
    return Wifi;
}
