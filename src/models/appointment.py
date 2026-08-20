class Appointment:
    def __init__(self, doctor_obj, patient_obj, date_time):
        self.date_time = date_time
        self.doctor = doctor_obj
        self.patient = patient_obj

