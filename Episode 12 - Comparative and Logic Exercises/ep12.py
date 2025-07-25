# Membuat rentang dari gabungan angka

"""
Contoh studi kasus pertama:
User meng input angka yang ketentuannya adalah jika angka
inputan kurang dari 3 bernilai True dan lebih dari 7 bernilai 
True, untuk inputan angka di antara 3 dan 7 akan bernilai False
"""

print("+++++++3-------7++++++++")
inputUser = float(input("masukkan angka : "))

isLowerThan = inputUser < 3
isHigherThan = inputUser > 7

result = isLowerThan or isHigherThan  
print("Hasilnya adalah = ", result)


"""
Contoh studi kasus kedua:
Sama seperti studi kasus sebelumnya, namun di balik yang angkanya 
diantara 3 dan 7 bernilai True, dan jika kurang dari 3 dan lebih dari 7 
bernilai False

"""

print("--------3+++++++++7-------")
inputUser = float(input("masukkan angka : "))

isLowerThan = inputUser > 3
isHigherThan = inputUser < 7

print(isLowerThan)
print(isHigherThan)

result = isLowerThan and isHigherThan  
print("Hasilnya adalah = ", result)