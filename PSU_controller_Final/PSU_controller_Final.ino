#define ONBOARD_LED 2
bool start = false;
const int startPin = 5;
const int stopPin = 3;
const int enablePin = 4;
String sD1 = "init";
String sD2 = "init";
String sD3 = "init";
String sD4 = "init";
long D1 = 50000;
long D2 = 1000000;
long D3 = 50000;
long D4 = 1000000;

void setup() {
  pinMode(ONBOARD_LED,OUTPUT);
  pinMode(startPin, OUTPUT);
  pinMode(stopPin, OUTPUT);
  pinMode(enablePin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    sD1 = Serial.readStringUntil(',');
    sD2 = Serial.readStringUntil(',');
    sD3 = Serial.readStringUntil(',');
    sD4 = Serial.readStringUntil('\n');
    if (sD1 == "Start") {
      start = true;
    }
    else if (sD1 == "Stop") {
      start = false;
    }
    else if (sD1 == "Enable") {
      digitalWrite(ONBOARD_LED, HIGH);
      digitalWrite(enablePin, HIGH);
    }
    else if (sD1 == "Disable") {
      digitalWrite(ONBOARD_LED, LOW);
      digitalWrite(enablePin, LOW);
    }
    else {
      D1 = sD1.toInt();
      D2 = sD2.toInt();
      D3 = sD3.toInt();
      D4 = sD4.toInt();
    }
  }
  if (start == true) {
    digitalWrite(startPin, HIGH);
    delayMicroseconds(D1);
    digitalWrite(startPin, LOW);
    delayMicroseconds(D2);
    digitalWrite(stopPin, HIGH);
    delayMicroseconds(D3);
    digitalWrite(stopPin, LOW);
    delayMicroseconds(D4);
  }
}