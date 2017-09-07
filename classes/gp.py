from .room import Room

class Gp(Room):

    def __init__(self, floor, room_num, r_capacity):
        self.doctor_list = []
        self.room_patient = []
        self.patient_list = []
        self.r_type = "GP"
        self.r_location = {"floor":floor, "room": room_num}
        Room(self.r_type, self.r_location, r_capacity, self.patient_list, self.doctor_list)

    #
    # def display_room(self):
    #     super().display_room()
    #     print("GP Doctor", self.room_doctor)
    #     print("Patient inside:", self.room_patient)
    #     print("Patients Waiting:", self.patient_queue)
    #


