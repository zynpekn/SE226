int LED1pin = 44;
int LED2pin = 43;
int LED3pin = 45;
int LED4pin = 46;

int button1pin = 30;
int button2pin = 31;
int button3pin = 32;
int button4pin = 33;

int LED1state = LOW;
int LED2state = LOW;
int LED3state = LOW;
int LED4state = LOW;

int lastButton1state = LOW;
int lastButton2state = LOW;
int lastButton3state = LOW;
int lastButton4state = LOW;

void setup() {
  pinMode(LED1pin, OUTPUT);
  pinMode(LED2pin, OUTPUT);
  pinMode(LED3pin, OUTPUT);
  pinMode(LED4pin, OUTPUT);

  pinMode(button1pin, INPUT);
  pinMode(button2pin, INPUT);
  pinMode(button3pin, INPUT);
  pinMode(button4pin, INPUT);
}

void loop() {
  int button1state = digitalRead(button1pin);
  int button2state = digitalRead(button2pin);
  int button3state = digitalRead(button3pin);
  int button4state = digitalRead(button4pin);

  if (button1state == HIGH && lastButton1state == LOW) {
    LED1state = !LED1state;
    digitalWrite(LED1pin, LED1state);
    delay(200);
  }

  if (button2state == HIGH && lastButton2state == LOW) {
    LED2state = !LED2state;
    digitalWrite(LED2pin, LED2state);
    delay(200);
  }

  if (button3state == HIGH && lastButton3state == LOW) {
    LED3state = !LED3state;
    digitalWrite(LED3pin, LED3state);
    delay(200);
  }

  if (button4state == HIGH && lastButton4state == LOW) {
    LED4state = !LED4state;
    digitalWrite(LED4pin, LED4state);
    delay(200);
  }

  lastButton1state = button1state;
  lastButton2state = button2state;
  lastButton3state = button3state;
  lastButton4state = button4state;
}