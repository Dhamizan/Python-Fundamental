# While Loop

'''
Dimulai dari:
1. While kondisi
2. aksi pertama
3. aksi seterusnya..
'''

# Contoh
print("Pertama:")
angka = 0
while angka < 5:
    print(angka)
    angka += 1

# Contoh ke dua
print("\nKedua:")
angka = 0
while True:
    if angka < 5:
        print(angka)
        angka += 1
    else:
        print("Selesai")
        break
    
# Continue, digunakan untuk melanjutkan program
print("\nKetiga:")
angka = 0
while True:
    print(angka)
    angka += 1
    if angka == 2:
        continue
    elif angka > 5:
        print("Selesai")
        break
    
# Pass, digunakan sebagai dummy, tidak akan melakukan apa-apa
print("\nKempat:")
angka = 0
while angka < 3:
    if angka == 1:
        pass 
    print(f"angka = {angka}")
    angka += 1

# Break, digunakan untuk menghentikan loop, contoh nya sama seperti yang kedua
print("\nKelima:")
angka = 0
while True:
    if angka < 5:
        print(angka)
        angka += 1
    else:
        print("Selesai")
        break
    
