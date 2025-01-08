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












