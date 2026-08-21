class Person:
    # Base class holding attributes shared by every kind of person in the system.
    # Doctor and Patient both inherit from this instead of repeating these fields.
    def __init__(self, name, id_number, age, contact_info):
        self.name = name
        self.id_number = id_number
        self.age = age
        self.contact_info = contact_info
