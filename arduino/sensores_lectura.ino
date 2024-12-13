#include <DHT.h>
#include <ArduinoJson.h>

// Configuración de pines
#define DHTPIN 2           // Pin digital para DHT11
#define DHTTYPE DHT11      
const int SOIL_PIN = A0;   // Pin analógico para sensor de humedad de suelo
const int MQ135_PIN = 8;   // Pin digital para MQ-135

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    dht.begin();
    pinMode(MQ135_PIN, INPUT);
}

void loop() {
    // Leer sensores
    float temperatura = dht.readTemperature();
    float humedad = dht.readHumidity();
    int humedadSuelo = analogRead(SOIL_PIN);
    int gasDetectado = digitalRead(MQ135_PIN);
    
    // Convertir humedad del suelo a porcentaje
    int humedadSueloPorcentaje = map(humedadSuelo, 0, 1023, 100, 0);
    humedadSueloPorcentaje = constrain(humedadSueloPorcentaje, 0, 100);

    // Crear JSON con las lecturas
    Serial.print("{");
    Serial.print("\"temperatura\":");
    Serial.print(temperatura);
    Serial.print(",\"humedad\":");
    Serial.print(humedad);
    Serial.print(",\"humedad_suelo\":");
    Serial.print(humedadSueloPorcentaje);
    Serial.print(",\"co2_detectado\":");
    Serial.print(gasDetectado);
    Serial.println("}");

    delay(5000);  // Lectura cada 5 segundos
}