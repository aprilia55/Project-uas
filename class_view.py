class View:
    def display_table(self, data):
        print(f"{'Name':<20}{'Age':<5}")
        print("-" * 25)
        for entry in data:
            print(f"{entry['name']:<20}{entry['age']:<5}")
