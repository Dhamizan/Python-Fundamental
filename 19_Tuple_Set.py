# Data Tuple dan Set

# 1. Data Tuple
# Bersifat Immutable (tidak bisa diubah), beda dengan list yang mutable (bisa diubah)
data_tuple = ("Dio", "Hamizan", "Putra")
print(data_tuple)

# Operasi Data Tuple
# Akses Nilai
print(data_tuple[0])

# Hitung Panjang
print(len(data_tuple))

# Cek nilai
print("Dio" in data_tuple)

# Menggabungkan data
data_tuple_baru = data_tuple + ("Ahmad", "Dio") # Kalau cuma satu data, barengi dengan "," di akhir "("Ahmad",)"
print(data_tuple_baru)

# Mengulang tuple
print(data_tuple * 2)

# Hitung jumlah elemen tertentu
hitung_dio = data_tuple_baru.count("Dio")
print(hitung_dio)

# 2. Data Set
# Data set tidak memilki index, tapi dia mutable, dan bersifat unik.
data_set = {"Dio", "Hamizan", "Putra"}
print(data_set)

# Operasi di set
# Tambah Data
data_set.add("Haya")
print(data_set)

# Gabung dua elemen - union
angka_1  = {1,2,3}
angka_2 = {3,4,5}
print(angka_1.union(angka_2))
print(angka_1 | angka_2)

# Irisan dua elemen - intersection
angka_1  = {1,2,3}
angka_2 = {3,4,5}
print(angka_1.intersection(angka_2))
print(angka_1 & angka_2)

# Selisih dua elemen - difference
angka_1  = {1,2,3}
angka_2 = {3,4,5}
print(angka_1.difference(angka_2))
print(angka_1 - angka_2)

# Gabungan tanpa yang sama dua elemen - symmetric difference
angka_1  = {1,2,3}
angka_2 = {3,4,5}
print(angka_1.symmetric_difference(angka_2))
print(angka_1 ^ angka_2)

# Hapus Elemen
# Remove, akan error kalau data tidak ada
data_set.remove("Haya")
print(data_set)

# Discard, tidak akan error kalau data tidak ada
data_set.discard("Haya")
print(data_set)

# Clear, untuk hapus semua data set
data_set.clear()