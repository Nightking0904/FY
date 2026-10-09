// Done by Roll no. : 162, 163, 164, 165


void setup() {
  // put your setup code here, to run once:
 pinMode(3 , OUTPUT);
 pinMode(4 , OUTPUT);
 pinMode(5 , OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(3 , HIGH);
delay(3000);
digitalWrite(3 , LOW);
digitalWrite(4 , HIGH);
delay(1000);
digitalWrite(4 ,LOW);
digitalWrite(5 , HIGH);
delay(3000);
digitalWrite(5 , LOW);
}
