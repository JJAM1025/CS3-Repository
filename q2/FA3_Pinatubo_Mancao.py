from abc import ABC, abstractmethod # Important tool: ABC (Abstract Base Class). Exists only to be a blueprint.

class Sensor(ABC):
    @abstractmethod # Decorator. Basically a strict rule where you are telling Python every child class must have their own version of this action.
    def get_reading(self): # Abstract method. Every child class MUST have this method.
        pass

class PHSensor(Sensor):
    def get_reading(self): # get_reading() implemented from class Sensor()
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self): # get_reading() implemented from class Sensor()
        return "[Temperature Sensor] Reading: 24.5°C"

pHSensor = PHSensor()
tempSensor = TempSensor()

# Printing for the terminal
print("--- Lab Inventory System ---")
print(pHSensor.get_reading())
print(tempSensor.get_reading())
print("\n----------------------------")
