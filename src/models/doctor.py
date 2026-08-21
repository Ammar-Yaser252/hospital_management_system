from src.models.person import Person

class Doctor(Person):
    def __init__(self,name, id_number, age, contact_info, specialization):
        super().__init__(name, id_number, age, contact_info)
        self.specialization = specialization
        self.available_slots = []
        self.doctor_appointments = []

    def write_prescription_for(self, patient, note):
        patient.record.write_prescription(note)

    def delete_appointment(self, appointment):
        self.doctor_appointments.remove(appointment)
        appointment.patient.patient_appointments.remove(appointment)