class Patient:
    """Class to represent a patient"""
    def __init__(self, name, birth_date, gender, medical_history, condition, medications):
        self._name = name
        self._birth_date = birth_date
        self._gender = gender
        self._medical_history = medical_history
        self._condition = condition
        self._medications = medications

class ConsultationQueue:
    """Class that represents line of patients waiting for consultation, using FIFO"""
    def __init__(self):
        self.items = []

    def enqueue(self, patient):
        self.items.append(patient)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return self.items == []

class ManagementSystem:
    """Class to represent patient record management system"""
    def __init__(self):
        self.patients = []

    def adding_patientrecord(self, patient):
        self.patients.append(patient)

    def update_patientrecord(self, patient_name, new_information):
        for patient in self.patients:
            if patient._name == patient_name:
                patient._medical_history = new_information.get('medical_history', patient._medical_history)
                patient._condition = new_information.get('condition', patient._condition)

    def remove_patientrecord(self, patient_name):
        for patient in self.patients:
            if patient._name == patient_name:
                self.patients.remove(patient)
                break

    def search(self, name):
        for patient in self.patients:
            if patient._name == name:
                return patient
        return None

    def organize_condition(self, patient):
        condition = {"Infection":1, "Diabetes":2, "Fever":3, "Allergy":4}
        return condition.get(patient._condition,  4)

    def sort_condition(self):
        self.patients.sort(key=self.organize_condition)

class Doctor:
    """Class to represent a doctor"""
    def __init__(self, doctor_name, specialty):
        self._doctor_name = doctor_name
        self._specialty = specialty

class AppointmentScheduler:
    """Class to represent the appointment scheduler system"""
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, patient_name, doctor):
        self.appointments[patient_name] = doctor

class Stack:
    """Class to represent a stack to manage the stack of prescriptions"""
    def __init__(self):
        self.stack = []

    def push(self, prescription):
        self.stack.append(prescription)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

class Prescription:
    """Class to represent a prescription"""
    def __init__(self):
        self.stack = Stack()

    def issue_prescription(self, patient, medication, dose, duration):
        prescription = (patient, medication, dose, duration)
        self.stack.push(prescription)

# Function to display the menu
def display_menu():
    print("Welcome to the Hospital Management System")
    print("1. Add Patient Record")
    print("2. Update Patient Record")
    print("3. Remove Patient Record")
    print("4. Search Patient")
    print("5. Schedule Appointment")
    print("6. Display Patient Records Sorted by Condition")
    print("7. Issue Prescriptions")
    print("8. Exit")

# Function to add a patient record
def add_patient_record():
    name = input("Enter patient name: ")
    birth_date = input("Enter patient birth date (DD/MM/YYYY): ")
    gender = input("Enter patient gender: ")
    medical_history = input("Enter patient medical history: ")
    condition = input("Enter patient condition: ")
    medications = input("Enter patient medications: ")
    patient = Patient(name, birth_date, gender, medical_history, condition, medications)
    patient_manager.adding_patientrecord(patient)

# Function to update a patient record
def update_patient_record():
    name = input("Enter patient name: ")
    new_information = {}
    medical_history = input("Enter new medical history (Leave blank to keep current): ")
    condition = input("Enter new condition (Leave blank to keep current): ")
    if medical_history:
        new_information['medical_history'] = medical_history
    if condition:
        new_information['condition'] = condition
    patient_manager.update_patientrecord(name, new_information)

# Function to remove a patient record
def remove_patient_record():
    name = input("Enter patient name: ")
    patient_manager.remove_patientrecord(name)

# Function to search for a patient
def search_patient():
    name = input("Enter patient name: ")
    patient = patient_manager.search(name)
    if patient:
        print("Patient found:")
        print("Name:", patient._name)
        print("Birth Date:", patient._birth_date)
        print("Gender:", patient._gender)
        print("Medical History:", patient._medical_history)
        print("Condition:", patient._condition)
        print("Medications:", patient._medications)
    else:
        print("Patient not found")

# Function to schedule an appointment
def schedule_appointment():
    name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    specialty = input("Enter doctor specialty: ")
    doctor = Doctor(doctor_name, specialty)
    scheduler.schedule_appointment(name, doctor)

# Function to display patient records sorted by condition
def display_patient_records_sorted_by_condition():
    patient_manager.sort_condition()
    print("Patients records sorted by medical condition:")
    for patient in patient_manager.patients:
        print("Name:", patient._name)
        print("Condition:", patient._condition)

# Function to issue prescriptions
def issue_prescriptions():
    print("Issuing prescriptions:")
    prescription.issue_prescription("Fatma", "Antibiotic", "1 mg", "4 days")
    prescription.issue_prescription("Mohammad", "Insulin", "10 units", "1 day")
    prescription.issue_prescription("Hessa", "Aspirin", "2 mg", "3 days")
    while not prescription.stack.isEmpty():
        issued_prescription = prescription.stack.pop()
        print("Prescription:", issued_prescription)

# Main function to run the menu-based interface
if __name__ == "__main__":
    patient_manager = ManagementSystem()
    scheduler = AppointmentScheduler()
    prescription = Prescription()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_patient_record()
        elif choice == '2':
            update_patient_record()
        elif choice == '3':
            remove_patient_record()
        elif choice == '4':
            search_patient()
        elif choice == '5':
            schedule_appointment()
        elif choice == '6':
            display_patient_records_sorted_by_condition()
        elif choice == '7':
            issue_prescriptions()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
