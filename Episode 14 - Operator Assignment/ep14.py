# Operator assignment adalah operasi yang dilakukan dengan penyingkatan dengan mengoperasikan assignment

## Operasi Aritmatika

a = 6   # Ini adalah assignment 
print('Nilai a = ',a)

# Operator Assignment Penjumlahan
a += 1  # Ini adalah bentuk operasi dari a = a + 1
print('Nilai a += 1, nilai a menjadi = ',a)

# Operator Assignment Pengurangan
a -= 2  # Ini adalah bentuk operasi dari a = a - 2
print('Nilai a -= 2, nilai a menjadi = ',a)

# Operator Assignment Perkalian
a *= 5  # Ini adalah bentuk operasi dari a = a * 5
print('Nilai a *= 5, nilai a menjadi = ',a)

# Operator Assignment Pembagian
a /= 5  # Ini adalah bentuk operasi dari a = a / 5
print('Nilai a /= 5, nilai a menjadi = ',a) # Hasilnya akan terotomatis bertype data float

# Operator Assignment Perpangkatan
a **= 3  # Ini adalah bentuk operasi dari a = a ** 3
print('Nilai a **= 3, nilai a menjadi = ',a) # Hasilnya akan terotomatis bertype data float

b = 10
print('Nilai b = ',b)

# Operator Assignment Modulus
b %= 3  # Ini adalah bentuk operasi dari b = b % 3
print('Nilai b %= 3, nilai b menjadi = ',b)

b = 10
print('Nilai b = ',b)

# Operator Assignment Floor Division
b //= 3  # Ini adalah bentuk operasi dari b = b // 3
print('Nilai b //= 3, nilai a menjadi = ',b)

## Operasi Bitwise Boolean

#Operator Assignment OR
c = True
print("Nilai c = ",c)
c |= False
print('Nilai c |= False, nilai c menjadi = ',c)
c = False
print("Nilai c = ",c)
c |= False
print('Nilai c |= False, nilai c menjadi = ',c)

#Operator Assignment AND
c = True
print("Nilai c = ",c)
c &= False
print('Nilai c &= False, nilai c menjadi = ',c)
c = True
print("Nilai c = ",c)
c &= True
print('Nilai c &= True, nilai c menjadi = ',c)

#Operator Assignment XOR
c = True
print("Nilai c = ",c)
c ^= False
print('Nilai c ^= False, nilai c menjadi = ',c)
c = True
print("Nilai c = ",c)
c ^= True
print('Nilai c ^= True, nilai c menjadi = ',c)

## Operator Bitwise Shift
d = 0b0100
print('Nilai d = ',d, 'Nilai d biner = ',format(d,'04b'))

# Shift Right
d >>= 2
print('Nilai d >>= 2, nilai d menjadi = ',format(d,'04b'))

# Shift Left
d <<= 1
print('Nilai d >>= 2, nilai d menjadi = ',format(d,'04b'))