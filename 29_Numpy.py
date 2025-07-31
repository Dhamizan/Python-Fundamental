# Numpy

import numpy as np

data_list = [1,2,3,4,5,6,7,8]
vektor_list = np.array([1,2,3,4,5,6,7,8])

print(f"data_list = {data_list}")
# print(data_list**2) <- ini akan gagal
print(f"vektor_list = {vektor_list}")
print(f"a pangkat 2 = {vektor_list**2}")
print(f"a kali 5 = {vektor_list*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")