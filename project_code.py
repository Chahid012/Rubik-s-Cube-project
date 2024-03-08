//access the built-in servo library
#include <Servo.h>
#include "khaibao.h"
Servo Serv1a; //create a servo turn object named Serv1a
Servo Serv1b; //create a servo in out named Serv1b
Servo Serv2a; //create a servo object named Serv2a
Servo Serv2b; //create a servo object named Serv2b
Servo Serv3a; //create a servo object named Serv3a
Servo Serv3b; //create a servo object named Serv3b
Servo Serv4a; //create a servo object named Serv4a
Servo Serv4b; //create a servo object named Serv4b
int i;
void ini() {
  // dung
  Serv1a.write(dung1a);
  Serv2a.write(dung2a);
  Serv3a.write(dung3a);
  Serv4a.write(dung4a);
  // xa
  Serv1b.write(xa1b);
  Serv2b.write(xa2b);
  Serv3b.write(xa3b);
  Serv4b.write(xa4b);
  delay(100);
  // attach the servo motors to their pins
  Serv1b.attach(pinServ1b);
  Serv2b.attach(pinServ2b);
  Serv3b.attach(pinServ3b);
  Serv4b.attach(pinServ4b);
  delay(500);
  Serv1a.attach(pinServ1a);
  delay(500);
  Serv2a.attach(pinServ2a);
  delay(500);
  Serv3a.attach(pinServ3a);
  delay(500);
  Serv4a.attach(pinServ4a);
  delay(500);
}

void Move() {
  // xa
  Serv1b.write(xa1b);
  Serv2b.write(xa2b);
  Serv3b.write(xa3b);
  Serv4b.write(xa4b);
  //delay(100);

  // dung
  Serv1a.write(dung1a);
  //delay(100);
  Serv2a.write(dung2a);
  //delay(100);
  Serv3a.write(dung3a);
  //delay(100);
  Serv4a.write(dung4a);
  //delay(100);

  // gan
  Serv1b.write(gan1b);
  Serv2b.write(gan2b);
  Serv3b.write(gan3b);
  Serv4b.write(gan4b);
  //delay(100);
}

void End() {
  // xa
  Serv1b.write(xa1b);
  Serv2b.write(xa2b);
  Serv3b.write(xa3b);
  Serv4b.write(xa4b);
  //delay(1000);
}

void setup() {
  Serial.begin(9600);
  ini();
  Serial.println("Done!");
  Serial.println("Input the rubik cube");
  Serial.println("Type MOVE to start");
}

void F_COUNTERCLOCKWISE_90() {
  Serv1a.write(ngang1a);
    delay(500);
    Serv1b.write(xa1b);
    delay(500);
    Serv1a.write(dung1a);
    delay(500);
    Serv1b.write(gan1b);
    delay(500);
}

void F_CLOCKWISE_90() {
    Serv1b.write(xa1b);
    delay(500);
    Serv1a.write(ngang1a);
    delay(500);
    Serv1b.write(gan1b);
    delay(500);
    Serv1a.write(dung1a);
    delay(500);
}

void F_ROTATE_90() {
    Serv1b.write(xa1b);
    delay(500);
    Serv1a.write(ngang1a);
    delay(500);
    Serv1b.write(gan1b);
    delay(500);
    Serv1a.write(dung1a);
    delay(500);
    Serv1b.write(xa1b);
    delay(500);
    Serv1a.write(ngang1a);
    delay(500);
    Serv1b.write(gan1b);
    delay(500);
    Serv1a.write(dung1a);
    delay(500);
}

void L_COUNTERCLOCKWISE_90(){
    Serv3a.write(ngang3a);
    delay(500);
    Serv3b.write(xa3b);
    delay(500);
    Serv3a.write(dung3a);
    delay(500);
    Serv3b.write(gan3b);
    delay(500);
}

void L_CLOCKWISE_90(){
    Serv3b.write(xa3b);
    delay(500);
    Serv3a.write(ngang3a);
    delay(500);
    Serv3b.write(gan3b);
    delay(500);
    Serv3a.write(dung3a);
    delay(500);
}

void L_ROTATE_180(){
  Serv3b.write(xa3b);
  delay(500);
  Serv3a.write(ngang3a);
  delay(500);
  Serv3b.write(gan3b);
  delay(500);
  Serv3a.write(dung3a);
  delay(500);
  Serv3b.write(xa3b);
  delay(500);
  Serv3a.write(ngang3a);
  delay(500);
  Serv3b.write(gan3b);
  delay(500);
  Serv3a.write(dung3a);
  delay(500);
}

