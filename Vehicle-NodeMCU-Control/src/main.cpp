#include "Server_Connect.h"

void setup(){
    Serial.begin(115200);
    connecttoWifi();
    setupmDNS();
    routeHandler(); 
}

void loop(){
    MDNS.update();
    server.handleClient();
}