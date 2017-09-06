from classes.hospital import Hospital
from classes.patient import Patient
from classes.doctor import Doctor
import random


sickness_array = ["diabetes", "fever", "hypertension", "broken leg"]
specialty_array = ["General Practice", "Dermatology", "Orthodontics", "Dentistry", "Pediatrics"]

new_hospital = Hospital("KN Hospital", 50)
'''
patient1 = Patient("John Doe",["diabetes","fever"])
patient2 = Patient("Jane Doe",["broken leg"])
patient1.display_patient()
new_hospital.addPatient(patient1)
new_hospital.addPatient(patient2)

doctor1 = Doctor("Dr Who", ["General Practice", "Dermatology"])
new_hospital.addDoctor(doctor1)

new_hospital.display_hospital();
new_hospital.admitPatient(patient1)

print("\n\n")
new_hospital.display_hospital();
'''
run = True
print("Welcome to", new_hospital.h_name, "\n")
while run:
    print("[1]Add Patient [2]Add Doctor [3]Add Room [4]Display Hospital [0]Quit")
    user_command = input("Enter Choice: ")
    if user_command == "0":
        run = False
    elif user_command == "1":
        new_patient = Patient(input("Enter Name:"), sickness_array[random.randrange(0, sickness_array.__len__())])
        new_hospital.addPatient(new_patient)
        new_patient.display_patient()
    elif user_command == "2":
        new_doctor = Doctor(input("Enter Doctor Name:"), specialty_array[random.randrange(0, specialty_array.__len__())])
        new_hospital.addDoctor(new_doctor)
        new_doctor.display_doctor()
    elif user_command == "4":
        new_hospital.display_hospital()