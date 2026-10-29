
# Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = 0
        self.set_bill_amount(bill_amount)

    # Getter methods
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")
        self.__bill_amount = bill_amount

    # Calculate full bill
    def calculate_bill(self):
        return self.__bill_amount


# Child class: Senior Patient
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


# Child class: PhilHealth Patient
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# Create one object per class
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)


# Display patient bills
print("Hospital Billing System")
print("-----------------------")

patients = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

for patient in patients:
    print("Patient Name: ", patient.get_name())
    print("Original Bill: ₱{:,.2f}".format(
        patient.get_bill_amount()
    ))
    print("Final Bill: ₱{:,.2f}".format(
        patient.calculate_bill()
    ))
    print()
