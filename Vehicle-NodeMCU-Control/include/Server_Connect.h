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
    server.send(200,"text/plain",WiFi.localIP().toString());
}

void setupmDNS(){
    if (!MDNS.begin("esp8266")) {
    Serial.println("Error setting up MDNS responder!");
    while (1) { delay(1000); }
  }
  Serial.println("mDNS responder started");
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

void leftHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Left");
    moveLeft();
}

void leftHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Right");
    moveRight();
}

void URLHandler(){
    server.on("/",rootHandle);
    server.on("/moveForward",forwardHandler);
    server.on("/moveBackward",backwardHandler);
}