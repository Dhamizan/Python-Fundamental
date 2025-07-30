# Pengenalan String

# 1. String bisa menggunakan single quote (') 
data_string = 'Haloo Single Quote'
print(data_string)
print(type(data_string))

# dan double quote (")
data_string = "Haloo Double Quote"
print(data_string)
print(type(data_string))

# Bisa juga digunakan bersamaan
print("Kata dia: 'Aku Mau Naik Unta'")
print("Sekarang Hari Jum'at")


# 2. Penggunaan tanda slash (\)
# membuat tanda ' menjadi string
print('Kata dia: \'Aku Mau Naik Unta\'')
print('Sekarang Hari Jum\'at')

# Backslash (\)
print("C:\\Users\\Games")

# Tab (\t)
print("Kamu\t\tDia, semakin asing")

# Backspace (\b)
print("Kamu \bDia, semakin asing")

# Baris Baru (\n)
print("Daftar Nama:\n1. Dio\n2. Hamizan")


# 3. String Literal atau RAW
# Raw String (r)
print(r'C:\Users\Games')

# Multiline String
print('''
Nama: Dio
Umur: 20
''')

print("""
Nama: Dio
Umur: 20    
""")

# Multiline Literal String dan RAW
print(r"""
Nama: Dio
Umur: 20
Website: dhamizanputra.com/portofolio    
""")

# Format String
nama = "Dio"
print(f"Halo Semuanya, nama saya {nama}")

# Mengatur Lebar
# mengatur lebar
data_nama = "Dio"
data_tinggi = 182
data_string = f"""
nama   = {data_nama:>5}
tinggi = {data_tinggi:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)