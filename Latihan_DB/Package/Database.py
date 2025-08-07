from Package.Fungsi import tambah_data_awal

DB_NAME = 'Latihan_DB/Package/isi_data.txt'
TEMPLATE = {
    'id_barang' : 'xxxxxx',
    'nama_barang' : 255*'',
    'harga_barang' : 255*'',
    'stok_barang' : 255*''
}

def init_program():
    try:
        with open(DB_NAME, 'r', encoding='utf-8'):
            print(f"Data Barang Tersedia")
    except Exception as e:
        print(f"Data Barang Tidak Tersedia. {e}")
        tambah_data_awal()