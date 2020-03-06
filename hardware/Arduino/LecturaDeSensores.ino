int jose=13;
float humedad=A0;
int lectura=0;
float iluminacion=A1;
int lectura1=0;
float temperatura;
int LM35=A2;

void setup() {
  pinMode(jose,OUTPUT);
  Serial.begin(9600);
}

void loop() {
//LED
  digitalWrite(jose,HIGH);
  delay(500);
  digitalWrite(jose,LOW);
  delay(500);
//humedad
  lectura=(analogRead(humedad))/2;
  Serial.print("Nivel de humedad: ");
  Serial.print(lectura);
  Serial.println("%");
//iluminacion
  lectura1=analogRead(iluminacion);
  Serial.print("Nivel de iluminación: ");
  Serial.print((lectura1/20)*lectura1);
  Serial.println("%");
//temperatura
  temperatura=(analogRead(LM35))*500/1024;
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println("°C");
}
