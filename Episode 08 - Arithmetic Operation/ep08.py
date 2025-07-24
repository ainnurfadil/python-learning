# Operasi arithmatika dalam Python

# variabel bilangan
x = 10
y = 3

# Operasi Penjumlahan +
hasil = x + y
print(x , " + " , y , " = ", hasil)

# Operasi Pengurangan -
hasil = x - y
print(x , " - " , y , " = ", hasil)

# Operasi Perkalian *
hasil = x * y
print(x , " * " , y , " = ", hasil)

# Operasi Pembagian /
hasil = x / y
print(x , " / " , y , " = ", hasil)

# Operasi Eksponen (Pangkat) **
hasil = x ** y
print(x , " ** " , y , " = ", hasil)

# Operasi Modulus (hasil sisa pembagian) %
hasil = x % y
print(x , " % " , y , " = ", hasil)

# Operasi Floor Divison (hasil pembagian yang dibulatkan ke angka terkecil) //
hasil = x // y
print(x , " // " , y , " = ", hasil)

# Operational Precedence (Prioritas Operasi)
# Operasi ini menggunakan konsep PEMDAS

a = 2
b = 3
c = 4

hasil = a**b*c+a/b-c%a//b
print(a,"**",b,"*",c,"+",a,"/",b,"-",c,"%",a,"//",b," = ",hasil)



