# Looping List

# For Loop
print(f"For Loop angka:")
angka = [1,2,3,4,5]
for i in angka:
    print(f"Angka: {i}")

print(f"\nFor Loop mahasiswa:")
mahasiswa = ["Dio", "Hamizan", "Putra"]
for i in mahasiswa:
    print(f"Nama: {i}")
    
# For Loop dengan Range
print(f"\nFor Loop angka range:")
angka_r = [4,7,5,2,3]
panjang = len(angka_r)
for i in range (panjang):
    print(f"Angka: {angka_r[i]}")

print(f"\nFor Loop angka range v2:") 
for i in range(len(angka_r)):
    print(f"Angka: {angka_r[i]}")
    
# While Loop
print(f"\nFor Loop angka while:")
angka_w = [1,3,5,7,9]
panjang_w = len(angka_w)
poin = 0
while poin < panjang:
    print(f"Angka: {angka_w[poin]}")
    poin += 1

# List Comprehension
print(f"\nFor Loop list comprehension:")
angka_lc = [1,2,3,4,5]
[print(f"Data Angka: {i}") for i in angka_lc]

print(f"\nFor Loop list comprehension v2:")
kali_2 = [i*2 for i in angka_lc]
print(f"Data Angka: {kali_2}")

# Enumerate, digunakan untuk melakukan looping sambil mendapatkan index dan nilai secara bersamaan dari sebuah list
print(f"\nFor Loop enumerate:")
angka_e = ["Dio", "Hamizan", "Putra"]
for i, j in enumerate(angka_e):
    print(f"Index: {i}, Nama: {j}")