# Operasi Manipulasi String

# Menyambung String
nama = "Dio"
pujian = "KECE"
print(nama + " " + pujian)

# Mengitung Panjang String
nama_lengkap = "Satya Wibowo"
panjang = len(nama_lengkap)
print(panjang)

# Operator untuk String
s = "S"
status = s in nama_lengkap
print("apakah " + s + " ada di " + nama_lengkap + ", " + str(status))

D = "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

# Pengulangan String
print("-"*10)
print(10*"-")

# Indexing
print("index ke-0 : " + nama_lengkap[0]) # Mengambil Index ke 0
print("index ke-6 : " + nama_lengkap[6]) # Mengambil Index ke 6
print("index ke-(-1) : " + nama_lengkap[-1]) # Mengambil Index Belakang
print("index ke-[6,8) : " + nama_lengkap[4:6]) # Index Diambil Mulai dari Index 4 Sampai Sebelum 6
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # Index Diambil Mulai Dari Index 0,2,4,6,8

# Item Terkecil
print(min(nama_lengkap))

# Item Terbesar
print(max(nama_lengkap))

# Mengecek Nilai ASCII
var_ascii = ord("a")
print("Nilai dari a:", str(var_ascii))

var_ascii = 97
print("Huruf dari 97:", chr(var_ascii))

# Merubah string ke upper case
print(nama_lengkap.upper())

# Merubah stirng ke lower case
print(nama_lengkap.lower())

# Pengecekan
print(nama_lengkap.islower()) # Mengecek apakah huruf kecil semua
print(nama_lengkap.isupper()) # Mengecek apakah huruf besar semua
print(nama_lengkap.isalpha()) # Mengecek apakah huruf semua
# isalnum() Mengecek Apakah Huruf dan Angka
# isdecimal() Mengecek Apakah Numeric
# isspace() Mengecek Apakah Isinya Spasi, Tab dan Enter (Newline \n)
# istitle() Mengecek Apakah Huruf Pertama Setiap Kata Uppercase

# startwith() dan endwith() 
cek_start = "Dio oiD".startswith("Dio")
print("start " + str(cek_start))
cek_end = "Dio oiDk".endswith("Oid")
print("end " + str(cek_end))

# join() dan split()
pisah = ['aku','mau','makan']
gabungan = ' HAHA '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "Naik Delman Keliling Kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

# Alokasi Karakter
kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")
