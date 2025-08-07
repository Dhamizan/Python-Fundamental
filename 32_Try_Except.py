# Try dan Except, untuk menghindari error

input_angka = int(input("Masukkan Angka: "))

try:
    hasil = 10/input_angka
    print(hasil)
except:
    print("Maaf, Anda tidak bisa membagi dengan angka 0")
    
