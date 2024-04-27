#include "Server_Connect.h"

void setup(){
    Serial.begin(115200);
    connecttoWifi();
    setupmDNS();
}

void loop(){
    MDNS.update();
}