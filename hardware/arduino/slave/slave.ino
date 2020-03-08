float humedad=A0;
float humedityInput=0;
float iluminacion=A1;
float iluminacionInput=0;
float iluminacionOutput;
float tempInput;
float tempOutput;
int LM35=A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
// humedad
  humedityInput=(analogRead(humedad))/2;
// iluminacion
  iluminacionInput=analogRead(iluminacion);
  iluminacionOutput = (iluminacionInput/20)*iluminacionInput;
// temp
  tempInput=analogRead(LM35);
  tempOutput = tempInput*500/1024;
  
// Send data stream line
  Serial.print("<");
  Serial.print(tempOutput);
  Serial.print(",");
  Serial.print(humedityInput);
  Serial.print(",");
  Serial.print(iluminacionOutput);
  Serial.println(">");
  delay(2000);
}
