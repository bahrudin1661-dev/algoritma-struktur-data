# disini adalah proyek pertama dari mata kuliah algoritma dan struktur data
# saya bahrudin lisa akan membuat program simple menggunakan bahasa pemograman yaitu python

# ALGORITMA = kasir_toko_sederhana
# DEKLARASI
nama_barang = str(input("masukkan nama barang : "))
harga_satuan = float(input("masukkan harga satuan : "))
jumlah_beli = int(input("masukkan jumlah beli : "))
total_bayar = (float(harga_satuan * jumlah_beli))

# ALUR LOGIKA
print("===========================================")
print("============Traksaksi berhasil=============")
print("===========================================")
print(f"barang yang ada pilih : {nama_barang}")
print(f"harga satuan barang tersebut : {harga_satuan:,.2f}")
print(f"jumlah seluruh barang yang ada : {jumlah_beli}")
print("==========================================================")
print(f"total biaya yang harus dikeluarkan: {total_bayar:,.2f}")
print("konfirmasi apakah pesanan anda sudah sesuai dengan")
print("==========================================================")
