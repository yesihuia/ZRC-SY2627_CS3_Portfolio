
from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):

    def get_reading(self):
        return "7.2 pH"

class TempSensor(Sensor):

    def get_reading(self):
        return "24.5°C"

print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

print(f"[pH Sensor] Reading: {ph_sensor.get_reading()}")
print(f"[Temperature Sensor] Reading: {temp_sensor.get_reading()}")

print("------------------------------")

my_sensor = Sensor()
