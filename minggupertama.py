print("===pencatatan zakat fitrah====")
nama_donatur = str(input("masukkan nama : "))
jumlah_jiwa = int(input("masukkan jumlah anggota yang di tanggung : "))
harga_beras_per_kg = float(input("masukkam harga beras per-kg : "))
total_berat_beras = jumlah_jiwa * 2.5
total_biaya = total_berat_beras * harga_beras_per_kg
print("Nama Donatur     : ", nama_donatur)
print("Jumlah Tanggungan: ", jumlah_jiwa, " jiwa")
print("Kewajiban Beras  : ", total_berat_beras, " kg")
print("Estimasi Nilai Uang : Rp", total_biaya)

# =============analisis model IPO (masukkan, proses, keluaran)=============

# =====Input======
# nama_donatur = "tipe data string"
# jumlah_jiwa = "tipe data integer"
# harga_beras_per_kg = "float"

# =====Proses======
# total_berat_beras = jumlah_jiwa * 2.5
# total_biaya = harga_beras_per_kg * jumlah_jiwa

# =====Output=====
# Menampilkan nama donatur
# Menampilkan total beras zakat fitrah yang harus diserahkan
# Menampilkan total biaya

#===============Penyusunan Pseudocode (Logika Pemrograman Sederhana)===============

# Algoritma mencatat_penerimaan_zakat_dari_warga

# Deklarasi:

# nama_donatur = string
# jumlah_jiwa = integer
# harga_beras_per_kg = float
# total_berat_beras = float
# total_biaya = float

# ALUR LOGIKA:
# // 1. Tahap Input Data
#    BACA nama_donatur
#    BACA jumlah_jiwa
#    BACA harga_beras_per_kg
#
# // 2. Tahap Pemrosesan Data
#    HITUNG total_berat_beras = jumlah_jiwa * 2.5
#    HITUNG total_biaya = harga_beras_per_kg * total_berat_beras

# // 3. Tahap Output Informasi
#    Tampilkan("Nama Donatur     : ", nama_donatur)
#    Tampilkan("Jumlah Tanggungan: ", jumlah_jiwa, " jiwa")
#    Tampilkan("Kewajiban Beras  : ", total_berat_beras, " kg")
#    Tampilkan("Estimasi Nilai Uang : Rp", total_biaya)
