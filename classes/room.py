class Room:

    def __init__(self, r_type, r_location, r_capacity, patient_list, doctor_list):
        self.r_type = r_type
        self.r_location = r_location
        self.patient_list = patient_list
        self.doctor_list = doctor_list
        self.r_capacity = r_capacity

    def display_room(self):
        print("Room Type:", self.r_type)
        print("Room Location:", self.r_location)
        if not self.patient_list:
            print("Is room occupied: No")
        else:
            print("Is room occupied: Yes, patient list below")
            for patient in self.patient_list:
                print("Patient#", patient_list.index(patient)," ", patient)
        if not self.doctor_list:
            print("Does the room have a doctor: No")
        else:
            print("Does the room have a doctor: Yes, patient list below")
            for doctor in self.doctor_list:
                print("Doctor#", self.doctor_list.index(doctor)," ", doctor.p_name)
        #print("Has doctor:", self.has_doctor)

    def add_doctor(self, doctor):
        self.doctor_list.append(doctor)
        print("Doctor",doctor.p_name, "added to ", self.r_type)

    def add_patient(self, patient):
        self.patient_list.append(patient)
        print("Patient ", patient.p_name, "added to", self.r_type)
        patient.is_queued = True

