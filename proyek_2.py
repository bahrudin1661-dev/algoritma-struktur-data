# tugas mandiri penggunaan if, elif, else

print("=================kalkulator dasar=================")
print("pilih mode operasi :\n1 = perjumlahan\n2 = pengurangan\n3 = perkalian\n4 = pembagian")
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
    
print("jawaban operasi adalah : ", jawaban)