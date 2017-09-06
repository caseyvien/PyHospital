from .room import Room

class Gp(Room):

    def __init__(self, floor, room):
        Room("GP", {"floor":floor, "room": room})
        self.room_doctor = []
        self.room_patient = []
        self.patient_queue = []

    def display_room(self):
        super().display_room()
        print("GP Doctor", self.room_doctor)
        print("Patient inside:", self.room_patient)
        print("Patients Waiting:", self.patient_queue)


