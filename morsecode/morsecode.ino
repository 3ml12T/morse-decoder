const int morsePin = 4; 
const int stopPin = 2;

long startTime; // store starting time here 

long endTime = -9999;

long duration; // variable to store how long the timer has been running 

float secduration; // variable to store the duration in seconds 

long duration2;
float secduration2;

int switchState = 0;
int stopped = 0;
int lastState = 0;
 

void setup() 

{ 

pinMode(morsePin,INPUT); 
pinMode(stopPin,INPUT);
pinMode(7,OUTPUT);

attachInterrupt(digitalPinToInterrupt(2),send,RISING);

Serial.begin(9600); 

} 

 

void loop() 

{ 
  switchState = digitalRead(morsePin);
  if (switchState != lastState){
    if (switchState == HIGH){ //switch went from off to on
      startTime = millis();
      digitalWrite(7,HIGH);
      //Is it a new letter?
      if(endTime > 0){
        duration2 = startTime - endTime;
        secduration2 = (float)duration2/1000; 
        if(secduration2 > 0.3){
          Serial.print(" ");
        }
      }
    }
    else { //switch went from on to off
      digitalWrite(7,LOW);
      endTime = millis();
      duration = endTime - startTime;
      secduration = (float)duration/1000; 
      if (secduration <= 0.3){
        Serial.print("."); 
      }
      else{
        Serial.print("-");
      }
    }
  }
  
  if(stopped){
    Serial.println("M");
  }
  lastState = switchState;
  stopped = 0;
} 

void send() {
  stopped = 1;
}
