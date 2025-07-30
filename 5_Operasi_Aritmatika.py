# Operasi Aritmatika

# Prioritas = 
# 1. ()
# 2. eksponen/pangkat
# 3. perkalian, pembagian, eksponen/perpangkatan, modulus, floor div 
# 4. tambah, kurang

angka_a = 5
angka_b = 4

# Tambah
tambah = angka_a + angka_b
print("Hasil Tambah = ", tambah)

# Kurang
kurang = angka_a - angka_b
print("Hasil Kurang = ", kurang)

# Perkalian
perkalian = angka_a * angka_b
print("Hasil Perkalian = ", perkalian)

# Pembagian
pembagian = angka_a / angka_b
print("Hasil Pembagian = ", pembagian)

# Perpangkatan/Eksponen
perpangkatan = angka_a ** angka_b
print("Hasil Perpangkatan = ", perpangkatan)

# Modulus
modulus = angka_a % angka_b
print("Hasil Modulus = ", modulus)

# Floor Div
floor_div = angka_a // angka_b
print("Hasil Floor Div = ", floor_div)

# Contoh:
a = 2
b = 3
c = 4

hasil = b * a + (a + c) - a ** b # Hasilnya 4
print(hasil)