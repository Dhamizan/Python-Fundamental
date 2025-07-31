# Write File Eksternal

# 1. Write (w)
with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Dio")
    
with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Thariq")

# Itu Bakal Ketimpa

# 2. Append (a), buat nambah data tanpa ketimpa
with open("data_1.txt", "a", encoding="utf-8") as file:
    file.write("\nDio")
    
with open("data_1.txt", "a", encoding="utf-8") as file:
    file.write("\nTegar")
    
with open("data_2.txt", "w", encoding="utf-8") as file:
    file.write("Akhmad")
    
# 3. Read dan Write (r+), file harus udah ada, dan dia akan nimpa juga
with open("data_2.txt", "r+", encoding="utf-8") as file:
    file.write("Zufar")
    #file.write("Rafif")
    #file.write("Putra")