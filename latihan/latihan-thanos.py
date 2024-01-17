# TODO: Silakan buat kode Anda di bawah ini.
# Dihari pertama hanya ada 1 penduduk
# Di hari-hari berikutknya Dr Strange muncul dan menggandakan penduduknya menjadi 3x lipat
# Namun dihari kelipatan 3, Thanos muncul dan menghilangkan 1/2 penduduk(pembulatan ke bawah)
# Disaat thanos muncul, Dr Strange tidak berani muncul

def simulasi_penduduk(hari):
    for i in range(1, hari + 1):
        # Hari pertama hanya ada 1 penduduk
        if i == 1:
            jumlah_penduduk = 1

        # Dr Strange menggandakan penduduk menjadi 3x lipat
        elif i % 3 != 0:
            jumlah_penduduk *= 3

        # Thanos muncul di hari kelipatan 3, menghilangkan 1/2 penduduk (pembulatan ke bawah)
        elif i % 3 == 0:
            jumlah_penduduk = jumlah_penduduk // 2
        print(f"Hari ke-{i}: Jumlah penduduk = {jumlah_penduduk}")
    return jumlah_penduduk

# Uji simulasi untuk 10 hari
hari_ke = 50
total_penduduk = simulasi_penduduk(hari_ke)
print(f"\nJumlah penduduk setelah {hari_ke} hari: {total_penduduk}")