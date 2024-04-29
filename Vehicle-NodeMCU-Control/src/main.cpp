#include "Server_Connect.h"

void setup(){
    Serial.begin(115200);
    connecttoWifi();
    setupmDNS();
    server.begin();
    MDNS.addService("http", "tcp", 80);
    URLHandler(); 
}

void loop(){
    server.handleClient();
}