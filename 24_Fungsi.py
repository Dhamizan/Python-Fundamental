# Fungsi

# 1. Pengenalan Fungsi
def sapa(): # jadi inisiasi nama fungsinya dulu = def nama_fungsi(argumen"jika pakai"):
    print("Halo, saya adalah fungsi sapa!") # Setelahnya buat isi fungsinya
    
sapa() # Pemanggilan fungsinya

# 2. Fungsi dengan argumen
def sapa_nama(nama): # argumen yang diberikan
    print(f"Halo, {nama}!") # Fungsi ini akan menampilkan pesan
    
sapa_nama("Dio")

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(hasil)
    
tambah(1,2)

# 3. Fungsi dengan kembalian (return)
def tambah(angka1, angka2):
    # Boleh juga gini
    # return angka1 + angka2
    hasil = angka1 + angka2
    return hasil # Kembalian nilai dari fungsi

jumlah = tambah(2,2)
print(jumlah)

# 4. Fungsi dengan default argumen
def sapa_lagi(nama="Anonim"):
    print(f"Halo, {nama}!") # Jika tidak ada argumen, maka akan menggunakan anonim
    
sapa_lagi()
sapa_lagi("Dio")

# 5. Type Hint pada Fungsi
def kuadrat(angka:int) -> int:
    return angka ** 2

hasil = kuadrat(5)
print(hasil)

# 6. Fungsi dengan args (*)
def biodata(*data):
    nama = data[0]
    umur = data[1]
    print(f"Nama: {nama}\nUmur: {umur}")

biodata("Dio", 20)

# 7. Fungsi kwargs (**)
def biodata(**data):
    nama = data["nama"]
    umur = data["umur"]
    print(f"Nama: {nama}\nUmur: {umur}")
    
biodata(nama="Dio", umur=20)

# 8. Gabungan args dan kwargs
def kasir(*harga_barang, **opsi):
    total = sum(harga_barang)
    print(f"Total awal: Rp{total}")

    # Terapkan diskon jika ada
    diskon = opsi.get("diskon", 0)
    if diskon:
        total -= total * (diskon / 100)
        print(f"Diskon {diskon} % diterapkan!")

    # Tampilkan nama pelanggan jika ada
    nama = opsi.get("nama", "Pelanggan")
    print(f"Terima kasih, {nama}!")
    print(f"Total akhir: Rp{total:.0f}")

kasir(10000, 15000, 20000, diskon=10, nama="Dio")

# 9. Fungsi Anonymous Lambda
def kuadrat(a):
    return a ** 2

hasil = kuadrat(3)
print(hasil)

kuadrat = lambda a : a**2
print(kuadrat(3))

# 10. Global Scope
x = 10
def tambah():
    hasil = x**2
    print(hasil)
    
tambah()

# 11. Local Scope
def tambah():
    x = 10
    print(x**2)
    
tambah()