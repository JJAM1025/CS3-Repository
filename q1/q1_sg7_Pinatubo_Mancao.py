class Glassware:
    def __init__(self, name):
        self.name = name

class Beaker(Glassware):
    def __init__(self):
        super().__init__(name="Beaker")

class Tray:
    def __init__(self):
        self.beakers = [Beaker() for i in range(5)]
