#include "Header_definitions.h"
#include "Control_Car.h"

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

void rootHandle(){
    server.send(200,"text/plain","Connection with Vehicle Estasblished.\nGesture Controlled Vehcile online.");
}

void forwardHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Forward");
    moveForward();
}

void backwardHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Backward");
    moveBackward();
}

void URLHandler(){
    server.on("/",rootHandle);
    server.on("/moveForward",forwardHandler);
    server.on("/moveBackward",backwardHandler);
}