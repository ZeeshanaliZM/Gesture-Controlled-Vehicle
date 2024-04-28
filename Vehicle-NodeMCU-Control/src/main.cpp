#include "Server_Connect.h"

void setup(){
    Serial.begin(115200);
    connecttoWifi();
    setupmDNS();
    URLHandler(); 
}

void loop(){
    MDNS.update();
    server.handleClient();
}