# 1. Merubah Case (Besar/Kecil Huruf)
print("\n--- Merubah Case ---")
salam = "bro"
salam_upper = salam.upper()
print("Original: ",salam, "Upper: ",salam_upper)

alay = "aKu KeCe AbieS"
alay_lower = alay.lower()
print("Original: ",alay, "Upper: ",alay_lower)

# 2. Pengecekan dengan Method isX()
print("\n--- Pengecekan dengan isX() ---")
salam_kecil = "sis"
apakah_lower = salam_kecil.islower()

salam_besar = "SIS"
apakah_upper = salam_besar.isupper()
print(salam_upper,"is lower ? ",apakah_upper)

# Contoh isalpha(), isalnum(), isdecimal(), isspace()
str_alpha = "Python"
apakah_alpha = str_alpha.isalpha()
str_alphanum = "Python3"
apakah_alphanum = str_alphanum.isalnum()
str_decimal = "12345"
apakah_decimal = str_decimal.isdecimal()
str_space = "   "
apakah_space = str_space.isspace()

print(str_alpha, "is alpha ? ",apakah_alpha)
print(str_alphanum, "is alpha ? ",apakah_alphanum)
print(str_decimal, "is alpha ? ",apakah_decimal)
print(str_space, "is alpha ? ",apakah_space)

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul, "is title ? ",cek_judul)

judul_salah = "it is Okay Not To Be Okay"
cek_judul = judul_salah.istitle()
print(judul_salah, "is title ? ",cek_judul)

# 3. Pengecekan Komponen Awal dan Akhir String
print("\n--- Pengecekan Start/End ---")
kalimat = "sajangnim oppa"
cek_start = kalimat.startswith("sajangnim")
print(kalimat, "starts with 'sajangnim'?", cek_start)

cek_end = kalimat.endswith("oppa")
print(kalimat, "ends with 'oppa'?", cek_end)


# 4. Penggabungan dan Pemisahan Komponen String
print("\n--- Join dan Split ---")
pisah = ['aku','sayang','kamu']
gabung_koma = ",".join(pisah)
print(pisah, "digabungkan = ", gabung_koma)

gabung_spasi = " ".join(pisah)
print(pisah, "digabungkan = ", gabung_spasi)

gabung_ehem = " ehem ".join(pisah)
print(pisah, "digabungkan = ", gabung_ehem)


gabungan_str = "aku ehem sayang ehem kamu"
split_str = gabungan_str.split(" ehem ")
print(gabungan_str, "dipisah = ", split_str)


# 5. Alokasi Karakter (Justifikasi String)
print("\n--- Justifikasi String ---")
teks = "teks"
print(teks)
kanan = teks.rjust(10)
print("Rata Kanan (10 char): ", kanan)

kiri = teks.ljust(10)
print("Rata Kiri (10 char): ", kiri)

tengah = teks.center(10)
print("Rata Tengah (10 char): ", tengah)

tengah_fill = teks.center(20, "-")
print("Rata Tengah (20 char, fill '-'): ", tengah_fill)

# 6. Menghilangkan Karakter (Strip)
print("\n--- Strip Karakter ---")
kalimat_strip = "-------tengah-------"
print("Original: ", kalimat_strip)
strip_result = kalimat_strip.strip("-")
print("Strip '-': ", strip_result)

spasi_kalimat = "     spasi di awal dan akhir     "
print("Original: ", spasi_kalimat)
strip_spasi_result = spasi_kalimat.strip()
print("Strip spasi: ", strip_spasi_result)
