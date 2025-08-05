
#include <Arduino.h>
#include <BLEDevice.h>
# include <Wire.h>
# include<LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);

#define MAX_DEVICES 1000

struct DeviceInfo {
  char address[18];
};

DeviceInfo devices[MAX_DEVICES];
int numDevices = 0;

const char* providedAddresses[] = {
"33:17:BC:4D:CA:12","30:C0:1B:96:56:CC", "67:41:c9:f6:fc:e3"
};

struct AttendanceInfo {
  char address[18];
};

AttendanceInfo attendance[MAX_DEVICES];


void setup() {
  Serial.begin(115200);
  BLEDevice::init("");
  Wire.begin(18,19);
  lcd.begin();

  lcd.backlight();

  
}
void loop(){

  BLEScan* pBLEScan = BLEDevice::getScan();
  pBLEScan->setActiveScan(true);

  BLEScanResults foundDevices = pBLEScan->start(5);

  int count = foundDevices.getCount();

  int numAttendance = 0;

  for (int i = 0; i < count; i++) {
    BLEAdvertisedDevice device = foundDevices.getDevice(i);

    if (numDevices < MAX_DEVICES) {
      const char* address = device.getAddress().toString().c_str();
      bool isNewDevice = true;

      // Check if the device is already in the list
      for (int j = 0; j < numDevices; j++) {
        if (strcmp(address, devices[j].address) == 0) {
          isNewDevice = false;
          break;
        }
      }

      // If it's a new device, add it to the list
      if (isNewDevice) {
        strncpy(devices[numDevices].address, address, sizeof(devices[numDevices].address));
        numDevices++;}

      // Check if the address is in the providedAddresses list
      for (int k = 0; k < sizeof(providedAddresses) / sizeof(providedAddresses[0]); k++) {
        if (strcmp(address, providedAddresses[k]) == 0) {
          if (numAttendance < MAX_DEVICES) {
            strncpy(attendance[numAttendance].address, address, sizeof(attendance[numAttendance].address));
            numAttendance++;
          }
          break;
        }
      }
    }
  }
Serial.println("All Discovered Devices:");
  for (int i = 0; i < numDevices; i++) {
    Serial.print("\"");
    Serial.print(devices[i].address);
    Serial.print("\"");
    Serial.println(",");
  }

  lcd.print("Attendance List:");
  delay(2000);
  lcd.clear();
  lcd.print("Total Present: ");
  lcd.print(numAttendance);
  delay(2000);
  lcd.clear();

  
  for (int i = 0; i < numAttendance; i++) {
    lcd.print(attendance[i].address);
    delay(4000);
    lcd.clear();
  }


  pBLEScan->clearResults();   
  delay(3000);
}