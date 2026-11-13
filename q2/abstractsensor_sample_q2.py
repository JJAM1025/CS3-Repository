from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
        return "26 deg C"
    def __str__(self):
        return "26 deg C"

tempSensor = TempSensor()
print(tempSensor.get_data())
print(tempSensor)
