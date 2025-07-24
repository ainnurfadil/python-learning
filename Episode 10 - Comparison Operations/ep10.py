# Operasi Komparasi adalah sebuah operasi perbandingan nilai dari inputan

# Setiap hasil dari komparasi adalah nilai Boolean (True and False)

# Jenis jenis operasinya adalah >,<,>=,<=,==,!=,is, is not

# Inputan variabel
a = 4       # Mengingat kembali, ini namanya assignment
b = 2

# Lebih besar dari (>)
print("LEBIH BESAR >")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = a > b
print(a,">",b,"=",hasil)

# Kurang dari (<)
print("KURANG DARI <")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = a < b
print(a,"<",b,"=",hasil)

# Lebih besar sama dengan (>=)
print("LEBIH BESAR SAMA DENGAN >=")
hasil = a >= 4
print(a,">=",4,"=",hasil)
hasil = b >= 4
print(b,">=",4,"=",hasil)
hasil = a >= b
print(a,">=",b,"=",hasil)

# Kurang dari sama dengan (<=)
print("KURANG DARI SAMA DENGAN <=")
hasil = a <= 4
print(a,"<=",4,"=",hasil)
hasil = b <= 4
print(b,"<=",4,"=",hasil)
hasil = a <= b
print(a,"<=",b,"=",hasil)

# Sama dengan (==)
print("SAMA DENGAN ==")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)
hasil = a == b
print(a,"==",b,"=",hasil)

# Tidak sama dengan (!=)
print("SAMA DENGAN !=")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)
hasil = a != b
print(a,"!=",b,"=",hasil)

"""
KHUSUSON ILA "IS" WA "IS NOT"
IS dan IS NOT adalah operasi untuk membandingkan nilai memory atau object identity
contoh dari perbandingan sebelumnya:
a == 4
a disini sebagai nilai variabel yang menyimpan datanya dalam memory, biasa disebut object.
4 disini berperan sebagai nilai "Literal", nilai Literal disini sifatnya nilai yang di eksekusi khusus di baris tersebut.

Untuk perbandingan tersebut kalo di buat seperti:
a is 4
dalam python tidak dapat di eksekusi atau akan ada warning bahwa object dan literal tidak dapat dibandingkan.

untuk itu misalkan contoh kasus seperti ini:
a = 4
b = 4

a is b = True
maka hasil dari "a is b" adalah True

kenapa bisa gitu, karena sebagai contoh ketika:
id(a) = 140735169250312         # identitas dari variabel a yang tersimpan di dalam memory pc yang buat deskripsi ini
hex(id(a)) = 0x7fff75c54408     # hex code dari variabel a yang tersimpan di dalam memory pc yang buat deskripsi ini
id(a) = 140735169250312         # identitas dari variabel b, hasilnya sama dengan a karena nilainya sama dan akan berbeda jika nilainya berbeda
hex(id(a)) = 0x7fff75c54408     # hex code dari variabel b, hasilnya sama dengan a karena nilainya sama dan akan berbeda jika nilainya berbeda
"""
x = 4
y = 5

print()
print("nilai x =", x," id = ",hex(id(x)))
print("nilai x =", y," id = ",hex(id(y)))

# is operation
print('\nOPERATION "IS"')
hasil = x is y
print(a,"is",y,"=",hasil)

# is not operation
print('OPERATION "IS NOT"')
hasil = x is not y
print(x,"is not",y,"=",hasil)

