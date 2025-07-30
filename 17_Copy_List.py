# Copy List

# 1. Copy List - 1 Dimensi
data = ["Dio", "Hamizan", "Putra"]
data_new = data

print(hex(id(data)))
print(hex(id(data_new)))

# 2. Copy Nested List - List Bersarang
data_copy = data.copy()
print(hex(id(data)))
print(hex(id(data_copy)))

# 3. Copy List dengan deepcopy
from copy import deepcopy # bisa juga import copy, pemanggilannya copy.deepcopy(data_listnya)
data_deep = deepcopy(data)
print(hex(id(data)))
print(hex(id(data_copy)))

# Contoh nya
# 1. Copy Biasa, dimana ketika ada perubahahn (dalam kasus ini diedit), maka data asli akan berubah
data_new[2] = "Haya"
print(data)
print(data_new)

# 2. Copy Nested List, dimana ketika ada perubahan, makan tidak akan mengubah data asli dan hanya mengubah data copy nya
data_copy[2] = "Putra"
print(data)
print(data_copy)

# 3. Sama seperti poin 2
data_deep[2] = "Rahman"
print(data)
print(data_deep)