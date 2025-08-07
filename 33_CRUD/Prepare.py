import os

if __name__ == "__main__":
    so = os.name
    
    while True:
        match so:
            case "nt": os.system("cls")
            case "posix": os.system("clear")
            
        print(f"{"="*5} Sistem Tambah Data Barang {"="*5}")
        print(f"{"="*37}")
        print(f"1. Lihat Barang")
        print(f"2. Buat Barang")
        print(f"3. Edit Barang")
        print(f"4. Hapus Barang")
        print(f"5. Keluar")
        
        opsi_pengguna = int(input("Masukkan opsi yang ingin digunakan: "))
        
        match opsi_pengguna:
            case 1: print("Lihat Barang")
            case 2: print("Buat Barang")
            case 3: print("Edit Barang")
            case 4: print("Hapus Barang")
            case 5: print("Keluar")
        break
    
    print("Terima Kasih Broo")