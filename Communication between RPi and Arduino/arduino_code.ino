#include <SoftwareSerial.h>

char Serialdata=0;
void setup() {
// put your setup code here, to run once:
pinMode(13,OUTPUT);
pinMode(11,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
{
  Serialdata=Serial.read();
  Serial.println(Serialdata);

  if(Serialdata < '0')
  {
    digitalWrite(13,HIGH);
    //digitalWrite(11,LOW);
  }
  else if(Serialdata > '0')
  {
    digitalWrite(13,LOW);
    //digitalWrite(11,HIGH);
  }
}
}
