// Constants

int rightPin = 12;
int leftPin = 11;
int forwardPin = 10;
int backwardPin = 9;

void setup() {
  Serial.begin(9600); // initialize serial communications at 9600 bps

  pinMode(rightPin, OUTPUT);
  pinMode(leftPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);

  digitalWrite(rightPin, HIGH);
  digitalWrite(leftPin, HIGH);
  digitalWrite(forwardPin, HIGH);
  digitalWrite(backwardPin, HIGH);
  
}

void loop() {
  /*  check if data has been sent from the computer: */
  if (Serial.available()) {
    /* read the most recent byte */
    char readInt = Serial.read();
    /*ECHO the value that was read, back to the serial port. */
    Serial.print(readInt);

    // Left
    if (readInt == '1') {
      digitalWrite(leftPin, HIGH);
    } else if (readInt == '2') {
      digitalWrite(leftPin, LOW);
    }
    // Right
    else if (readInt == '3') {
      digitalWrite(rightPin, HIGH);
    } else if (readInt == '4') {
      digitalWrite(rightPin, LOW);
    }
    // Forward
    else if (readInt == '5') {
      digitalWrite(forwardPin, HIGH);
    } else if (readInt == '6') {
      digitalWrite(forwardPin, LOW);
    }
    // Backward
    else if (readInt == '7') {
      digitalWrite(backwardPin, HIGH);
    } else if (readInt == '8') {
      digitalWrite(backwardPin, LOW);
    }
  }
}
