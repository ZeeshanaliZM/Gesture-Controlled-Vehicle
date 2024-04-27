#include "Header_definitions.h"

void connecttoWifi(){
    WiFi.mode(WIFI_STA);
    WiFi.begin(FPSTR(ssid),FPSTR(password));
    Serial.print(F("Connecting"));
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(F("."));
    }
    Serial.println();
    Serial.print(F("Connected, IP address: "));
    Serial.println(WiFi.localIP());
    }