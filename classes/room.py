class Room:

    def __init__(self, r_type: object, r_location: object) -> object:
        self.r_type = r_type
        self.r_location = r_location
        self.is_occupied = False
        self.has_doctor = False

    def display_room(self):
        print("Room Type:", self.r_type)
        print("Room Location:", self.r_location)
        print("Is room occupied:", self.is_occupied)
        print("Has doctor:", self.has_doctor)