//Hannaneh Hojaiji
//
// set pin numbers:
const int buttonPin1 = 2;     // the number of the pushbutton pin
const int buttonPin2 = 3;     // the number of the pushbutton pin
const int buttonPin3 = 4;     // the number of the pushbutton pin
const int buttonPin4 = 5;     // the number of the pushbutton pin
const int buttonPin5 = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState1 = 0;         // variable for reading the pushbutton status
int buttonState2 = 0; 
int buttonState3 = 0; 
int buttonState4 = 0; 
int buttonState5 = 0; 

void setup() {s
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  buttonState4 = digitalRead(buttonPin4);
  buttonState5 = digitalRead(buttonPin5);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState1 == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Serial.write(1);
    buttonState2 = 0;
    buttonState3 = 0;
    buttonState4 = 0;
    buttonState5 = 0;
  } 
  if (buttonState2 == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Serial.write(2);
    buttonState1 = 0;
    buttonState3 = 0;
    buttonState4 = 0;
    buttonState5 = 0;
  }if (buttonState3 == HIGH) {
    Serial.write(3);
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    buttonState1 = 0;
    buttonState2 = 0;
    buttonState4 = 0;
    buttonState5 = 0;
  }if (buttonState4 == HIGH) {
    Serial.write(4);
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    buttonState1 = 0;
    buttonState2 = 0;
    buttonState3 = 0;
    buttonState5 = 0;
  }if (buttonState5 == HIGH) {
    Serial.write(5);
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    buttonState1 = 0;
    buttonState2 = 0;
    buttonState3 = 0;
    buttonState4 = 0;
  }else {
    // turn LED off:
    Serial.write(0);
    digitalWrite(ledPin, LOW);
    buttonState1 = 0;
    buttonState2 = 0;
    buttonState3 = 0;
    buttonState4 = 0;
    buttonState5 = 0;
  }
}


//derived from:  https://create.arduino.cc/projecthub/glowascii/basic-arduino-javascript-workshop-88c8df
