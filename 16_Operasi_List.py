# Operasi List

data = ["Dio", "Hamizan", "Putra"]

# Mengambil Data Berdasarkan Index
print(data[0])

# Index, Mengambil Data Berdasarkan Isi untuk mengetahui berada di Index mana
print(data.index("Hamizan"))

# Menambah Data
data.append("Akhmad") # Menambahkan Data di Akhir
print(data)
data.insert(0, "Thariq") # Menambahkan Data Sesuai di Index yang Ditentukan
print(data)

# Mengubah Data
data[2] = "Tegar"
print(data)

# Menghapus Data
data.remove("Putra") # Menghapus Data Berdasarkan Index yang Dipilih
print(data)
data.pop() # Menghapus Data di Index yang Terakhir
print(data) 

# Jumlah Data Dalam List
jumlah_data = len(data)
print(jumlah_data)

# Count, digunakan untuk menghitung jumlah suatu data
data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
jumlah_2 = data.count(2)
print(jumlah_2)

# Mengurutkan List
data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
data.sort()
print(data)

data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
urutan_sort = sorted(data) # Sorted, digunakan untuk mengurutkan tanpa merusak data asli
print(data)
print(urutan_sort)

# Mengurutkan List (Kebalikan)
data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
data.sort()
data.reverse()
print(data)

data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
data.sort()
data.sort(reverse=True)
print(data)

data = [1,2,3,2,1,4,5,3,2,4,5,2,1,3,5]
data.sort()
kebalikan = list(reversed(data))
print(kebalikan)