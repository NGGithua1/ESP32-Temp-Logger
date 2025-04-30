#include <OneWire.h>
#include <DallasTemperature.h>

// GPIO pin connected to DS18B20 data line
#define ONE_WIRE_BUS 14

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);

  sensors.begin();
  Serial.println("Timestamp (ms), Temperature (°C)");
}

void loop() {
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);

  unsigned long timestamp = millis();
  Serial.print(timestamp);
  Serial.print(", ");
  Serial.println(temperatureC);
  const int serialprintInterval = 0; //increase value to slow down serial print activity
    //delay(10); 
}
