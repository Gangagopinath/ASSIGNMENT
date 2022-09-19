#include <Arduino.h>
int A=0,B=0,C=0,X=0;   //input
int P,Q,R,Y;          //output

void fsm_read()
{
  A = digitalRead(8);
  B= digitalRead(9);
  C = digitalRead(10);
 X= digitalRead(11);
}

void fsm_update()
{  
 
 P=(!B && !X)||(C && !X);
 Q=(B && !C)||(C && X);
 R=(!B && !X)||(!C && !X)||(!B && !C);
 Y=(B && C && !X);


//  P=(!B&&!X)||(C&&!X);
//  Q=(!B&&C&&X)||(A&&X)||(B&&!C&&!X);
//  R=(B&&!C)||(B&&X)||(!A&&!C&&X);
//  Y=(B&&C&&!X);

  digitalWrite(2, P);
  digitalWrite(3, Q);
  digitalWrite(4, R);
  digitalWrite(5, Y);
  
  digitalWrite(13, HIGH);
  delay(2000);
  digitalWrite(13, LOW);
  delay(2000);
  
}
void setup() {
    pinMode(2, OUTPUT);  //OUTPUT for F1
    pinMode(3, OUTPUT);  //OUTPUT for F1
    pinMode(4, OUTPUT);  //OUTPUT for F1 
    pinMode(5, OUTPUT);  // to led
    
    pinMode(13, OUTPUT); //clock
    
    pinMode(8, INPUT);  //Input for 1th FF 
    pinMode(9, INPUT);  //INPUT for 2nd FF
    pinMode(10, INPUT);  //INPUT for 3rd FF
    pinMode(11, INPUT);  //INPUT +5V OR GRD
    
}


void loop()
 {
fsm_read();
fsm_update();
  
  }
