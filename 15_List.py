# List []

# Data List Number
data_number = [1,2,3,4]
print(data_number)

# Data List String
data_string = ["Dio", "Hamizan", "Putra"]
print(data_string)

# Data List Boolean
data_boolean = [True, False, True]
print(data_boolean)

# Data List Campuran
data_campuran = [1, "Dio", True, 4.0, False]
print(data_campuran)

# Membuat Data List dengan range (start, stop, step)
data_range = range(0,10,2)
print(data_range)

data_list = list(data_range)
print(data_list)

# Membuat Data List dengan for loop dan list comprehension
data_l = [i**2 for i in range(0,10)]
print(data_l)

data_l_if = [i for i in range(0, 10) if i != 5]
print(data_l_if)

# Nested List
data_1 = [1,2,3]
data_2 = [3,4,5]
data_gabung = data_1 + data_2
data_aja = [data_1, data_2]
print(data_gabung)
print(data_aja)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[1][2])
matrix[1][2] = 10
print(matrix)

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
    
