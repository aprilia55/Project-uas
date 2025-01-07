# Class untuk menyimpan data
class Data:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, name):
        self.records = [record for record in self.records if record['Nama'] != name]

    def get_average_score(self):
        if not self.records:
            return 0
        total_score = sum(record['Nilai Ujian'] for record in self.records)
        return total_score / len(self.records)

    def find_record(self, name):
        return [record for record in self.records if record['Nama'].lower() == name.lower()]

# Class untuk memproses data
class Process:
    def __init__(self, data):
        self.data = data

    def validate_input(self, name, age, score):
        if not name:
            raise ValueError("Nama tidak boleh kosong.")
        if not age.isdigit() or int(age) <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        if not score.isdigit() or int(score) < 0 or int(score) > 100:
            raise ValueError("Nilai ujian harus berupa angka antara 0 dan 100.")

    def add_user(self, name, age, score):
        self.validate_input(name, age, score)
        self.data.add_record({"Nama": name, "Usia": int(age), "Nilai Ujian": int(score)})

# Class untuk menampilkan data
class View:
    def __init__(self, data):
        self.data = data

    def display(self):
        if not self.data.records:
            print("Tidak ada data untuk ditampilkan.")
            return
        
        # Menampilkan header tabel
        print(f"{'Nama':<20} {'Usia':<5} {'Nilai Ujian':<12}")
        print("=" * 45)
        
        # Menampilkan setiap record dalam tabel
        for record in self.data.records:
            print(f"{record['Nama']:<20} {record['Usia']:<5} {record['Nilai Ujian']:<12}")

    def display_average_score(self):
        avg_score = self.data.get_average_score()
        print(f"Rata-rata Nilai Ujian: {avg_score:.2f}")

# Fungsi utama untuk menjalankan program
def main():
    data = Data()
    process = Process(data)
    view = View(data)

    while True:
        print("\nMenu:")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Tampilkan Rata-rata Nilai Ujian")
        print("4. Cari Data Siswa")
        print("5. Hapus Data Siswa")
        print("6. Keluar")

        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            try:
                name = input("Masukkan nama: ")
                age = input("Masukkan usia: ")
                score = input("Masukkan nilai ujian (0-100): ")
                process.add_user(name, age, score)
                print("Data berhasil ditambahkan!")
            except ValueError as e:
                print(f"Kesalahan: {e}")

        elif choice == '2':
            view.display()

        elif choice == '3':
            view.display_average_score()

        elif choice == '4':
            name = input("Masukkan nama yang dicari: ")
            records = data.find_record(name)
            if records:
                for record in records:
                    print(f"Nama: {record['Nama']}, Usia: {record['Usia']}, Nilai Ujian: {record['Nilai Ujian']}")
            else:
                print("Data tidak ditemukan.")

        elif choice == '5':
            name = input("Masukkan nama yang ingin dihapus: ")
            data.remove_record(name)
            print(f"Data siswa dengan nama '{name}' telah dihapus.")

        elif choice == '6':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
