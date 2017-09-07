from .room import Room


class Hospital:

    def __init__(self, h_name, h_capacity):
        self.h_name = h_name
        self.h_capacity = h_capacity
        self.patient_list = []
        self.room_list = []
        self.admit_list = []
        self.doctor_list = []
        self.available_doctor_list = []
        self.available_doctor_list = []
        self.booked_doctor_list = []
        self.busy_patient_list = []
        self.idle_patient_list = []

    def display_hospital(self):
        print("Hospital Name:", self.h_name)
        print("Hospital capacity", self.h_capacity)
        print("List of patients")
        for patient in self.patient_list:
            print(patient.p_name)
        print("List of rooms")
        for room in self.room_list:
            print(room.r_type)
        print("List of admissions")
        for patient in self.admit_list:
            print(patient.p_name)
        print("List of doctors")
        for doctor in self.doctor_list:
            print(doctor.p_name)
        print("List of available doctors")
        for doctor in self.available_doctor_list:
            print(doctor.p_name)
        print("List of booked doctors")
        for doctor in self.booked_doctor_list:
            print(doctor.p_name)

    def addPatient(self, patient):
        self.patient_list.append(patient)
        self.idle_patient_list.append(patient)
        print("Patient",patient.p_name,"added")

    def admitPatient(self, patient):
        if patient in self.patient_list:
            self.admit_list.append(patient)

    def addRoom(self, room):
        self.room_list.append(room)
        print("Room",room.r_type," added")

    def addDoctor(self, doctor):
        if self.doctor_list.__len__() <= self.h_capacity:
            self.doctor_list.append(doctor)
            self.available_doctor_list.append(doctor)
            print("Doctor",doctor.p_name, "added")
        else:
            print("Hospital is full. Doctor", doctor.p_name, "not added")

    def assignDoctor(self, doctor, room):
        if doctor in self.doctor_list and room in self.room_list:
            new_room = self.room_list[self.room_list.index(room)]
            new_doctor = self.doctor_list[self.doctor_list.index(doctor)]
            new_doctor.assign_room(new_room)
            new_room.add_doctor(new_doctor)
            self.booked_doctor_list.append(doctor)
            self.available_doctor_list.remove(doctor)

    def assignPatient(self, patient, room):
        if patient in self.patient_list and room in self.room_list:
            new_room = self.room_list[self.room_list.index(room)]
            new_patient = self.patient_list[self.patient_list.index(patient)]
            new_patient.assign_room(new_room)
            new_room.add_patient(new_patient)
            self.busy_patient_list.append(patient)
            self.idle_patient_list.remove(patient)

    def removeDoctor(self, doctor, room):
        doctor.leave_room(room)
        room.remove_doctor(doctor)
        self.available_doctor_list.append(doctor)
        self.booked_doctor_list.remove(doctor)

    def removePatient(self, patient, room):
        patient.leave_room(room)
        room.remove_doctor(patient)
        self.idle_patient_list.append(patient)
        self.busy_patient_list.remove(patient)

    def displayRoom(self, room):
        new_room = self.room_list[self.room_list.index(room)]
        new_room.display_room()

    def displayRoomList(self):
        if self.room_list:
            for room_num, room in enumerate(self.room_list):
                print(room_num, room.r_type)
            return 1
        else:
            return 0

