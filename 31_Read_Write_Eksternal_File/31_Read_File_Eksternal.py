# Read File Eksternal

print(f"{"="*3} File Nama Orang {"="*3}")
file = open("data.txt", mode="r")

# Tampilkan Semua
# print(file.read())

print(f"Statur Read (r) : {file.readable()}")
print(f"Statur Writable (w) : {file.writable()}")

# Tampilkan Perbaris
# print(file.readline(), end="") #1
# print(file.readline(), end="") #2

# Tampilkan Semua dengan List
print(file.readlines())

# Close File
print(f"Apakah file sudah ditutup? : {file.closed}")
file.close()
print(f"Apakah file sudah ditutup? : {file.closed}")

# Membuka file dengan with
print("\n",3*"=", " Membaca file txt dengan with", 3*"=")
with open("data.txt", mode="r") as file:
    a = file.readline()
    print(a, end="")
    print(f"Apakah file sudah ditutup? : {file.closed}")

print(f"Apakah file sudah ditutup? : {file.closed}")