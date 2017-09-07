from classes.hospital import Hospital
from classes.patient import Patient
from classes.doctor import Doctor
from classes.room import Room
from classes.gp import Gp
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
    print("[1]Add Patient \n"
          "[2]Add Doctor \n"
          "[3]Add Room \n"
          "[4]Assign Doctor to Room \n"
          "[5]Assign Patient to Room \n"
          "[6]Display Room \n"
          "[9]Display Hospital \n"
          "[0]Quit")
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
    elif user_command == "3":
        new_roomtype = input("Enter room type: [1]GP [2]Cancel")
        if new_roomtype == "1":
            new_gp = Gp(1, new_hospital.room_list.__len__(), 1)
            new_hospital.addRoom(new_gp)
            new_gp.display_room()
    elif user_command == "4":
        if new_hospital.displayRoomList():
            add_room_command = input("Select room number: ")
            if int(add_room_command) <= new_hospital.room_list.__len__():
                selected_room = new_hospital.room_list[int(add_room_command)]
            for doc_num, doctor in enumerate(new_hospital.doctor_list):
                print(doc_num, doctor.p_name)
            add_doctor_command = input("Select doctor number: ")
            if int(add_doctor_command) <= new_hospital.room_list.__len__():
                selected_doctor = new_hospital.doctor_list[int(add_doctor_command)]
                new_hospital.assignDoctor(selected_doctor, selected_room)
        else:
            print("No rooms created")
    elif user_command == "6":
        if new_hospital.displayRoomList():
            add_room_command = input("Select room number: ")
            selected_room = new_hospital.room_list[int(add_room_command)]
            new_hospital.displayRoom(selected_room)
        else:
            print("No rooms created")
    elif user_command == "9":
        new_hospital.display_hospital()