## Penggunaan PIP Numpy

'''
Numpy merupakan package yang berisi fungsi operasi matematika
'''

import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])      # Menggunakan fungsi array pada numpy

# cara pemanggilannya sama
print(f'list_a = {list_a}')
print(f'vector_a = {vector_a}')

'''
Ketika list di berikan operasi matematika akan menjadi error
print(list_a**2)        # Ini akan menjadi error ketika dijalankan
'''
print(f'vector_a = {vector_a*2}')
print(f'vector_a = {vector_a**5}')

matrix_b = np.array([(2,4),(6,8)])      # Fungsi untuk menampilkan array
print(f'matrix_b = \n{matrix_b}')
print(f'matrix_b = \n{matrix_b**2}')    # Ketika array dipangkatkan

zeros_c = np.zeros((2,2))
print(f'zeros c = \n{zeros_c}')

ones_d = np.ones((2,2))
print(f'ones d = \n{ones_d}')

jumlah = matrix_b + matrix_b**2 + ones_d
print('\nJumlah matrix_b + matrix_b**2 + ones_d\n',jumlah)