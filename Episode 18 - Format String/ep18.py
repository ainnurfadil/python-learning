# 1. Format String Dasar (f-string)
print("\n--- F-String Dasar ---")
nama = "Marlin"
format_str = f"Hello {nama}"
print(format_str)

# 2. Format String dengan Tipe Data Berbeda
print("\n--- F-String dengan Tipe Data Berbeda ---")
angka_int = 2005
format_int = f"angka = {angka_int}"
print(format_int)

angka_float = 2005.5
format_float = f"angka = {angka_float}"
print(format_float)

boolean_var = True
format_bool = f"nilai boolean = {boolean_var}"
print(format_bool)

# 3. Formatting Angka Lebih Lanjut
print("\n--- Formatting Angka Lebih Lanjut ---")

# Menampilkan Bilangan Bulat (Integer)
angka_bulat = 15
format_bulat = f"bilangan bulat = {angka_bulat:d}"
print(format_bulat)

# Menampilkan Bilangan Ribuan dengan Pemisah
angka_jutaan = 2000000
format_jutaan = f"jutaan = {angka_jutaan:,}"
print(format_jutaan)

# Mengontrol Jumlah Angka Desimal
angka_desimal = 2005.54321
format_dua_desimal = f"desimal (2 belakang koma) = {angka_desimal:.2f}"
print(format_dua_desimal)

# Menampilkan Leading Zero (Nol di Depan)
angka_leading_zero = 2005.543
format_leading_zero = f"leading zero = {angka_leading_zero:09.3f}"
print(format_leading_zero)

# Menampilkan Tanda Plus (+) untuk Angka Positif
angka_positif = 10
format_plus = f"plus = {angka_positif:+d}"
print(format_plus)

angka_negatif = -10
format_minus = f"minus = {angka_negatif:+d}"
print(format_minus)

# Memformat Persentase
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# 4. Melakukan Operasi Aritmatika di dalam Placeholder
print("\n--- Operasi Aritmatika dalam F-String ---")
harga = 10000
jumlah = 5
format_total = f"harga total = {harga * jumlah:,}"
print(format_total)

# 5. Format Angka Lain (Biner, Oktal, Heksadesimal)
print("\n--- Format Angka Lain ---")
angka_basis = 255
format_biner = f"biner = {bin(angka_basis)}"
format_oktal = f"oktal = {oct(angka_basis)}"
format_hex = f"hex = {hex(angka_basis)}"
print(format_biner)
print(format_oktal)
print(format_hex)