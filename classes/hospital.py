class Hospital:

    def __init__(self, h_name, h_capacity):
        self.h_name = h_name
        self.h_capacity = h_capacity
        self.patient_list = []
        self.room_list = []
        self.admit_list = []
        self.doctor_list = []

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

    def addPatient(self, patient):
        self.patient_list.append(patient)
        print("Patient",patient.p_name,"added")

    def admitPatient(self, patient):
        if patient in self.patient_list:
            self.admit_list.append(patient)

    def addRoom(self, room):
        self.room_list.append(room)
        print("Room",room.r_type,"added")

    def addDoctor(self, doctor):
        self.doctor_list.append(doctor)
        print("Doctor",doctor.p_name, "added")
