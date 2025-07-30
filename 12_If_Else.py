# If Else Statement

'''
Dimulai dari
1. If
2. Kondisi
3. Aksinya
'''

# Contoh
angka = int(input("Masukkan Angka: "))
if angka < 10:
    print("Angka Satuan")
else:
    print("Angka Puluhan")
    
# Elif
angka = int(input("Masukkan Angka: "))
if angka < 10:
    print("Angka Satuan")
elif angka < 10:
    print("Angka Puluhan")
elif angka < 100:
    print("Angka Ratusan")
else:
    print("Angka Lebih Dari Ratusan")
    
# Percabangan
# Kita Akan Membuat Kalkulator Sederhana

print(25*"-")
print("KALKULATOR SEDERHANA")
print(25*"-")

angka1 = int(input("Masukkan Angka Pertama: "))
angka2 = int(input("Masukkan Angka Kedua: "))
print('''
1. Tambah
2. Kurang
3. Kali
4. Bagi
''')
operasi = int(input("Pilih Operasi: "))

if operasi == 1:
    print(angka1 + angka2)
elif operasi == 2:
    print(angka1 - angka2)
elif operasi == 3:
    print(angka1 * angka2)
elif operasi == 4:
    print(angka1 / angka2)
else:
    print("Operasi Tidak Tersedia")