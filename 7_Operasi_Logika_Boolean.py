# Operasi Logika Boolean

# Not
# Kebalikan
a = True
hasil = not a
print(hasil)

# Or
# True or True = True, True or False = True, False or True = True, False or False = False
# Apabila salah satu terdiri dari True, maka True
a = True
b = False
hasil = a or b
print(hasil)

# And
# True and True = True, True and False = False, False and True = False, False and False = False
# Apabila salah satu terdiri dari False, maka False
a = True
b = False
hasil = a and b
print(hasil)

# Xor
# True xor True = False, True xor False = True, False xor True = True, False xor False = False
a = True
b = False
hasil = a ^ b
print(hasil)