from src.models.person import Person
from src.models.doctor import Doctor

first_person = Person("Ali", "101", 45, "01150650812")  # person object
first_doctor = Doctor("John", "1001", 50, "011556600882", "Oncology") # doctor object

print (f"Name: {first_person.name}, ID: {first_person.id_number}, Age: {first_person.age}, Contact: {first_person.contact_info}")
print (f"Name: {first_doctor.name}, ID: {first_doctor.id_number}, Age: {first_doctor.age}, Contact: {first_doctor.contact_info}, Available slots: {first_doctor.available_slots}")
