from abc import ABC, abstractmethod

class Sensor(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):

    def __init__(self):
        super().__init__("pH Sensor")

    def get_reading(self):
        return "7.2 pH"

class TempSensor(Sensor):

    def __init__(self):
        super().__init__("Temperature Sensor")

    def get_reading(self):
        return "24.5°C"

print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

print(f"[{ph_sensor.name}] Reading: {ph_sensor.get_reading()}")
print(f"[{temp_sensor.name}] Reading: {temp_sensor.get_reading()}")

print("------------------------------")

my_sensor = Sensor()

