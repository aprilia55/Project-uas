class View:
    def display_data(self, data):
        print("=================================")
        print("| Nama | Usia                  |")
        print("=================================")
        print(f"| {data.get_name():<4} | {data.get_age():<20} |")
        print("=================================")
