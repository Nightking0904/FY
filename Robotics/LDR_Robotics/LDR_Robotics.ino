void setup() {
Serial.begin(9600);
delay(1500);
  pinMode(2, OUTPUT);
}

void loop() {
  int var1 = analogRead(A0);

    Serial.print("Sensor value= ");
    Serial.print(var1);
      if (var1 > 600) {
        Serial.println(" -> It's dark, turn lights ON");
        digitalWrite(2, HIGH);
    delay(50);
    }
    else { Serial.println(" ->Turn lights OFF");
      digitalWrite(2, LOW);
    delay(50);
    }
}

