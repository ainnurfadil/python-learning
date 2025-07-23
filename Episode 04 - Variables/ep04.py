# Variabel adalah tempat menyimpan data

# dalam python variabel tidak perlu di deklarasi
# untuk menaruh data nilai disebut assign / menaruh

a = 10
b = 15
panjang = 1000

# cara memanggil variabel
print("nilai a = ", a)
print("nilai b = ", b)
print("nilai panjang = ", panjang)

# contoh penamaan variabel yang boleh:
nilai_y = 15        # variable bisa ditambahkan underscore
juta10 = 10000000
nilaiZ = 17,5       # bisa menggunakan camel case """

""" untuk yang tidak boleh
nilai-a = 10        tidak boleh menggunakan dash
10juta = 1000000    tidak boleh angka berada di paling depan variabel"""

# Ketika variable yang sama di sebutkan 2 kali, maka yang terbaca adalah yang terakhir
a = 7
print("nilai a = ", a) # nilai a yang sebelumnya bernilai 10 menjadi 7

# assignment indirect, mengambil nilai secara tidak langsung
b = a
print("nilai b = ", b) # nilai b akan sama dengan nilai a
