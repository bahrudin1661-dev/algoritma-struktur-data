# tugas mandiri penggunaan if, elif, else

print("=================kalkulator dasar=================")
print("pilih mode operasi :\nperjumlahan = 1\npengurangan = 2\nperkalian = 3\npembagian = 4")
mode_operasi = int(input("masukkan pilihan : "))
angka_pertama = float(input("masukkan angka pertama : "))
angka_kedua = float(input("masukkan angka kedua : "))

if mode_operasi == 1:
    jawaban = angka_pertama + angka_kedua
elif mode_operasi == 2:
    jawaban = angka_pertama - angka_kedua
elif mode_operasi == 3:
    jawaban = angka_pertama * angka_kedua
elif mode_operasi == 4:
    jawaban = angka_pertama / angka_kedua
else:
    print("pilihan tidak tersedia")

