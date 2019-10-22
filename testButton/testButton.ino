const int button1 = 5;     // the number of the pushbutton pin
const int button2 = 4;     // the number of the pushbutton pin
const int button3 = 2;     // the number of the pushbutton pin
const int button4 = 12;     // the number of the pushbutton pin
const int button5 = 13;     // the number of the pushbutton pin

// variables will change:

void setup() {
  // initialize the pushbutton pin as an input:
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
  pinMode(button5, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(button1) == LOW) 
    Serial.print("Button1 is pressed \n");
    
  if (digitalRead(button2) == LOW) 
    Serial.print("Button2 is pressed \n ");

  if (digitalRead(button3) == LOW) 
    Serial.print("Button3 is pressed \n ");

  if (digitalRead(button4) == LOW) 
    Serial.print("Button4 is pressed \n ");

  if (digitalRead(button5) == LOW) 
    Serial.print("Button5 is pressed \n ");
 

}

