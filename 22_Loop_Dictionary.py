# Looping Dictionary

data_dict = {
    "dio" : "Dhiyaurrahman",
    "thq" : "Thariq",
    "ahd" : "Akhmad",
    "tgr" : "Tegar",
    "fiq" : "Faiq"
}

# Loop yang keluar key dan value nya
for i in data_dict:
    print(f"{i} : {data_dict[i]}")
    
# Operator untuk mengambil key
print("\nMengambil Key")
for i in data_dict.keys():
    print(i)

# Operator untuk mengambil value
print("\nMengambil Value")
for i in data_dict.values():
    print(i)
    
# Operator untuk mengambil items (key dan value)
print("\nMengambil Items")
for i, j in data_dict.items():
    print(f"{i} : {j}")