from src.models.person import Person
from src.models.medical_record import MedicalRecord
from src.models.appointment import Appointment

class Patient(Person):
    def __init__(self, name, id_number, age, contact_info, blood_type):
        super().__init__(name, id_number, age, contact_info)
        self.blood_type = blood_type
        self.record = MedicalRecord()      # every patient automatically gets their own record (composition)
        self.patient_appointments = []     # tracks every Appointment this patient has booked


    def book_appointment(self, doctor, date_time):
        # Creates one real Appointment object and links it on BOTH sides (patient + doctor),
        # so either side can see the same booking - not two separate copies.
        appointment = Appointment(doctor, self, date_time)
        self.patient_appointments.append(appointment)
        doctor.doctor_appointments.append(appointment)
        return appointment  # handed back so the caller (e.g. GUI) can use it immediately
    