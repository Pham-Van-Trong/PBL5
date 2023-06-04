#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
Servo myservo;

ESP8266WebServer server(80);

int gas = A0;
int val = 0;
int ledPN = D0;
int ledPK = D1;
int loa = D2;

void ledpnon()
{
    digitalWrite(ledPN, HIGH);
    server.send(200, "text/plain", "Success");
}
void ledpnoff()
{
    digitalWrite(ledPN, LOW);
    server.send(200, "text/plain", "Success");
}
void ledpkon()
{
    digitalWrite(ledPK, HIGH);
    server.send(200, "text/plain", "Success");
}
void ledpkoff()
{
    digitalWrite(ledPK, LOW);
    server.send(200, "text/plain", "Success");
}
void dooron()
{
    myservo.write(180);
    server.send(200, "text/plain", "Success");
}

void dooroff()
{
    myservo.write(0);
    server.send(200, "text/plain", "Success");
}

void setup()
{
    Serial.begin(9600);
    pinMode(ledPN, OUTPUT);
    pinMode(ledPK, OUTPUT);
    pinMode(loa, OUTPUT);
    myservo.attach(D3);
    WiFi.begin("Wifi Chua", "38383838@");
    while (WiFi.waitForConnectResult() != WL_CONNECTED)
    {
        Serial.print(".");
    }
    Serial.println("IP: ");
    Serial.print(WiFi.localIP());

    server.on("/ledpn/on", ledpnon);
    server.on("/ledpn/off", ledpnoff);
    server.on("/ledpk/on", ledpkon);
    server.on("/ledpk/off", ledpkoff);
    server.on("/door/on", dooron);
    server.on("/door/off", dooroff);
    server.begin();
}

void loop()
{
    server.handleClient();
    val = analogRead(gas);
    Serial.println(val, DEC);
    if (val > 500)
        digitalWrite(loa, HIGH);
    else
        digitalWrite(loa, LOW);
}
