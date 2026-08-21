from src.models.person import Person
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.medical_record import MedicalRecord
from src.models.appointment import Appointment

first_person = Person("Ali", "101", 45, "01150650812")  # person object
first_doctor = Doctor("John", "1001", 50, "011556600882", "Oncology") # doctor object
first_patient = Patient("Ahmed", "10001", 15, "012665588002", "A+") # patient object
first_record = MedicalRecord() 
booking = Appointment(first_doctor, first_patient, "2026-10-10  11:00 AM")


print (f"Name: {first_person.name}, ID: {first_person.id_number}, Age: {first_person.age}, Contact: {first_person.contact_info}")
print (f"Name: {first_doctor.name}, ID: {first_doctor.id_number}, Age: {first_doctor.age}, Contact: {first_doctor.contact_info}, Available slots: {first_doctor.available_slots}")
print (f"Name: {first_patient.name}, ID: {first_patient.id_number}, Age: {first_patient.age}, Contact: {first_patient.contact_info}, Blood type: {first_patient.blood_type}, Record: {first_patient.record}")

first_record.write_prescription("Take 2 paracetamol daily")
print (first_record.get_history())

first_record.write_prescription("Take 3 panadol daily")
print (first_record.get_history())


first_patient.record.write_prescription("Take 1 brufen when needed")
print (first_patient.record.get_history())

print(f"Doctor: {booking.doctor.name}, Patient: {booking.patient.name}, Date: {booking.date_time}")

first_doctor.write_prescription_for(first_patient, "Rest for 3 days")
print(first_patient.record.get_history())

print("________________________________________________________________________________________________")
second_appointment = first_patient.book_appointment(first_doctor, "2026-11-05 2:00 PM")

print(first_patient.patient_appointments)
print(first_doctor.doctor_appointments)
print(second_appointment.doctor.name, second_appointment.date_time)

first_doctor.delete_appointment(second_appointment)

print(first_patient.patient_appointments)
print(first_doctor.doctor_appointments)



first_doctor.add_slot("Monday 9:00 AM")
first_doctor.add_slot("Monday 10:00 AM")
print(first_doctor.available_slots)