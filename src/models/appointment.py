class Appointment:
    # Composition: links an ALREADY-EXISTING Doctor and Patient together.
    # Doesn't create new Doctor/Patient objects itself - it just holds references to real ones.
    def __init__(self, doctor_obj, patient_obj, date_time):
        self.date_time = date_time
        self.doctor = doctor_obj
        self.patient = patient_obj

