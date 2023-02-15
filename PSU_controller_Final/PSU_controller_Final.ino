#define ONBOARD_LED  2
bool start = false

String sD1 = "init";
String sD2 = "init";
String sD3 = "init";
String sD4 = "init";
int D1 = 50;
int D2 = 1000;
int D3 = 50;
int D4 = 1000;

String incomingMsg = "init";

void setup() {
  pinMode(ONBOARD_LED,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    sD1 = Serial.readStringUntil(',');
    sD2 = Serial.readStringUntil(',');
    sD3 = Serial.readStringUntil(',');
    sD4 = Serial.readStringUntil('\n');
    if (sD1 == "Start") {
      start = true
      digitalWrite(ONBOARD_LED, HIGH);
    }
    else if (sD1 == "Stop") {
      start = false
      digitalWrite(ONBOARD_LED, LOW);
    }
    else if (sD1 == "Enable") {
      digitalWrite(ONBOARD_LED, HIGH);
    }
    else {
      D1 = sD1.toInt();
      D2 = sD2.toInt();
      D3 = sD3.toInt();
      D4 = sD4.toInt();

      //Serial.println(D1);
      //Serial.println(D2);
      //Serial.println(D3);
      //Serial.println(D4);
    }
  }
  if (start == true) {
    digitalWrite(startPin, OUTPUT);
    
  }
}