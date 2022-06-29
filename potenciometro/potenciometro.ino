const int potenciometro = 0; // pino de entrada do potenciômetro
int valor = A0;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  valor = analogRead(potenciometro);

  String dataString = "";

  int rank = 1;

  dataString += String(valor*0.1); //estado carga
  dataString += ",";
  dataString += String(valor*0.147); // velocidade
  dataString += ",";
  dataString += String(valor*0.09); //t1
  dataString += ",";
  dataString += String(valor*0.099); //t2
  dataString += ",";
  dataString += String(valor*0.08); //t3
  dataString += ",";
  dataString += String(valor*0.088); //t4
  dataString += ",";
  dataString += String(valor*1.1); //r1
  dataString += ",";
  dataString += String(valor*1.1); //r2
  dataString += ",";
  dataString += String(valor); //r3
  dataString += ",";
  dataString += String(valor); //r4
  dataString += ",";
  dataString += String(valor*0.08999); //tm
  
  Serial.println(dataString);
  
  delay(500);
}
