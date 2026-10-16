class Father:
    eyes = "blue eyes"

class Mother:
    hair = "black hair"

class You(Father, Mother):
    def describeYourself(self):
        print("I have", self.eyes, "and", self.hair)

you = You()
you.describeYourself()
