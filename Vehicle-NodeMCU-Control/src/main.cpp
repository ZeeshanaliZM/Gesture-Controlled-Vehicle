#include "Server_Connect.h"
void basic(){
    server.send(200, "text/plain", "hello from esp8266!\r\n");
}

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