# Casting type data adalah merubah type data satu ke jenis type data yang lain

data_int = 9
print("data : ", data_int, " bertipe : ", type(data_int))

# Ketika mau merubah tipe data, kita bisa menggunakan format typeData(nama_variable)

data_float = float(data_int)    # Jadi disini variable yang di panggil di masukkan ke variabel baru
print("data : ", data_float, " bertipe : ", type(data_float))

print("==========INTGER========>")
data_int = 0
print("data : ", data_int, " bertipe : ", type(data_int))

data_float = float(data_int)
data_bool = bool(data_int)      # disini nilai boolean menjadi False
data_string = str(data_int)
print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_bool, " bertipe : ", type(data_bool))
print("data : ", data_string, " bertipe : ", type(data_string))

data_int = -1
print("data : ", data_int, " bertipe : ", type(data_int))

data_float = float(data_int)
data_bool = bool(data_int)      # disini menandakan boolean di luar angka 0 bernilai True
data_string = str(data_int)
print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_bool, " bertipe : ", type(data_bool))
print("data : ", data_string, " bertipe : ", type(data_string))

print("==========FLOAT========>")
data_float = 9.9
print("data : ", data_float, " bertipe : ", type(data_float))

data_int = int(data_float)        # nilai desimal float di atas 5, maka akan dibulatkan keangka terkecil/kebawah, jadi hasil ini menjadi angka 9 bukan 10
data_bool = bool(data_float)      
data_string = str(data_float)
print("data : ", data_int, " bertipe : ", type(data_int))
print("data : ", data_bool, " bertipe : ", type(data_bool))
print("data : ", data_string, " bertipe : ", type(data_string))

print("==========BOOLEAN========>")
data_boolean = True
print("data : ", data_boolean, " bertipe : ", type(data_boolean))

data_int = int(data_boolean)        # nilai integer dari True adalah 1, dan untuk False adalah 0
data_float = float(data_boolean)    # nilai dari float adalah 1.0, ada angka desimal 0 di belakangnya
data_string = str(data_boolean)     # nilai string akan menjadi "True" atau "False" tergantung dari input nilainya
print("data : ", data_int, " bertipe : ", type(data_int))
print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_string, " bertipe : ", type(data_string))

print("==========STRING========>")
data_string2 = "fadil"
print("data : ", data_string2, " bertipe : ", type(data_string2))

# data_int = int(data_string2)            # nilai string yang di ubah ke integer, tidak bisa terbaca dan terjadi error, harus character angka, dan akan bernilai 1 walau bercharacter "0"
data_boolean = bool(data_string2)         # nilai string yang berubah ke boolean, akan bernilai True walau pun characternya "False", jika nilai string kosong atau tidak ada character maka akan bernilai False
# data_float = float(data_string2)        # nilai string harus character angka
# print("data : ", data_int, " bertipe : ", type(data_int))
print("data : ", data_boolean, " bertipe : ", type(data_boolean))
# print("data : ", data_string2, " bertipe : ", type(data_string2))

print("")

data_string2 = "0"
print("data : ", data_string2, " bertipe : ", type(data_string2))

data_int = int(data_string2)         # nilai integer sesuai dengan caharacternya
data_float = float(data_string2)     # nilai dari float adalah 1.0, ada angka desimal 0 di belakangnya
data_boolean = bool(data_string2)     # nilai string akan menjadi "True" atau "False" tergantung dari input nilainya
print("data : ", data_int, " bertipe : ", type(data_int))
print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_boolean, " bertipe : ", type(data_boolean))

print("")

data_string2 = ""
print("data : ", data_string2, " bertipe : ", type(data_string2))

# data_int = int(data_string2)        # harus ada character, hasilnya error
# data_float = float(data_string2)    # harus ada character, hasilnya error
data_boolean = bool(data_string2)     
# print("data : ", data_int, " bertipe : ", type(data_int))
# print("data : ", data_float, " bertipe : ", type(data_float))
print("data : ", data_boolean, " bertipe : ", type(data_boolean))












