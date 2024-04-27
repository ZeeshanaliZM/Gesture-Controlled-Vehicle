#include "Header_definitions.h"

void connecttoWifi(){
    WiFi.begin(FPSTR(ssid),FPSTR(password));
    Serial.print("Connecting");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println();
    Serial.print("Connected, IP address: ");
    Serial.println(WiFi.localIP());
    }