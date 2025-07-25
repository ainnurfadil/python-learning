# BITWISE OPERATOR
# Operator untuk mengcompare angka biner
# Terdapat beberapa operator yang duganakan
# OR, AND, XOR, NOT, LEFT SHIT, RIGHT SHIFT

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('\nOR (|)===================')
print('nilai : ',a,' , angka binarynya : ',format(a,'08b'))
print('nilai : ',b,' , angka binarynya : ',format(b,'08b'))
print('----------------------------------------------(|)')
print('nilai : ',c,' , angka binarynya : ',format(c,'08b'))


# Bitwise AND (&)
c = a & b
print('\nAND (&)===================')
print('nilai : ',a,' , angka binarynya : ',format(a,'08b'))
print('nilai : ',b,' , angka binarynya : ',format(b,'08b'))
print('----------------------------------------------(&)')
print('nilai : ',c,' , angka binarynya : ',format(c,'08b'))


# Bitwise XOR (^)
c = a ^ b
print('\nXOR (^)===================')
print('nilai : ',a,'  , angka binarynya : ',format(a,'08b'))
print('nilai : ',b,'  , angka binarynya : ',format(b,'08b'))
print('----------------------------------------------(^)')
print('nilai : ',c,' , angka binarynya : ',format(c,'08b'))

# Bitwise NOT (~)
# Untuk operator bitwise NOT, jika inputan angkanya 9, untuk kebalikannya hasilnya akan menjadi -10.
# Dikarenakan 0 nya masih terhitung angka biner, jadi akan terhitung dibelakang angka 0 untuk membalikkan.
c = ~a
print('\nNOT (~)===================')
print('nilai : ',a,'   , angka binarynya :  ',format(a,'08b')) 
print('----------------------------------------------(^)')
print('nilai : ',c,' , angka binarynya : ',format(c,'09b'))

# Jadi, jika mau membalikkan angka biner bisa menggunakan metode operator XOR dengan pembanding nya bernilai 08b11111111
# sebagai contoh:

e = 0b00001001
f = 0b11111111

print('\nMembalikkan Biner=========')
print('nilai : ',a,' , angka binarynya   : ',format(a,'08b'))
print('nilai : ',e^f,' , angka binarynya : ',format(e^f,'08b'))

# Shift Right (>>) Menggeser angka biner ke kanan
c = a >> 2
print('\nShift Right (>>)===================')
print('nilai : ',a,' , angka binarynya : ',format(a,'08b')) 
print('----------------------------------------------(>> 2)')
print('nilai : ',c,' , angka binarynya : ',format(c,'08b'))

# Shift Left (<<) Menggeser angka biner ke kiri
c = a << 2
print('\nShift Left (<<)===================')
print('nilai : ',a,' , angka binarynya  : ',format(a,'08b')) 
print('----------------------------------------------(<< 2)')
print('nilai : ',c,' , angka binarynya : ',format(c,'08b'))