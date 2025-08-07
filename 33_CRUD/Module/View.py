from . import Operasi

def read_console():
    file_data = Operasi.read()
    
    id_barang = "ID Barang"
    nama_barang = "Nama Barang"
    harga_barang = "Harga Barang"
    jumlah_barang = "Jumlah Barang"
    
    print(f"\n{"="*100}")
    print(f"{id_barang:8} | {nama_barang:20} | {harga_barang:14} | {jumlah_barang:10}")
    print(f"\n{"="*100}")
    
    for i, data in enumerate(file_data):
        data_break = data.split(",")
        id_barang = data_break[0]
        nama_barang = data_break[1]
        harga_barang = data_break[2]
        jumlah_barang = data_break[3]
        print(f"{id_barang:8} | {nama_barang:20} | {harga_barang:14} | {jumlah_barang:10}")
        