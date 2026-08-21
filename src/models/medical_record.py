class MedicalRecord:
    def __init__(self):
        self.__history = []    # Private: only accessible through the methods below, not directly from outside the class


    def write_prescription(self, note):
        # The only approved way to add a note to the private history.
        # Keeps changes controlled instead of letting outside code edit the list directly.
        self.__history.append(note)

    def get_history(self):
         # The only approved way to read the private history from outside the class.
        # Note: returns the actual list, not a copy - callers shouldn't modify it directly.
        return self.__history