
from abc import ABC, abstractmethod


# TASK 1: Create an Abstract Base Class
class Sensor(ABC):

    # TASK 2: Create an abstract method
    @abstractmethod
    def get_reading(self):
        pass


# TASK 3: Create the pH Sensor child class
class PHSensor(Sensor):

    def get_reading(self):
        return "7.2 pH"


# TASK 3: Create the Temperature Sensor child class
class TempSensor(Sensor):

    def get_reading(self):
        return "24.5°C"


# TASK 4: Display the sensor readings
print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

print(f"[pH Sensor] Reading: {ph_sensor.get_reading()}")
print(f"[Temperature Sensor] Reading: {temp_sensor.get_reading()}")

print("------------------------------")


# TASK 5: Test the abstract class
# This intentionally produces a TypeError.
my_sensor = Sensor()
