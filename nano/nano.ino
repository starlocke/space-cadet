String incoming = "";
int on_duration = 15;
int off_duration = 1500;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    incoming = Serial.readString();
    if(incoming.toInt() > 0){
      off_duration = incoming.toInt();
      incoming = "";
    }
    if(incoming.toInt() < 0){
      on_duration = -(incoming.toInt());
      incoming = "";
    }
  }
  digitalWrite(LED_BUILTIN, HIGH);
  delay(on_duration);
  digitalWrite(LED_BUILTIN, LOW);
  delay(off_duration);
}
