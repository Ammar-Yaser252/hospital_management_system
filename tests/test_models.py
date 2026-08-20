from src.models.person import Person
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.medical_record import MedicalRecord

first_person = Person("Ali", "101", 45, "01150650812")  # person object
first_doctor = Doctor("John", "1001", 50, "011556600882", "Oncology") # doctor object
first_patient = Patient("Ahmed", "10001", 15, "012665588002", "A+") # patient object
first_record = MedicalRecord()


print (f"Name: {first_person.name}, ID: {first_person.id_number}, Age: {first_person.age}, Contact: {first_person.contact_info}")
print (f"Name: {first_doctor.name}, ID: {first_doctor.id_number}, Age: {first_doctor.age}, Contact: {first_doctor.contact_info}, Available slots: {first_doctor.available_slots}")
print (f"Name: {first_patient.name}, ID: {first_patient.id_number}, Age: {first_patient.age}, Contact: {first_patient.contact_info}, Blood type: {first_patient.blood_type}, Record: {first_patient.record}")

first_record.write_prescription("Take 2 paracetamol daily")
print (first_record.get_history())

first_record.write_prescription("Take 3 panadol daily")
print (first_record.get_history())
