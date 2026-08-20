from src.models.person import Person

class Doctor(Person):
    def __init__(self,name, id_number, age, contact_info, specialization):
        super().__init__(name, id_number, age, contact_info)
        self.specialization = specialization
        self.available_slots = []