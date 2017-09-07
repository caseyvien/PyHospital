from .person import Person

class Patient(Person):

    def __init__(self, p_name, sicknesses):
        Person.__init__(self,"Patient",p_name)
        self.sicknesses = sicknesses
        self.inpatient = False
        self.is_cured = False
        self.is_queued = False
        self.room_assignment = []

    def display_patient(self):
        print("Patient name:", self.p_name)
        print("Type:", self.p_type)
        print("Sicknesses:", self.sicknesses)
        print("Is an in-patient", self.inpatient)
        print("Is cured?", self.is_cured)
        print("Is queued?", self.is_queued)

    def assign_room(self, room):
        #self.room_assignment.clear()
        self.leave_room(room)
        self.room_assignment.append(room)
        self.is_queued = True

    def leave_room(self, room):
        self.room_assignment.clear()
        self.is_queued = False