long randNumber;
 
void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}
 
void loop() {

  String dataString = "";

  dataString += String(random(100)); //estado carga
  dataString += ",";
  dataString += String(random(150)); // velocidade
  dataString += ",";
  dataString += String(random(100)); //t1
  dataString += ",";
  dataString += String(random(100)); //t2
  dataString += ",";
  dataString += String(random(100)); //t3
  dataString += ",";
  dataString += String(random(100)); //t4
  dataString += ",";
  dataString += String(random(1000)); //r1
  dataString += ",";
  dataString += String(random(1000)); //r2
  dataString += ",";
  dataString += String(random(1000)); //r3
  dataString += ",";
  dataString += String(random(1000)); //r4
  dataString += ",";
  dataString += String(random(100)); //tm
  
  Serial.println(dataString);
  
  delay(250);
}
