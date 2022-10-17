
//https://stackoverflow.com/a/19720372/11493297

#include <SoftwareSerial.h>

#define rxPin 8
#define txPin 7

SoftwareSerial mySerial(rxPin, txPin); // RX, TX
char Char, inputByte;

void setup() {
  Serial.begin(9600);   
  Serial.println("Goodnight moon!");

  mySerial.begin(9600);
  mySerial.println("Hello, world?");

  digitalWrite(13,LOW);
}

void loop(){
  while(Serial.available()>0){
    Char = Serial.read();
    Serial.print(Char);

    if (inputByte=='1'){
      digitalWrite(13,HIGH);
      }
  
    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      } 
  }

   while(mySerial.available()>0){

    inputByte = mySerial.read();
    mySerial.println(inputByte, ";");

    if (inputByte=='1'){
      digitalWrite(13,HIGH);
      }
  
    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      } 
  }
}
