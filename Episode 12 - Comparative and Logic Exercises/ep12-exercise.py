# EXERCISE 
"""
# 01
Buat program hasil inputan user anatar angka 0-5 dan 8-11 bernilai True.
Untuk selain itu bernilai False.
---------0++++++++5----------8+++++++++11----------
"""
print("---------0++++++++5----------8+++++++++11----------")
userInput = float(input("Masukkan angka : "))

greaterZero = userInput > 0
bellowFive = userInput < 5
greaterEight = userInput > 8
bellowEleven = userInput < 11

firstStep = greaterZero and bellowFive
secondStep = greaterEight and bellowEleven

finalOutput = firstStep or secondStep

print("Hasil nya = ",finalOutput)


"""
# 02
Seperti soal sebelumnya namun dibalik yakni inputan angka 0-5 dan 8-11 bernilai false.
Untuk selain itu bernilai True.
+++++++++++0-----------5+++++++++++8----------11+++++++++++
"""
print("+++++++++++0-----------5+++++++++++8----------11+++++++++++")
userInput = float(input("Masukkan angka : "))

greaterZero = userInput < 0
bellowFive = userInput > 5
greaterEight = userInput < 8
bellowEleven = userInput > 11

firstStep = greaterZero or bellowFive
secondStep = greaterEight or bellowEleven

finalOutput = firstStep and secondStep

print("Hasil nya = ",finalOutput)
