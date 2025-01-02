class Process:
    def __init__(self, data):
        self.data = data

    def get_user_input(self):
        while True:
            try:
                name = input("Masukkan nama: ")
                age = int(input("Masukkan umur: "))
                if age < 0:
                    raise ValueError("Umur tidak boleh negatif.")
                self.data.add_entry(name, age)
                break
            except ValueError as e:
                print(f"Input tidak valid: {e}. Silahkan coba lagi.")
