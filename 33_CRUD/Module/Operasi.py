from .Random_ID import random_string
from . import Database

def tambah_data_ft():
    nama_barang = input("Nama Barang: ")
    harga_barang = int(input("Harga Barang: "))
    jumlah_barang = int(input("Jumlah Barang: "))
    
    data = Database.TEMPLATE.copy()
    
    data["id_barang"] = random_string(6)
    data["nama_barang"] = nama_barang
    data["harga_barang"] = harga_barang
    data["jumlah_barang"] = jumlah_barang
    
    data_str = f"{data['id_barang']}, {data['nama_barang']}, {data['harga_barang']}, {data['jumlah_barang']}\n"
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil ditambahkan")

def tambah_data():
    data = Database.TEMPLATE.copy()
    
    data["id_barang"] = random_string(6)
    data["nama_barang"] = input("Nama Barang: ")
    data["harga_barang"] = int(input("Harga Barang: "))
    data["jumlah_barang"] = int(input("Jumlah Barang: "))
    
    data_str = f"{data['id_barang']}, {data['nama_barang']}, {data['harga_barang']}, {data['jumlah_barang']}\n"
    print(f"Kamu Menambahkan data: {data_str}")
    
    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil ditambahkan")
    
def edit_data():
    data = Database.TEMPLATE.copy()
    
    data["id_barang"] = random_string(6)
    data["nama_barang"] = input("Nama Barang: ")
    data["harga_barang"] = int(input("Harga Barang: "))
    data["jumlah_barang"] = int(input("Jumlah Barang: "))
    
    data_str = f"{data['id_barang'], {data['nama_barang']}, {data['harga_barang']}, {data['jumlah_barang']}}"
    print(f"Kamu Mengedit data: {data_str}")
    panjang = len(data_str)
    
    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek()
            file.write(data_str)
    except:
        print("hoho")
    

def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            konten = file.readlines()
            return konten
    except:
        print("Tidak Bisa Membaca Database")
        with open(Database.DB_NAME, "w") as file:
            pass
        return []