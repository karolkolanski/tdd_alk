class Customer:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self._age
    def is_adult(self):
        pass
