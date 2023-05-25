#include<Servo.h>
Servo myservo;
int gas = 0;
int val = 0;
int ledPN = 12;
int ledPK = 13;
int loa = 10;
void setup() {
  Serial.begin(9600);
  pinMode(ledPN,OUTPUT);
  pinMode(ledPK,OUTPUT);
  pinMode(loa,OUTPUT);
  myservo.attach(11);
}

void loop() {
  if (Serial.available() > 0) {
    int state = Serial.read() - '0';
    switch(state) {
      case 0: digitalWrite(ledPN,LOW);
              break;
      case 1: digitalWrite(ledPN, HIGH);
              break;
      case 2: digitalWrite(ledPK, LOW);
              break;
      case 3: digitalWrite(ledPK, HIGH);
              break;
      case 4: myservo.write(90);
              break;
      case 5: myservo.write(0);
              break;
    }
  }
  val = analogRead(gas);
  Serial.println(val, DEC);
  if(val > 200) digitalWrite(loa,HIGH);
  else digitalWrite(loa,LOW);
}