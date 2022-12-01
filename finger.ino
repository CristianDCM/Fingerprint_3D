// codigo para lecto de huella digital
#include <SoftwareSerial.h>
#include <Adafruit_Fingerprint.h>
SoftwareSerial mySerial(2, 3); // RX, TX
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);
void setup()
{
    Serial.begin(9600);
    Serial.println("Prueba de detección de huella digital");
    mySerial.begin(57600);
    if (finger.verifyPassword())
    {
        Serial.println("¡Sensor de huellas dactilares encontrado!");
    }
    else
    {
        Serial.println("No encontré el sensor de huellas dactilares :(");
        while (1)
        {
            delay(1);
        }
    }
    finger.getTemplateCount();
    Serial.print("El sensor contiene");
    Serial.print(finger.templateCount);
    Serial.println(" plantillas");
    Serial.println("Esperando un dedo válido...");
}
void loop()
{
    uint8_t p = finger.getImage();
    if (p != FINGERPRINT_OK)
        return;
    p = finger.image2Tz();
    if (p != FINGERPRINT_OK)
        return;
    p = finger.fingerFastSearch();
    if (p != FINGERPRINT_OK)
    {
        Serial.println("No se encontraron coincidencias");
        return;
    }
    Serial.print("Identificación de huella digital encontrada #");
    Serial.print(finger.fingerID);
    Serial.print(" con confianza de");
    Serial.println(finger.confidence);
}
