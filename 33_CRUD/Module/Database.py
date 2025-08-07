from . import Operasi

DB_NAME = "33_CRUD/data.txt"
TEMPLATE = {
    "id_barang" : "xxxxxx",
    "nama_barang" : 255*" ",
    "harga_barang" : 0,
    "jumlah_barang" : 0,
}

def init_console():
    try:
        with open(DB_NAME, "r"):
            print("Database Tersedia")
    except:
        print(f"Database Tidak Tersedia, Silahkan Masukkan Data Baru")
        Operasi.tambah_data_ft()