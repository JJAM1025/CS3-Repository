class Patient:
    __name: str # Objects __name and __bill_amount have a double underscore because they are private (as seen in the class diagram).
    __bill_amount: float
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount) # Float function to turn the inputted number into a float).
        if self.__bill_amount < 0:
            print("Bill amount must not be lower than 0.")
    def get_name(self): # Get_name() so that the variable __name can be accessed in different classes.
        return self.__name
    def set_name(self, name): # Set_name(name) to update the __name variable if needed.
        self.__name = name
    def get_bill_amount(self): # Get_bill_amount() so that the variable __bill_amount can be accessed in different classes.
        return self.__bill_amount
    def set_bill_amount(self, bill_amount): # Set_bill_amount(bill_amount) to update the __bill_amount variable if needed.
        self.__bill_amount = bill_amount
    def calculate_bill(self): # Receipt, showing the original and discounted bill amount.
        print(f"Patient Name: {self.__name}\nOriginal Bill: {self.__bill_amount}\nFinal Bill: {self.__bill_amount}\n")

class SeniorPatient(Patient): # SeniorPatient(Patient) because Patient will be the parent class. We can now access public variables.
    def calculate_bill(self): # Receipt, showing the original and discounted bill amount. Function also includes calculation for the 20% discount.
        self.finalbill = self.get_bill_amount()*0.8
        print(f"Patient Name: {self.get_name()}\nOriginal Bill: {self.get_bill_amount()}\nFinal Bill: {self.finalbill}\n")

class PhilHealthPatient(Patient): # PhilHealth(Patient), the reason being exactly the same as SeniorPatient(Patient).
    def calculate_bill(self): # Receipt, showing the original and discounted bill amount. Function also includes calculation for the 15% discount.
        self.finalbill = self.get_bill_amount()*0.85
        print(f"Patient Name: {self.get_name()}\nOriginal Bill: {self.get_bill_amount()}\nFinal Bill: {self.finalbill}\n")

# TESTING
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
regular_patient.calculate_bill()
senior_patient.calculate_bill()
philhealth_patient.calculate_bill()
