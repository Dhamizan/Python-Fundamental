import os
import Package.Database as db
import Package.Fungsi as fn

if __name__ == "__main__":
    sistem = os.name
    
    while True:
        match sistem:
            case 'nt': os.system('cls')
            case 'posix': os.system('clear')
        
        print(f"{'='*20} Biodata {"="*20}")

        db.init_awal()
        
        print('''
Pilih Opsi:
1. Lihat Data
2. Tambah Data
3. Sunting Data
4. Hapus Data
5. Keluar''')
        
        opsi = int(input("Masukkan Opsi: "))
        
        match opsi:
            case 1: fn.lihat_data()
            case 2: fn.tambah_data()
            case 3: fn.sunting_data()
            case 4: fn.hapus_data()
            case 5: break
            
        opsi_lanjut = int(input("Lanjut? (1)"))
        
        match opsi_lanjut:
            case 1: continue
            