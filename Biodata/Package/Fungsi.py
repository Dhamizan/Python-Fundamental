import random, string
from datetime import datetime
from . import Database as db

def buat_id(panjang:int)->str:
    hasil = ''
    for i in range(panjang):
        hasil = hasil + random.choice(string.ascii_letters)
    return hasil        

def tambah_data_awal():
    db.TEMPLATE.copy()
    
    bulan_data = {
    "January": "Januari", "February": "Februari", "March": "Maret",
    "April": "April", "May": "Mei", "June": "Juni",
    "July": "Juli", "August": "Agustus", "September": "September",
    "October": "Oktober", "November": "November", "December": "Desember"
    }
    
    tambah_id = buat_id(4)
    nama = input("Masukkan Nama: ")
    umur = int(input("Masukkan Umur: "))
    ttl = input("Masukkan TTL (tanggal bulan tahun): ")
    hari, bulan, tahun = ttl.split()    
    f_ttl = datetime.strptime(f"{hari} {bulan} {tahun}", '%d %B %Y')
    bulan_en = f_ttl.strftime('%B')
    bulan_in = bulan_data[bulan_en]
    f_ttl_in = f"{f_ttl.day} {bulan_in} {f_ttl.year}"
    data_str = f"{tambah_id}, {nama}, {umur}, {f_ttl_in}\n"
    
    try:
        with open(db.DB_NAME, 'w', encoding='utf8') as file:
            file.write(data_str)
            print("Data Berhasil Ditambahkan ke Database!")
    except Exception as e:
        print(f"Gagal Menambahkan Data!: {e}")
        
def read():
    try:
        with open(db.DB_NAME, 'r', encoding='utf8') as file:
            return file.readlines()
    except Exception as e:
        return []
    
def lihat_data():
    data = read()
    
    print(f"{'ID':4} | {'Nama':8} | {'Umur':2} | {'TTL':16}")
    
    for i, d in enumerate(data):
        data_space = d.split(', ')
        data_id = data_space[0]
        data_nama = data_space[1]
        data_umur = data_space[2]
        data_ttl = data_space[3]
        
        print(f"{data_id:4} | {data_nama:8} | {data_umur:} | {data_ttl:16}")
        
def tambah_data():
    db.TEMPLATE.copy()
    
    bulan_data = {
    "January": "Januari", "February": "Februari", "March": "Maret",
    "April": "April", "May": "Mei", "June": "Juni",
    "July": "Juli", "August": "Agustus", "September": "September",
    "October": "Oktober", "November": "November", "December": "Desember"
    }
    
    tambah_id = buat_id(4)
    nama = input("Masukkan Nama: ")
    umur = int(input("Masukkan Umur: "))
    ttl = input("Masukkan TTL (tanggal bulan tahun): ")
    hari, bulan, tahun = ttl.split()    
    f_ttl = datetime.strptime(f"{hari} {bulan} {tahun}", '%d %B %Y')
    bulan_en = f_ttl.strftime('%B')
    bulan_in = bulan_data[bulan_en]
    f_ttl_in = f"{f_ttl.day} {bulan_in} {f_ttl.year}"
    data_str = f"{tambah_id}, {nama}, {umur}, {f_ttl_in}\n"
    
    try:
        with open(db.DB_NAME, 'a', encoding='utf8') as file:
            file.write(data_str)
            print("Data Berhasil Ditambahkan ke Database!")
    except Exception as e:
        print(f"Gagal Menambahkan Data!: {e}")
        
def sunting_data():
    lihat_data()
    
    cari_id = input("Cari ID yang Ingin Dirubah: ")
    found = False
    
    with open(db.DB_NAME, 'r+', encoding='utf8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        
        for i in range(len(lines)):
            data = lines[i].strip().split(',')
            
            if data[0] == cari_id:
                found = True
                bulan_data = {
                "January": "Januari", "February": "Februari", "March": "Maret",
                "April": "April", "May": "Mei", "June": "Juni",
                "July": "Juli", "August": "Agustus", "September": "September",
                "October": "Oktober", "November": "November", "December": "Desember"
                }
                
                tambah_id = cari_id
                nama = input("Masukkan Nama: ")
                umur = int(input("Masukkan Umur: "))
                ttl = input("Masukkan TTL (tanggal bulan tahun): ")
                hari, bulan, tahun = ttl.split()    
                f_ttl = datetime.strptime(f"{hari} {bulan} {tahun}", '%d %B %Y')
                bulan_en = f_ttl.strftime('%B')
                bulan_in = bulan_data[bulan_en]
                f_ttl_in = f"{f_ttl.day} {bulan_in} {f_ttl.year}"
                data_str = f"{tambah_id}, {nama}, {umur}, {f_ttl_in}\n"
                lines[i] = data_str
                break
        
        file.writelines(lines)
        print('Data Berhasil Diubah')
        
        if not found:
                print('Data Tidak Ditemukan!')
                sunting_data()
                
def hapus_data():
    lihat_data()
    
    cari_id = input("Cari ID: ")
    found = False
    
    with open(db.DB_NAME, 'r+', encoding='utf8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        
        for i in range(len(lines)):
            data = lines[i].strip().split(',')
            
            if data[0] == cari_id:
                found = True
            else:
                file.write(lines[i])
                
    if not found:
            print('Data TIdak Ditemukan!')
            hapus_data()
