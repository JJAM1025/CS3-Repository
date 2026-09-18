class Tusoktusok:
    name = ""
    sauce = [] # -> for 1:N
    # sauce = None -> for 1:1
    def __init__(self, name):
        self.name = name
    def dip(self, sauce):
        self.sauce.append(sauce)
        # self.sauce = sauce
    def eat(self):
        print("I ate", self.name, "with", end=" ")
        [print(s.name, end = " ")for s in self.sauce]
        print("and it tastes", end = " ")
        [print(s.taste, end = " ") for s in self.sauce]
        print()

class Sauce:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

fishball = Tusoktusok("fishball")
vinegar = Sauce("vinegar", "sour")
fishball.dip(vinegar)
fishball.eat()
