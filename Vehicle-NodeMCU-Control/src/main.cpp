#include "Server_Connect.h"

void setup(){
    Serial.begin(115200);
    connecttoWifi();
    server.begin();
    URLHandler(); 
}

void loop(){
    server.handleClient();
}