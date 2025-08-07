import Package.Database as db
import random
import string

def random_id(a:int) -> str:
    id_barang = ''.join(random.choice(string.ascii_letters) for i in range(a))
    return id_barang

def read():
    try:
        with open(db.DB_NAME, 'r', encoding='utf-8') as file:
            return file.readlines()
    except:
        []

def lihat_data():
    data = read()
    
    print(45*'=')
    print(f"{'ID Barang':7} | {'Nama Barang':20} | {'Harga Barang':10} | {'Stok Barang':4}")
    print(45*'=')
    
    for i, d in enumerate(data):
        data_space = d.strip().split(',')
        id_barang = data_space[0]
        nama_barang = data_space[1]
        harga_barang = data_space[2]
        stok_barang = data_space[3]
        
        print(f"{id_barang:7} | {nama_barang:20} | {harga_barang:10} | {stok_barang:4}")
        
def tambah_data_awal():
    data = db.TEMPLATE.copy()
    data['id_barang'] = random_id(6)
    data['nama_barang'] = input('Masukkan Nama Barang: ')
    data['harga_barang'] = input('Masukkan Harga Barang: ')
    data['stok_barang'] = input('Masukkan Stok Barang: ')
    
    data_str = f"{data['id_barang']},{data['nama_barang']},{data['harga_barang']},{data['stok_barang']}\n"
    
    try:
        with open(db.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
            print(f"Berhasil Menambahkan Data! -> {data_str}")
    except Exception as e:
        print(f'Gagal Menambahkan Data! -> {e}')
        
def tambah_data():
    data = db.TEMPLATE.copy()
    data['id_barang'] = random_id(6)
    data['nama_barang'] = input('Masukkan Nama Barang: ')
    data['harga_barang'] = input('Masukkan Harga Barang: ')
    data['stok_barang'] = input('Masukkan Stok Barang: ')
    
    data_str = f"{data['id_barang']},{data['nama_barang']},{data['harga_barang']},{data['stok_barang']}\n"
    
    try:
        with open(db.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
            print(f"Berhasil Menambahkan Data! -> {data_str}")
    except Exception as e:
        print(f'Gagal Menambahkan Data! -> {e}')
        
def sunting_data():
    cari_id = input("Cari ID Barang yang ingin diubah: ")
    found = False
    
    try:
        with open(db.DB_NAME, 'r+', encoding='utf-8') as file:
            filec = file.readlines()
            file.seek(0)
            file.truncate()
            
            for i in range(len(filec)):
                data = filec[i].strip().split(',')
                
                if data[0] == cari_id:
                    nama_barang = input('Masukkan Nama Barang Baru: ')
                    harga_barang = input('Masukkan Harga Barang Baru: ')
                    stok_barang = input('Masukkan Stok Barang Baru: ')
                    
                    data_str = f"{cari_id},{nama_barang},{harga_barang},{stok_barang}"
                    filec[i] = data_str
                    found = True
        
            file.writelines(filec)
            print(f"Berhasil Menambahkan Data! -> {data_str}")
        
        if not found:
            print(f"Data {cari_id} tidak ditemukan")
                
    except Exception as e:
        print(f"Gagal merubah data! -> {e}")

def hapus_data():
    cari_id = input("Cari ID Barang yang ingin dihapus: ")
    found = False
    
    try:
        with open(db.DB_NAME, 'r+', encoding='utf-8') as file:
            filec = file.readlines()
            file.seek(0)
            file.truncate()
            
            for i in range(len(filec)):
                data = filec[i].strip().split(',')
                if data[0] == cari_id:
                    found = True
                else:
                    file.write(filec[i])
        
            if found:
                print(f"Data {cari_id} berhasil dihapus!")
            else:
                print(f"Data {cari_id} tidak ditemukan")
    
    except Exception as e:
        print(f"Gagal Menghapus Data! {str(e)}")