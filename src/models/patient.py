from src.models.person import Person
from src.models.medical_record import MedicalRecord

from src.models.appointment import Appointment



class Patient(Person):
    def __init__(self, name, id_number, age, contact_info, blood_type):
        super().__init__(name, id_number, age, contact_info)
        self.blood_type = blood_type
        self.record = MedicalRecord()
        self.patient_appointments = []

#__________________________________________________________________________
    def book_appointment(self, doctor, date_time):
        appointment = Appointment(doctor, self, date_time)
        self.patient_appointments.append(appointment)
        doctor.doctor_appointments.append(appointment)
        return appointment
    