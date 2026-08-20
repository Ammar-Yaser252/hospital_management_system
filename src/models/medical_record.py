class MedicalRecord:
    def __init__(self):
        self.__history = []

    def write_prescription(self, note):
        self.__history.append(note)

    def get_history(self):
        return self.__history