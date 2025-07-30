# Copy Dictionary

data_dict = {
    "dio" : "Dhiyaurrahman",
    "thq" : "Thariq",
    "ahd" : "Akhmad",
    "tgr" : "Tegar",
    "fiq" : "Faiq"
}

data_dict_new = data_dict.copy()
print(data_dict_new)

data_dict_new["fiq"] = "Faiqs"
print(data_dict)
print(data_dict_new)

# Hapus data berdasarkan key
data_dict_new.pop("fiq")
print(data_dict)
print(data_dict_new)

# Hapus data terakhir
data_dict_new.popitem()
print(data_dict)
print(data_dict_new)