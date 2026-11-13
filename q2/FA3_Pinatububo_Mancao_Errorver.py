from abc import ABC, abstractmethod 
class Sensor(ABC):
    @abstractmethod
    def get_reading(self): 
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"

pHSensor = PHSensor()
tempSensor = TempSensor()
my_sensor = Sensor() # Error

print("--- Lab Inventory System ---")
print(pHSensor.get_reading())
print(tempSensor.get_reading())
print("\n----------------------------")
