class Car:
    def __init__(self, brand, model, battery=35):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        self.battery -= distance/20
        print("The car traveled",distance,"km")
        print("You have",self.battery,"wH left")
    def charge(self, wH):
        self.battery += wH
        print("Car recharged. You now have",self.battery,"wH")
    def dashboard(self):
        print("Battery:",self.battery)

mycar = Car("BYD","Seal 5")
mycar.go(100)
mycar.charge(5)
mycar.dashboard()
