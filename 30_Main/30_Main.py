# __main__ sebagai gate program

print(f"__name__ dari file 30_Main.py adalah: {__name__}")
import Tes

# Contoh Penggunaan
def tambah(a:int, b:int)->int:
    return a + b

if __name__ == "__main__":
    angka_1 = 20
    angka_2 = 30
    hasil = tambah(angka_1, angka_2)
    print(f"Hasil dari {angka_1} + {angka_2} = {hasil}")
    
# Import dari package
import package