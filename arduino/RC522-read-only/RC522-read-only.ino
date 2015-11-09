#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           
#define SS_PIN          10         

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

MFRC522::MIFARE_Key key;

byte tag_id[5];

/**
 * Initialize.
 */
void setup() {
    Serial.begin(9600); // Initialize serial communications with the PC
    while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
    SPI.begin();        // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card
    Serial.println("Iniciando programa lectura RFID...");
}

/**
 * Main loop.
 */
void loop() {
    // Look for new cards
    if ( ! mfrc522.PICC_IsNewCardPresent())
        return;

    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial())
        return;

    // Show some details of the PICC (that is: the tag/card)
    Serial.print(F("Card UID:"));
    dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
    Serial.println();
    
    Serial.print(F("PICC type: "));
    byte piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
    Serial.println(mfrc522.PICC_GetTypeName(piccType));

    Serial.print("Stored Data: ");
    int i;
    for (i = 0; i < sizeof(tag_id) - 1; i++)
    {
      Serial.print(tag_id[i], HEX);
    }
    Serial.println();
    Serial.println("End...");

    delay(1000);
}

/**
 * Helper routine to dump a byte array as hex values to Serial.
 */
void dump_byte_array(byte *buffer, byte bufferSize) {

    for (byte i = 0; i < bufferSize; i++) {
      
        Serial.print(buffer[i] < 0x10 ? " 0":""); 
        Serial.print(buffer[i], HEX);
        tag_id[i] = buffer[i];       
    }
  
}
