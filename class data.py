class Data:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, age):
        self.entries.append({"name": name, "age": age})

    def get_entries(self):
        return self.entries
