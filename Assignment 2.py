class Patient:
    """Class to represent a patient"""
    # Using initializing constructor to initialize attributes of Patient class
    def __init__(self, name, birth_date, gender, medical_history, condition, medications):
        # Initializing attributes
        self._name = name
        self._birth_date = birth_date
        self._gender = gender
        self._medical_history = medical_history
        self._condition = condition
        self._medications = medications

class ConsultationQueue:
    """Class that represents line of patients waiting for consultation, using FIFO"""
    def __init__(self):
        #Creating an empty list of items for queue
        self.items = []
    
    #The enqueue will add a patient to the line of patients waiting for consultation
    def enqueue(self, patient):
        #it appends the patient to items lists
        self.items.append(patient)

    #The dequeue will remove the first patient (at index 0) from the queue
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    #is Empty will check if the queue is empty
    def isEmpty(self):
        return self.items == []

#Creating patient 1 as an object and displaying its attributes
patient1 = Patient("Fatma", "02/06/2004", "Female", "None", "Fever", "Antibiotic")
#Creating patient 2 as an object and displaying its attributes
patient2 = Patient("Mohammad", "05/11/1998", "Male", "None", "Diabetes", "Insulin")
#Creating patient 3 as an object and displaying its attributes
patient3 = Patient("Hessa", "28/3/2001", "Female", "Asthma", "Allergy", "Aspirin")

#Implement the Queue on consultation variable
consultation = ConsultationQueue()
#add patients to the consultation queue using enqueue
consultation.enqueue(patient1)
consultation.enqueue(patient2)
consultation.enqueue(patient3)

#Remove the patients from the consultation queue using dequeue and print their names
print("Dequeuing Patients")
print(consultation.dequeue()._name)
print(consultation.dequeue()._name)
print(consultation.dequeue()._name)

class ManagementSystem:
    """Class to represent patient record management system"""
    def __init__(self):
        self.patients = [] # create a new list to collect the patients


    def adding_patientrecord(self, patient): # define a function to add a new patient record by using append function
        self.patients.append(patient)


    def update_patientrecord(self, patient_name, new_information): # define a function to update a patient record using the a new argument patient_name and new_information
        for patient in self.patients: # Iterate through the patients in the patient list
            if patient._name == patient_name: # If a new given patient name is similar to an existed patient name
                patient._medical_history = new_information.get('medical_history', patient._medical_history) # update their medical history
                patient._condition = new_information.get('condition', patient._condition) # update the patient condition


    def remove_patientrecord(self, patient_name): # define a function to remove patient record
        for patient in self.patients: # Iterate through every patient in the patient list
            if patient._name == patient_name: # If a new given patient name is similar to an existed patient name
                self.patients.remove(patient) # select the patient and remove it from the list
                break # use the break statement to exit the loop


    #define a function to search for a patient
    def search(self, name):
        #for loop to iterate through the list of patients
        for patient in self.patients:
            #if the name is equal to the name being search it will return the patient
            if patient._name == name:
                return patient
        #Otherwise if the name is not found, it will return None
        return None

    #define a function to organize patients based on condition
    def organize_condition(self, patient):
        #create a dictionary that puts value based on conditon's severity
        condition = {"Infection":1, "Diabetes":2, "Fever":3, "Allergy":4}
        #the 4 represents the defined key conditions in the dictionary
        return condition.get(patient._condition,  4)
    #define a function to sort the conditions
    def sort_condition(self):
        #sort patients using the organize_condition key
        self.patients.sort(key=self.organize_condition)

class Doctor: # Create a class to represent the doctors
    """Class to represent a doctor"""
    def __init__(self, doctor_name, specialty): # add the doctor name and specialty as an attributes of the doctor class
        self._doctor_name = doctor_name
        self._specialty = specialty

