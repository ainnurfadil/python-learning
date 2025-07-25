# Macam macam pembuatan string

# 1. Dengan menggunakan quote

## Single quote
data = 'menggunakan single quote'
print(data)

## Double quote

data = "menggunakan double quote"
print(data)

## Keduanya dapat digunakan bebarengan
print('"Halo apa kabar?"')
print("'Halo apa kabar?'")
print("Hari ini adalah hari Jum'at")

# 2. Dengan menggunakan Tanda \

## Merubah tanda ' menjadi string
print('Hari ini adalah hari Jum\'atkah?')

## Merubah backslash
print("C:\\user\\Mucha")    # Hasilnya adalah C:\user\Mucha

## Tab
print("Ini di double\t\ttab")

## Newline
print("Baris pertama.\nBaris kedua.")   # Ini namanya LF -> Line Feed. Biasa dipakai os UNIX.
print("Baris pertama.\rBaris kedua.")   # ini namanya CR -> Carriege Return. Biasa dipakai os lama Commodore, acorn, lisp.
print("Baris pertama.\n\rBaris kedua.") # ini gabungannya CRLF, biasa dipakai oleh WINDOWS.

# 3. String literal atau Raw

## Penulisan seperti ini akan rusak
print('C:\new folder')

## Raw String
print(r'C:\new folder')

## Multiline literal string
print("""
Nama    : Mucha
Kelas   : Sudah kuliah
""")

## Multiline literal string dan Raw
print("""
Nama    : Mucha
Kelas   : Masih kuliah \ Computer Science
Website : www.localhost.com/username
""")
