# Ada beberapa type data yang bisa dibaca oleh python

# type data integer (int): Angka
data_integer = 198
print("data : ", data_integer, " bertipe : ", type(data_integer))

# type data float: Angka yang ada koma nya
data_float = 1.5
data_float2 = 1.567     # kalau dalam bahasa lain ini termasuk double, tapi di python jadi satu dengan float
print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_float2, " bertipe : ", type(data_float2))

# type data string (str): kumpulan karakter yang ditandai dengan tanda petik 2
data_string = "mucha"
print("data : ", data_string, " bertipe : ", type(data_string))

# type data boolean (bool): biner yang ber nilai True/False
data_boolean = False
print("data : ", data_boolean, " bertipe : ", type(data_boolean))

# type data kompleks (complex): tipe data angka yang terdapat bilangan imajiner
data_complex = 5j
print("data : ", data_complex, " bertipe : ", type(data_complex))

# kita bisa memasukkan tipe data dari bahasa C
from ctypes import c_double     # mengimport libray ctypes

data_c_double = c_double(10.5432)
print("data : ", data_c_double, " bertipe : ", type(data_c_double))



