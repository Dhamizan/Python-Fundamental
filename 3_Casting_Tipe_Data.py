# Merubah Tipe Data

data_integer = 2
print("Ini data integer:", (data_integer))
print("Tipe data:", type(data_integer))

# Kita coba rubah ke tipe data lainnya
data_float = float(data_integer)
print("Ini data float:", data_float)
print("Tipe data:", type(data_float))

data_string = str(data_integer)
print("Ini data string:", data_string)
print("Tipe data:", type(data_string))

data_boolean = bool(data_integer)
print("Ini data boolean:", data_boolean)
print("Tipe data:", type(data_boolean)) #Jika nilainya 0, maka akan false