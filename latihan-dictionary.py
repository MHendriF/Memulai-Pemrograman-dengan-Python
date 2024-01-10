"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""


# TODO: Silakan buat kode Anda di bawah ini.
# Membuat variabel dictionary "data_diri"
data_diri = {
    "firstName": "Hendri",  # Ganti dengan nama depan Anda
    "lastName": "Febri",  # Ganti dengan nama belakang Anda
    "age": 25,  # Ganti dengan umur Anda
    "isMarried": False  # Ganti dengan status pernikahan Anda, True jika sudah menikah, False jika belum
}

# Menampilkan informasi dari dictionary "data_diri"
print("Data Diri:")
print("Nama:", data_diri["firstName"], data_diri["lastName"])
print("Umur:", data_diri["age"], "tahun")
print("Status Pernikahan:", "Menikah" if data_diri["isMarried"] else "Belum Menikah")
