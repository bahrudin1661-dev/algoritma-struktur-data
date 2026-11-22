# tugas ke satu
tunggakan = 300000
pembayaran_per_bulan = 100000
bulan = 1

while tunggakan > 0:
    print(f"bulan ke-{bulan}, pembayaran sebesar {pembayaran_per_bulan}")
    bulan += 1
    tunggakan -= pembayaran_per_bulan

# tugas ke ketiga
urutan_buku = 0
jumlah_buku = int(input("masukkan jumlah buku : "))
total_denda = 0
for i in range(jumlah_buku):
    urutan_buku += 1
    hari_terlambat = int(input(f"buku ke-{urutan_buku}, masukkan berapa hari terlambat : "))
    if hari_terlambat == 0:
        continue
    denda = float(hari_terlambat * 1000)
    total_denda += denda
print(f"{total_denda:,.2f}")