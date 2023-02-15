char incomingByte = 'B';
bool activeSwitch = false;
const int startPin = 2;
const int stopPin = 3;
String incomingMessage = "init"


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(startPin, OUTPUT);
  pinMode(stopPin, OUTPUT);
}

void pulsedPSU() {
  digitalWrite(startPin, HIGH);
  delay(50);
  digitalWrite(startPin, LOW);
  delay(1000);
  digitalWrite(stopPin, HIGH);
  delay(50);
  digitalWrite(stopPin, LOW);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    incomingByte = Serial.read();

    if (incomingByte == 'A') {
      activeSwitch = true;
    }
    else if (incomingByte == 'B') {
      activeSwitch = false;
    }
    
  }

  switch(activeSwitch) {
      case true:
        pulsedPSU();
        break;
      case false:
        break;
      }
}

