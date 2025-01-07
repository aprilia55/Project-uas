class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def input_data(self):
        name = input("nama: ")
        self.data.set_name(name)

        while True:
            try:
                age = int(input("20: "))
                self.data.set_age(age)
                break  # keluar dari loop jika usia valid
            except ValueError:
                print("Input tidak valid! Harap masukkan angka untuk usia.")
            except Exception as e:
                print(e)

    def display_data(self):
        self.view.display_data(self.data)
