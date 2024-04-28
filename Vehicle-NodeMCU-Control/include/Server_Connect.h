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

void setupmDNS(){
    if (!MDNS.begin("esp8266")) {
        Serial.println(F("Error setting up MDNS responder!"));
        while (1) {delay(1000);}
    }
    Serial.println(F("mDNS responder started"));
    server.begin();
    MDNS.addService("http", "tcp", 80);
}

void rootHandle(){
    server.send(200,"text/plain","Connection with Vehicle Estasblished.\nGesture Controlled Vehcile online.");
}

void URLHandler(){
    server.on("/",rootHandle);
}