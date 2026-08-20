from src.models.person import Person
from src.models.medical_record import MedicalRecord

class Patient(Person):
    def __init__(self, name, id_number, age, contact_info, blood_type):
        super().__init__(name, id_number, age, contact_info)
        self.blood_type = blood_type
        self.record = MedicalRecord()
