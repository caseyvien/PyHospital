from .person import Person

class Doctor(Person):

    def __init__(self, d_name, specialties):
        Person.__init__(self,"Doctor",d_name)
        self.specialties = specialties
        self.current_room = []

    def display_doctor(self):
        print("Doctor\'s name:", self.p_name)
        print("Specialties:", self.specialties)
