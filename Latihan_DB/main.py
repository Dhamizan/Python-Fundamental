import os
import Package as p

if __name__ == '__main__':
    while True:
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        
        p.init_program()
        
        print(f"{'='*15} Data Barang {'='*15}")
        
        print('''
1. Lihat Data
2. Tambah Data
3. Sunting Data
4. Hapus Data
5. Keluar''')
        
        opsi = int(input("Masukkan Opsi: "))
        match opsi:
            case 1: p.lihat_data()
            case 2: p.tambah_data()
            case 3: p.sunting_data()
            case 4: p.hapus_data()
            case 5: break
        
        opsi_lanjut = input("Lanjut? (y/n): ")
        if opsi_lanjut.lower() == 'y':
            continue
        else:
            print(f"Kamu berhasil keluar!")  
            break
        
    