void loop()
{
  if (solved == false) {
    // wait for solve steps
    if (Serial.available() > 0) {
      data = Serial.readStringUntil('\n');
      Serial.print("data: ");
      Serial.println(data);

      if (data == "END") {
        solved = true;
        End();
        Serial.print(" MOVE?");
      } else {
        L = data.length();
        index = 1;
        String S[int(L / 2) + 1];

        /*String analyze*/
        trash = 0;
        /*Data tracking*/
        count = 0;
        while (index > 0) {
          index = data.indexOf(' ');
          //                          Serial.println(index);
          if (index > 0) {
            S[trash] = data.substring(0, index);
          } else {
            S[trash] = data.substring(0, L);
          }
          //                          Serial.println(S[trash]);
          trash = trash + 1;
          count = index + 1;
          data = data.substring(count, L);
        }
        /* OUTPUT: s (sequence of solve steps)*/
        trash = 0;
        while (trash < int(L / 2) + 1) {

          //////////////////////////////// Start coding here ///////////////////////////////////////////
          //MOVE 2 OUTSIDES 
          if (S[trash]=="7A"){
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);
          }
          //FRONT FUNCTION 
          //COUNTERCLOCKWISE 90
          if (S[trash]=="1A"){
            F_COUNTERCLOCKWISE_90();
          }
          //CLOCKWISE 90
          if (S[trash]=="1B"){
            F_CLOCKWISE_90();
          }
          //ROTATE 180 
              if (S[trash]=="1C"){
            F_ROTATE_90();
          }
          //LEFT FUNCTION 
          //COUNTERCLOCKWISE 90 
          if (S[trash]=="3A"){
            L_COUNTERCLOCKWISE_90();
          }
          //CLOCKWISE 90
          if (S[trash]=="3B"){
            L_CLOCKWISE_90();
          }
          //ROTATE 180 
              if (S[trash]=="3C"){
              L_ROTATE_180();
          }
          //BACK FUNCTION
          //COUNTERCLOCKWISE 90
                    if (S[trash]=="2A"){
              Serv2a.write(ngang2a);
              delay(500);
              Serv2b.write(xa2b);
              delay(500);
              Serv2a.write(dung2a);
              delay(500);
              Serv2b.write(gan2b);
              delay(500);
          }
          //CLOCKWISE 90
          if (S[trash]=="2B"){
              Serv2b.write(xa2b);
              delay(500);
              Serv2a.write(ngang2a);
              delay(500);
              Serv2b.write(gan2b);
              delay(500);
              Serv2a.write(dung2a);
              delay(500);
          }
          //ROTATE 180 
              if (S[trash]=="2C"){
              Serv2b.write(xa2b);
              delay(500);
              Serv2a.write(ngang2a);
              delay(500);
              Serv2b.write(gan2b);
              delay(500);
              Serv2a.write(dung2a);
              delay(500);
              Serv2b.write(xa2b);
              delay(500);
              Serv2a.write(ngang2a);
              delay(500);
              Serv2b.write(gan2b);
              delay(500);
              Serv2a.write(dung2a);
              delay(500);
          }

//RIGHT FUNCTION 
//COUNTERCLOCKWISE 90
          if (S[trash]=="4A"){
              Serv4a.write(ngang4a);
              delay(500);
              Serv4b.write(xa4b);
              delay(500);
              Serv4a.write(dung4a);
              delay(500);
              Serv4b.write(gan4b);
              delay(500);
          }
          //CLOCKWISE 90
          if (S[trash]=="4B"){
              Serv4b.write(xa4b);
              delay(500);
              Serv4a.write(ngang4a);
              delay(500);
              Serv4b.write(gan4b);
              delay(500);
              Serv4a.write(dung4a);
              delay(500);
          }
          //ROTATE 180 
              if (S[trash]=="4C"){
              Serv4b.write(xa4b);
              delay(500);
              Serv4a.write(ngang4a);
              delay(500);
              Serv4b.write(gan4b);
              delay(500);
              Serv4a.write(dung4a);
              delay(500);
              Serv4b.write(xa4b);
              delay(500);
              Serv4a.write(ngang4a);
              delay(500);
              Serv4b.write(gan4b);
              delay(500);
              Serv4a.write(dung4a);
              delay(500);
          }
      // //UP FUNCTION
                //COUNTERCLOCKWISE 90 
          if (S[trash]=="5A"){
            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            }
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);

              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);  

          }
          //CLOCKWISE 90
          if (S[trash]=="5B"){
            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            }
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);

              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);  
          }
          //ROTATE 180 
          if (S[trash]=="5C"){
            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            }
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);

              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);  
          }
      //DOWN FUNCTION
      //COUNTERCLOCKWISE 90
              if (S[trash]=="6A"){
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);

            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
                }
            }
      //CLOCKWISE90
                if (S[trash]=="6B"){
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);

            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            }
                }
          //ROTATE 180 
          if (S[trash]=="6C"){
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);
              Serv1b.write(xa1b);
              delay(500);
              Serv1a.write(ngang1a);
              delay(500);
              Serv1b.write(gan1b);
              delay(500);
              Serv1a.write(dung1a);
              delay(500);
            for(i=1;i<=3;i++)
            {
              Serv1b.write(xa1b);
              Serv2b.write(xa2b);
              delay(500);
              Serv3a.write(ngang3a);
              Serv4a.write(ngang4a);
              delay(500);
              Serv1b.write(gan1b);
              Serv2b.write(gan2b);
              delay(500);
              Serv3b.write(xa3b);
              Serv4b.write(xa4b);
              delay(500);
              Serv3a.write(dung3a);
              Serv4a.write(dung4a);
              delay(500);
              Serv3b.write(gan3b);
              Serv4b.write(gan4b);
              delay(500);                          
            }
        }
          //////////////////////////////// Stop coding here ///////////////////////////////////////////
          Serial.print(S[trash]);
          Serial.print(" ");
          trash = trash + 1;

        }
        Serial.println(" ");
        Serial.println("MOVED!");
        data = "";
      }
    }
    
   }else {
    if (Serial.available() > 0) {
      data = Serial.readStringUntil('\n');
      if (data == "MOVE") {
        Move();
        solved = false;
        Serial.println("Input solving steps");
      }
      data = "";
    }
    data = "";
  }
    }
