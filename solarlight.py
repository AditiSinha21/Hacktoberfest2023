const int ledPin = 12;  // Pin connected to the LED
const int solarVoltagePin = A0;  // Pin connected to the solar panel's voltage
const int batteryVoltagePin = A1;  // Pin connected to the battery voltage

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Read solar panel voltage
  int solarVoltage = analogRead(solarVoltagePin);
  
  // Read battery voltage
  int batteryVoltage = analogRead(batteryVoltagePin);

  // Check if it's dark (nighttime) - you may need to adjust this threshold based on your setup
  if (solarVoltage < 100 && batteryVoltage > 100) {
    // It's dark, turn on the LED
    digitalWrite(ledPin, HIGH);
  } else {
    // It's light, turn off the LED
    digitalWrite(ledPin, LOW);
  }
}
