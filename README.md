# Project UAS

Nama : Alfarizki Aprilia Putri

NIM : 312410455

Kelas : TI.24.A5

Mata Kuliah : BAHASA PEMROGRAMAN

# Daftar Link Youtube
- [video Tutorial](https://youtu.be/zARyDQw_x0Y?si=CVD6HMswQq7wjxHE)

##  Kelas Data
Kelas Data adalah sebuah cetak biru (blueprint) untuk membuat objek yang memiliki atribut name dan age, serta metode untuk mengakses dan memodifikasi atribut tersebut.
##  1. Konstruktor ```(__init__)```

```python
def __init__(self):
    self.name = "april"
    self.age = 0
```
* Konstruktor adalah metode khusus yang akan dipanggil secara otomatis saat objek
  
* dari kelas ```Data``` dibuat.
  
* Atribut ```self.name``` diinisialisasi dengan nilai default ```"april"```.
  
* Atribut `self.age` diinisialisasi dengan nilai default `0`.
  
## 2. Metode `set_name`
```python
def set_name(self, name):
    self.name = name
```
* Metode ini digunakan untuk mengubah nilai atribut name.
* Parameter name adalah nilai baru yang akan diberikan ke atribut self.name.

## 3. Metode set_age
```python
def set_age(self, age):
    if age < 0:
        raise ValueError("Usia tidak boleh negatif")
    self.age = age
```
* Metode ini digunakan untuk mengubah nilai atribut age.
* Sebelum mengubah nilai, metode ini memeriksa apakah nilai age lebih kecil dari 0.
* Jika ya, akan memunculkan error (ValueError) dengan pesan "Usia tidak boleh 
  negatif".
* Jika nilai valid (>= 0), atribut self.age diubah menjadi nilai baru tersebut.
  
## 4.Metode get_name
```python
def get_name(self):
    return self.name
```
* Metode ini digunakan untuk mengambil atau mengembalikan nilai atribut name.
  
## 5. Metode get_age
```python
def get_age(self):
    return self.age
```
* Metode ini digunakan untuk mengambil atau mengembalikan nilai atribut age.
* Namun, pada kode saya, ada kesalahan kecil: ada tambahan to pada akhir baris. 
  Seharusnya:
 ```python
return self.age
```
Fungsi Kode Ini
Kode ini dapat digunakan sebagai dasar untuk merepresentasikan entitas data sederhana dengan dua atribut: name dan age. Hal ini cocok untuk menyimpan data pengguna atau informasi entitas lainnya yang membutuhkan validasi sederhana.

## Penjelasan Kode: Kelas View
Kelas View bertanggung jawab untuk menampilkan data dengan format tabel sederhana ke konsol. Kelas ini hanya memiliki satu metode, yaitu display_data.

1. Metode display_data
   
```python
def display_data(self, data):
    print("=================================")
    print("| Nama | Usia                  |")
    print("=================================")
    print(f"| {data.get_name():<4} | {data.get_age():<20} |")
    print("=================================")
```
* Parameter :

* data: Objek yang diberikan sebagai argumen harus memiliki metode get_name() dan get_age(). Dalam konteks ini, objek dari kelas Data dapat digunakan.
  
* Fungsi Metode:

* Menampilkan data atribut name dan age dari objek data ke konsol dalam format 
  tabel yang terstruktur.
  
* Langkah-langkah:

1. Baris Header: Menampilkan garis horizontal = untuk memisahkan bagian atas tabel.
2. Header Kolom: Baris dengan label kolom Nama dan Usia.
3. Isi Data: Mengambil nilai name dan age menggunakan metode get_name() dan 
   get_age() dari objek data, kemudian menampilkan dalam format tabel.
   
   {data.get_name():<4}: Memformat nama agar rata kiri dengan lebar minimum 4 
   karakter.

   {data.get_age():<20}: Memformat usia agar rata kiri dengan lebar minimum 20 
   karakter.

4. Baris Penutup: Menampilkan garis horizontal untuk menutup tabel.
   
* Manfaat Kode
Kelas View memisahkan logika presentasi (tampilan) dari logika bisnis 
(pengelolaan data). Hal ini membuat kode lebih modular dan lebih mudah 
dipelihara, karena tugas untuk memformat dan menampilkan data dikelola secara 
terpisah dari pengelolaan data itu sendiri.


## Kelas `Process`
Kelas Process bertanggung jawab untuk:

1. Mengelola proses pengambilan input data dari pengguna.
2. Menghubungkan data (kelas Data) dan tampilan (kelas View).
3. Mengorganisir alur kerja secara terstruktur.
   
## 1. Konstruktor `(__init__)`
```phython
def __init__(self):
    self.data = Data()
    self.view = View()
def __init__(self):
    self.data = Data()
    self.view = View()
```
### Apa yang dilakukan?

* Konstruktor adalah metode khusus yang otomatis dipanggil saat objek dari kelas Process dibuat.
* Dua atribut dideklarasikan:
    * self.data: Membuat instance dari kelas Data untuk menyimpan data.
    * self.view: Membuat instance dari kelas View untuk menampilkan data.
### Kenapa penting?

* Konstruktor ini menginisialisasi dua objek, data dan view, yang akan digunakan dalam metode lainnya untuk menjalankan tugas pengelolaan data dan tampilan.

## 2. Metode input_data
```phython
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
```
Fungsi Metode
Metode ini bertugas untuk mengambil input dari pengguna dan menyimpannya ke dalam objek data.

Detail Per Bagian

1. Input Nama
   
```python
name = input("nama: ")
self.data.set_name(name)
```
* Apa yang dilakukan?
* Meminta pengguna memasukkan nama melalui keyboard.
* Nama tersebut disimpan ke atribut name di dalam objek data menggunakan metode * 
  set_name().

2. Input Usia dengan Validasi
```python
while True:
    try:
        age = int(input("20: "))
        self.data.set_age(age)
        break
    except ValueError:
        print("Input tidak valid! Harap masukkan angka untuk usia.")
    except Exception as e:
        print(e)
```
1. Apa yang dilakukan?
* Meminta pengguna memasukkan usia melalui keyboard dalam bentuk angka.
  
* Validasi:
  
* int(input("20: ")): Mengonversi input menjadi bilangan bulat.
* Jika konversi berhasil dan usia valid, usia tersebut disimpan di atribut age 
  dalam objek data menggunakan metode set_age().
* Jika konversi gagal (input bukan angka), ValueError akan ditangkap, dan pesan 
  error ditampilkan.
* Looping:
* Menggunakan while True agar proses pengambilan input terus berulang sampai 
  pengguna memberikan input yang valid.
  break: Keluar dari loop jika usia berhasil diatur tanpa error.








