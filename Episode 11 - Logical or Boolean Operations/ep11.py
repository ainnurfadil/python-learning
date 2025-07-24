# Operasi logika atau boolean

# macam - macam logikanya NOT, OR, AND, XOR

# NOT (nilai boolean berkebalikan)
print("\nLOGIKA NOT ==========")
a = True
b = not a
print("data a =", a)
print("------------NOT")
print("data b =", b)

print()
a = False
b = not a
print("data a =", a)
print("------------NOT")
print("data b =", b)

# OR (akan bernilai True jika salah satu nya bernilai True)
print("\nLOGIKA OR ==========")
a = True
b = True
c = a or b
print(a," or",b," =",c)
a = True
b = False
c = a or b
print(a," or",b,"=",c)
a = False
b = True
c = a or b
print(a,"or",b," =",c)
a = False
b = False
c = a or b
print(a,"or",b,"=",c)

# AND (akan bernilai True jika semuanya bernilai True)
print("\nLOGIKA AND ==========")
a = True
b = True
c = a and b
print(a," and",b," =",c)
a = True
b = False
c = a and b
print(a," and",b,"=",c)
a = False
b = True
c = a and b
print(a,"and",b," =",c)
a = False
b = False
c = a and b
print(a,"and",b,"=",c)

# XOR (akan bernilai True jika HANYA bernilai 1 True)
print("\nLOGIKA XOR ==========")
a = True
b = True
c = a ^ b
print(a," xor",b," =",c)
a = True
b = False
c = a ^ b
print(a," xor",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"xor",b," =",c)
a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)
