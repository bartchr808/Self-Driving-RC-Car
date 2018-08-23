// Constants
int rightPin = 12;
int leftPin = 11;
int forwardPin = 10;
int backwardPin = 9;

enum CommandTypes {
  STOP            = 0,
  FORWARD         = 1,
  BACKWARD        = 2,
  LEFT            = 3,
  RIGHT           = 4,
  FORWARD_LEFT    = 13,
  FORWARD_RIGHT   = 14,
  BACKWARD_LEFT   = 23,
  BACKWARD_RIGHT  = 24
};

int receivedInput = false;
CommandTypes currentCommand = STOP;
int commandTime = 75;
int order = 55;

// Helper functions for setting pin values for RC controller
void forward(int time){
  digitalWrite(forwardPin, LOW);
  delay(time);
  off();
}

void reverse(int time) {
  digitalWrite(backwardPin, LOW);
  delay(time);
  off();
}

void left(int time) {
  digitalWrite(leftPin, LOW);
  delay(time);
  off();
}

void right(int time) {
  digitalWrite(rightPin, LOW);
  delay(time);
  off();
}

void leftForward(int time) {
  digitalWrite(leftPin, LOW);
  digitalWrite(forwardPin, LOW);
  delay(time);
  off();
}

void rightForward(int time) {
  digitalWrite(rightPin, LOW);
  digitalWrite(forwardPin, LOW);
  delay(time);
  off();
}

void leftReverse(int time) {
  digitalWrite(leftPin, LOW);
  digitalWrite(backwardPin, LOW);
  delay(time);
  off();
}

void rightReverse(int time) {
  digitalWrite(rightPin, LOW);
  digitalWrite(backwardPin, LOW);
  delay(time);
  off();
}

// Set all pins to off state
void off(){
  digitalWrite(backwardPin, HIGH);
  digitalWrite(forwardPin, HIGH);
  digitalWrite(leftPin, HIGH);
  digitalWrite(rightPin, HIGH);
}

// Determine what action to the RC controller corresponds to the sent action
//   and perform that action on the corresponding pin(s)
void CommandSelection(CommandTypes currentCommand, int time){
  switch (currentCommand){
    
    // Off
    case STOP: 
      off(); 
      break;
    
    // 1D Commands
    case FORWARD: 
     forward(time); 
     currentCommand = STOP; 
     break;
    
    case BACKWARD: 
      reverse(time); 
      currentCommand = STOP; 
      break;
      
    case LEFT: 
      left(time); 
      currentCommand = STOP; 
      break;
    
    case RIGHT: 
      right(time); 
      currentCommand = STOP; 
      break;
    
    // 2D Commands
    case FORWARD_LEFT: 
      leftForward(time); 
      currentCommand=STOP; 
      break;
    case FORWARD_RIGHT: 
      rightForward(time); 
      currentCommand = STOP; 
      break;
    
    case BACKWARD_LEFT: 
      leftReverse(time); 
      currentCommand = STOP; 
      break;
    
    case BACKWARD_RIGHT: 
      rightReverse(time); 
      currentCommand = STOP; 
      break;
    }
}

void setup() {       
  // Initialize digital pins as outputs
  pinMode(rightPin, OUTPUT);     
  pinMode(leftPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);

  // Initialize serial communications at 9600 bps
  Serial.begin(9600);
}

void loop() {
  off();

  // Get input
  if (Serial.available() > 0) {
    currentCommand = (CommandTypes)(Serial.read());
    receivedInput = true;
  }
  
  if (receivedInput) {
    CommandSelection(currentCommand, commandTime);
  }
}
