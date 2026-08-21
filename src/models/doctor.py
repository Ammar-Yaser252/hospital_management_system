from src.models.person import Person

class Doctor(Person):
    def __init__(self,name, id_number, age, contact_info, specialization):
        super().__init__(name, id_number, age, contact_info)                  # reuse Person's setup instead of repeating it
        self.specialization = specialization
        self.available_slots = []              # starts empty; filled in later via the GUI, not at creation
        self.doctor_appointments = []          # tracks every Appointment this doctor is part of

    def write_prescription_for(self, patient, note):
        # Doctor actively writes into the PATIENT's own record (not the doctor's).
        # Keeps prescriptions tied to whoever the patient actually is.
        patient.record.write_prescription(note)

    def delete_appointment(self, appointment):
        # Must remove from BOTH sides (doctor's and patient's lists), since booking
        # added the same Appointment object to both - otherwise they'd go out of sync.
        self.doctor_appointments.remove(appointment)
        appointment.patient.patient_appointments.remove(appointment)