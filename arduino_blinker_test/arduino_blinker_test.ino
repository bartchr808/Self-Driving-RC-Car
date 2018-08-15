// Constants
int ledPin = 12;

void setup() {
  Serial.begin(9600); // initialize serial communications at 9600 bps

  pinMode(ledPin, OUTPUT);
}

void loop() {
  /*  check if data has been sent from the computer: */
  if (Serial.available()) {
    /* read the most recent byte */
    char readInt = Serial.read();
    /*ECHO the value that was read, back to the serial port. */
    Serial.print(readInt);

    if (readInt == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (readInt == '2') {
      digitalWrite(ledPin, LOW);
    }
  }
}
