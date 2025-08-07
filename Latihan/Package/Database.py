from . import Fungsi

DB_NAME = "Latihan/Package/Database.txt"
TEMPLATE = {
    'nim' : 'xxxxx',
    'nama' : 255*"",
    'alamat' : 255*"",
    'email' : 255*"",
    'no_hp' : 255*""
}

def init_ft():
    try:
        with open(DB_NAME, 'r', encoding='utf-8'):
            print(f"Database tersedia")
    except:
        print(f"Database tidak ditemukan!, silahkan buat: ")
        Fungsi.tambah_data_ft()