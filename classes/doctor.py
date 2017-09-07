from .person import Person

class Doctor(Person):

    def __init__(self, d_name, specialties):
        Person.__init__(self,"Doctor",d_name)
        self.specialties = specialties
        self.room_assignment = []

    def display_doctor(self):
        print("Doctor\'s name:", self.p_name)
        print("Specialties:", self.specialties)

    def assign_room(self, room):
        #self.room_assignment.clear()
        self.leave_room(room)
        self.room_assignment.append(room)

    def leave_room(self, room):
        self.room_assignment.clear()


