#include "Server_Connect.h"

//Connect to the Wifi. Retrieve the Wifi Credentials from the EEPROM
void connecttoWifi(int Address){
    WifiDetails* Wifi1 = getWifiDetails(Address);
    WiFi.mode(WIFI_STA);
    WiFi.begin(Wifi1->SSID,Wifi1->password);
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

//Root Handler for webserver
void rootHandle(){
    server.send(200,"text/plain",WiFi.localIP().toString());
}

//Setup mDNS to the webserver to get the IP address of the vehicle
void setupmDNS(){
    if (!MDNS.begin("esp8266")) {
    Serial.println("Error setting up MDNS responder!");
    while (1) { delay(1000); }
  }
  Serial.println("mDNS responder started");
}

//Handler to move the car Forward when /moveForward Route is reached
void forwardHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Forward");
    moveForward();
}

//Handler to move the car backward when /moveBackward Route is reached
void backwardHandler(){
    server.send(200,"text/plain","");
    Serial.println("Move Backward");
    moveBackward();
}

//Handler to change the direction of the car when /directionControl Route is reached
void directionControlHandler(){
    int PWM = server.arg("Direction").toInt();
    server.send(200,"text/plain","");
    if PWM>0 
    {
        Serial.println("Move Left");
        moveLeft(PWM);
    }
    else{
        Serial.println("Move Right");
        moveRight(PWM);
    }
}

//Handler to change the speed of the car when /speedControl Route is reached
void speedControlHandler(){
    int speed = server.arg("speed").toInt();
    server.send(200,"text/plain","");
    Serial.println("Change speed");
    setMotorSpeed_Direction(DRIVER_EN2_BACK_SPEED,speed);
}

//Link Endpoints and Handlers together
void URLHandler(){
    server.on(ROOT,rootHandle);
    server.on(FORWARD,forwardHandler);
    server.on(BACKWARD,backwardHandler);
    server.on(DIRECTION,directionControlHandler)
    server.on(SPEED,speedControlHandler);
}