class AppointmentScheduler: # create another class to represent the appointment scheduler system
    def __init__(self):
        # create an appointment dictionary
        self.appointments = {}

    def schedule_appointment(self, patient_name, doctor): # define a function for scheduling an appointment and use the patient_naem and doctor class arguments
        self.appointments[patient_name] = doctor # for a given patient name, assign a doctor, and add them in the appointments dictionary


# test case: Add a new patient record, including personal details, medical history, and current condition.
patient_manager = ManagementSystem()
patient_manager.adding_patientrecord(patient1)
patient_manager.adding_patientrecord(patient2)
patient_manager.adding_patientrecord(patient3)

# test case: Update an existing patient record with new information or medical updates.
new_information = {'medical_history': 'Allergies, Diabetes', 'condition': 'Stable'}
patient_manager.update_patientrecord('Fatma', new_information)

# test case: Remove a patient record from the queue upon discharge or transfer to another facility.
patient_manager.remove_patientrecord('Mohammad')

# test case: Schedule an appointment for a patient with a specific doctor.
doctor1 = Doctor("Dr. Mariam", "Endocrinologist")
scheduler = AppointmentScheduler()
scheduler.schedule_appointment('Fatma', doctor1)

#test case: search for a specific patient from the patients list
patient_name = "Fatma"
patient = patient_manager.search(patient_name)
#If the patient is found it will print a summary of the patient details
if patient:
   doctor = scheduler.appointments.get(patient_name)
   print("Patient Summary:")
   print("Name:", patient._name)
   print("Date of Birth:", patient._birth_date)
   print("Gender:", patient._gender)
   print("Medical History:", patient._medical_history)
   print("Condition:", patient._condition)
   #if the patient has a scheduled appointment with a doctor print details
   if doctor:
       print("Appointment Details:")
       print(doctor._doctor_name)
       print("Specialty:", doctor._specialty)
   #otherwise, print doctor not scheduled yet
   else:
       print("Doctor: Not scheduled yet")
#However, if the patient is not found it will print Patient not found
else:
   print("Patient not found")

#test case: sort patients based on condition
patient_manager.sort_condition()
print("Patients records sorted by medical condition:")
#print the name of the patient and their condition
for patient in patient_manager.patients:
   print(patient._name, ", Condition:", patient._condition)


class Stack:
   """Class to represent a stack to manage the stack of prescriptions"""
   def __init__(self):
       #Create an empty list for stack
       self.stack = []

   #The push function will add prescription onto the stack
   def push (self, prescription):
       self.stack.append(prescription)

   #The pop function will remove the last prescription added (top) to the stack
   def pop(self):
       return self.stack.pop()

   #is Empty will check if the stack is empty
   def isEmpty(self):
       return self.stack == []

class Prescription:
   """Class to represent a prescription"""
   def __init__(self):
       #Implement the Stack() to self.stack
       self.stack = Stack()

   #defining a function to issue prescription with its attributes
   def issue_prescription(self, patient, medication, dose, duration):
       #Creating a prescription variable that has the attributes
       prescription = (patient, medication, dose, duration)
       #Push the prescription onto the stack
       self.stack.push(prescription)

#Creating prescriptions from the Prescription class
prescription = Prescription()
#Issuing a prescription for the patients and including its attributes
prescription.issue_prescription("Fatma", "Antibiotic", "1 mg", "4 days")
prescription.issue_prescription("Mohammad", "Insulin", "10 units", "1 day")
prescription.issue_prescription("Hessa", "Aspirin", "2 mg", "3 days")

#Check if the prescription stack is empty, if it is print no issued prescriptions
if prescription.stack.isEmpty():
   print("No issued prescriptions")
#If the prescription stack is not empty pop the patient's prescription and print it
else:
   issued_prescription = prescription.stack.pop()
   print("Prescription:", issued_prescription)
   issued_prescription = prescription.stack.pop()
   print("Prescription:", issued_prescription)
   issued_prescription = prescription.stack.pop()
   print("Prescription:", issued_prescription)
