from . import Database
import random
import string

def random_string(p:int) -> str:
    hasil = ''
    for i in range(p):
        hasil.join(random.choice(string.ascii_letters))
        
    return hasil

# def random_string(p:int) -> str:
#     hasil = ''
#     for i in range(p):
#         hasil += random.choice(string.ascii_letters)
#     return hasil

# def random_string(panjang:int) -> str:
#     hasil = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
#     return hasil

def read():
    try:
        with open(Database.DB_NAME, 'r', encoding='utf-8') as file:
            return file.readlines()
    except:
        return []
    
def lihat_data():
    data_file = read()
    
    print(f"\n{"="*100}")
    print(f"{'NIM':8} | {'Nama':20} | {'Alamat':10} | {'Email':30} | {'No. Telp':12}")
    print(f"\n{"="*100}")
    
    for i, data in enumerate(data_file):
        data_space = data.split(',')
        data_nim= data_space[0]
        data_nama = data_space[1]
        data_alamat = data_space[2]
        data_email = data_space[3]
        data_notelp = data_space[4]
        
        print(f"{data_nim:8} | {data_nama:20} | {data_alamat:10} | {data_email:30} | {data_notelp:12}")

def tambah_data_ft():
    data = Database.TEMPLATE.copy()
    data['nim'] = random_string(6)
    data['nama'] = input('Masukkan nama: ')
    data['alamat'] = input('Masukkan alamat: ')
    data['email'] = input('Masukkan email: ')
    data['no_hp'] = input('Masukkan no hp: ')
    
    data_str = f"{data['nim']},{data['nama']},{data['alamat']},{data['email']},{data['no_hp']}\n"
    print(f"Anda menambahkan data: {data_str}")
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data")
        
def tambah_data():
    data = Database.TEMPLATE.copy()
    
    data['nim'] = random_string(6)
    data['nama'] = input('Masukkan nama: ')
    data['alamat'] = input('Masukkan alamat: ')
    data['email'] = input('Masukkan email: ')
    data['no_hp'] = input('Masukkan no hp: ')
    
    data_str = f"{data['nim']},{data['nama']},{data['alamat']},{data['email']},{data['no_hp']}\n"
    print(f"Anda menambahkan data: {data_str}")
    
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data")
        
def sunting_data():
    lihat_data()
    
    cari_nim = input("Silahkan ketik NIM yang ingin dirubah: ")
    nim_ditemukan = False
    
    try:
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
            file.seek(0)
            file.truncate()
            
            for i in range(len(lines)):
                data = lines[i].strip().split(',')
                
                if data[0] == cari_nim:
                    print(f"\nData ditemukan, silahkan ubah isi datanya: ")
                    
                    nama_baru = input("Masukkan Nama: ")
                    alamat_baru = input("Masukkan Alamat: ")
                    email_baru = input("Masukkan Email: ")
                    no_hp_baru = input("Masukkan No HP: ")
                    
                    data_str = f"{cari_nim},{nama_baru},{alamat_baru},{email_baru},{no_hp_baru}"
                    lines[i] = data_str
                    nim_ditemukan = True
                    print(f"Anda merubah isi data menjadi: {data_str}")
                    break
                    
            file.writelines(lines)
            
            if not nim_ditemukan:
                print("Data tidak ditemukan")
                
    except Exception as e:
        print(f"Gagal mengubah data: {str(e)}")
                    
def hapus_data():
    lihat_data()
    
    cari_nim = input("Masukkan NIM yang ingin dihapus: ")
    nim_ditemukan = False
    
    try:
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            
            for i in range(len(lines)):
                data = lines[i].strip().split(',')
                if data[0] == cari_nim:
                    nim_ditemukan = True
                else:
                    file.write(lines[i])
            
            if nim_ditemukan:
                print(f"Data {cari_nim} berhasil dihapus")
            else:
                print(f"NIM tidak ditemukan")
        
    except Exception as e:
        print(f"Gagal menghapus data: {str(e)}")