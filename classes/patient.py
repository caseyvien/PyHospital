from .person import Person

class Patient(Person):

    def __init__(self, p_name, sicknesses):
        Person.__init__(self,"Patient",p_name)
        self.sicknesses = sicknesses
        self.inpatient = False
        self.is_cured = False

    def display_patient(self):
        print("Patient name:", self.p_name)
        print("Type:", self.p_type)
        print("Sicknesses:", self.sicknesses)
        print("Is an in-patient", self.inpatient)
        print("Is cured?", self.is_cured)