#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>

#define BAUDRATE 115200
#define LED_R1 14
#define LED_G1 12
#define LED_B1 13
#define LED_R2 4
#define LED_G2 0
#define LED_B2 2

const char* ssid = "Laboratorium-IoT";
const char* pass = "IoTL@bolatorium";

AsyncWebServer server(80);

void wifi_connect() {
  WiFi.begin(ssid, pass);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(250);
  }
  Serial.println("\nWiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(BAUDRATE);
  pinMode(LED_R1, OUTPUT);
  pinMode(LED_G1, OUTPUT);
  pinMode(LED_B1, OUTPUT);
  pinMode(LED_R2, OUTPUT);
  pinMode(LED_G2, OUTPUT);
  pinMode(LED_B2, OUTPUT);
  
  wifi_connect();

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->send(200, "text/plain", "LED Controller");
  });

  server.on("/rgb", HTTP_POST, [](AsyncWebServerRequest *request) {
    if (request->hasParam("red1")) {
      int red1 = request->getParam("red1")->value().toInt();
      int green1 = request->getParam("green1")->value().toInt();
      int blue1 = request->getParam("blue1")->value().toInt();
      int red2 = request->getParam("red2")->value().toInt();
      int green2 = request->getParam("green2")->value().toInt();
      int blue2 = request->getParam("blue2")->value().toInt();
      
      analogWrite(LED_R1, red1);
      analogWrite(LED_G1, green1);
      analogWrite(LED_B1, blue1);
      analogWrite(LED_R2, red2);
      analogWrite(LED_G2, green2);
      analogWrite(LED_B2, blue2);

      request->send(200, "text/plain", "RGB values set");
    } else {
      request->send(400, "text/plain", "Missing parameters");
    }
  });

  server.begin();
}
    

void loop() {


}
