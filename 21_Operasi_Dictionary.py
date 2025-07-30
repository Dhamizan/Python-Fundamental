# Operasi Dictionary

data_dict = {"nama": "Dio",
             "umur": 20,
             "kampus": "IPB"}

# Akses Dictionary
print(data_dict["nama"])

# Mengecek data
KEY = "nama"
CEKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di dalam dictionary: {CEKKEY}")

# Mengupdate data
data_dict["nama"] = "Hamizan"
print(data_dict["nama"])

data_dict.update({"hobby" : "Badmin"})
print(data_dict["nama"])

# Menghapus data
print(data_dict)
del data_dict["hobby"]
print(data_dict)