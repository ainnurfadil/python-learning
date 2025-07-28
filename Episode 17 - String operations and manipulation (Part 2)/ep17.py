# 1. Merubah Case (Besar/Kecil Huruf)
print("\n--- Merubah Case ---")
salam = "bro"
salam_upper = salam.upper()
<<<<<<< Updated upstream
print(f"Original: '{salam}', Upper: '{salam_upper}'")

alay = "aKu KeCe AbieS"
alay_lower = alay.lower()
print(f"Original: '{alay}', Lower: '{alay_lower}'")
=======
print("Original: ",salam, "Upper: ",salam_upper)

alay = "aKu KeCe AbieS"
alay_lower = alay.lower()
print("Original: ",alay, "Upper: ",alay_lower)
>>>>>>> Stashed changes

# 2. Pengecekan dengan Method isX()
print("\n--- Pengecekan dengan isX() ---")
salam_kecil = "sis"
apakah_lower = salam_kecil.islower()
print(f"'{salam_kecil}' islower? {apakah_lower}")

salam_besar = "SIS"
apakah_upper = salam_besar.isupper()
print(f"'{salam_besar}' isupper? {apakah_upper}")

# Contoh isalpha(), isalnum(), isdecimal(), isspace()
str_alpha = "Python"
str_alphanum = "Python3"
str_decimal = "12345"
str_space = "   "

print(f"'{str_alpha}' isalpha? {str_alpha.isalpha()}")
print(f"'{str_alphanum}' isalnum? {str_alphanum.isalnum()}")
print(f"'{str_decimal}' isdecimal? {str_decimal.isdecimal()}")
print(f"'{str_space}' isspace? {str_space.isspace()}")

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(f"'{judul}' istitle? {cek_judul}")

judul_salah = "it is Okay Not To Be Okay"
print(f"'{judul_salah}' istitle? {judul_salah.istitle()}")

# 3. Pengecekan Komponen Awal dan Akhir String
print("\n--- Pengecekan Start/End ---")
kalimat = "sajangnim oppa"
cek_start = kalimat.startswith("sajangnim")
print(f"'{kalimat}' starts with 'sajangnim'? {cek_start}")

cek_end = kalimat.endswith("oppa")
print(f"'{kalimat}' ends with 'oppa'? {cek_end}")

# 4. Penggabungan dan Pemisahan Komponen String
print("\n--- Join dan Split ---")
pisah = ['aku', 'sayang', 'kamu']
gabung_koma = ",".join(pisah)
print(f"List: {pisah}, Joined by ',': '{gabung_koma}'")

gabung_spasi = " ".join(pisah)
print(f"List: {pisah}, Joined by ' ': '{gabung_spasi}'")

gabung_ehem = " ehem ".join(pisah)
print(f"List: {pisah}, Joined by ' ehem ': '{gabung_ehem}'")

gabungan_str = "aku ehem sayang ehem kamu"
split_str = gabungan_str.split(" ehem ")
print(f"String: '{gabungan_str}', Split by ' ehem ': {split_str}")

# 5. Alokasi Karakter (Justifikasi String)
print("\n--- Justifikasi String ---")
teks = "teks"
print(f"Original: '{teks}'")
kanan = teks.rjust(10)
print(f"Rata Kanan (10 char): '{kanan}'")

kiri = teks.ljust(10)
print(f"Rata Kiri (10 char): '{kiri}'")

tengah = teks.center(10)
print(f"Rata Tengah (10 char): '{tengah}'")

tengah_fill = teks.center(20, "-")
print(f"Rata Tengah (20 char, fill '-'): '{tengah_fill}'")

# 6. Menghilangkan Karakter (Strip)
print("\n--- Strip Karakter ---")
kalimat_strip = "-------tengah-------"
print(f"Original: '{kalimat_strip}'")
strip_result = kalimat_strip.strip("-")
print(f"Strip '-': '{strip_result}'")

spasi_kalimat = "     spasi di awal dan akhir     "
print(f"Original: '{spasi_kalimat}'")
strip_spasi_result = spasi_kalimat.strip()
print(f"Strip spasi: '{strip_spasi_result}'")
