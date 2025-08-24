import os
from Package import Database as db
from Package import Fungsi


if __name__ == "__main__":
    sistem = os.name
    
    while True:
        match sistem:
            case 'nt': os.system('cls')
            case 'posix': os.system('clear')
            
        print(f"{'='*10} Daftar Mahasiswa Universitas Fiksi {'='*10}")
        
        db.init_ft()
        
        print(f"1. Lihat Mahasiswa")
        print(f"2. Tambah Mahasiswa")
        print(f"3. Sunting Mahasiswa")
        print(f"4. Hapus Mahasiswa")
        print(f"5. Keluar Sistem")
        
        opsi = int(input("Masukkan Opsi: "))
        
        match opsi:
            case 1: Fungsi.lihat_data()
            case 2: Fungsi.tambah_data()
            case 3: Fungsi.sunting_data()
            case 4: Fungsi.hapus_data()
            case 5:
                print(f"Anda berhasil keluar!")
                break
            
        opsi_lanjut = input("- Lanjut = y \n- Tidak Lanjut = n\nMasukkan Opsi: ")
        
        if opsi_lanjut == 'n' or opsi_lanjut == 'N':
            print(f"Anda berhasil keluar!") 
            break
        else:
            continue