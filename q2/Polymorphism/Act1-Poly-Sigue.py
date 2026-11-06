class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")

class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

patient1 = Patient("Gabriel Ayop", 15000)
patient2 = SeniorPatient("Navy Ayop", 15000)
patient3 = PhilhealthPatient("Yve Ayop", 15000)

patients = [patient1, patient2, patient3]

print("Hospital Billing System")
print("------------------------")

for patient in patients:
    print("Patient Name:", patient.get_name())
    patient.display_patient_type()
    print("Original Bill: ₱{:,.2f}".format(patient.get_bill_amount()))
    print("Final Bill: ₱{:,.2f}".format(patient.calculate_bill()))
    print()
