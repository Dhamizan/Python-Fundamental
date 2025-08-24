import os
import datetime as dt
from . import Fungsi as fn

BASE_DIR = os.path.dirname(__file__)
DB_NAME = os.path.join(BASE_DIR, "data.txt")
TEMPLATE = {
    "id":"xxxx",
    "nama":255*"",
    "umur":0,
    "ttl":None
}

def init_awal():
    try:
        with open(DB_NAME, 'r', encoding='utf8'):
            print("Database Tersedia!")
    except:
        print("Database Belum Tersedia, Silahkan Buat!")
        fn.tambah_data_awal()