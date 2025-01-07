class Data:
    def __init__(self):
        self.name = "april"
        self.age = 0

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Usia tidak boleh negatif")
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
