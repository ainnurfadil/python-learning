print("===== STRING WIDTH AND ALIGNMENT =====")

# 1. Membuat Data Awal
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 170.1
data_nomor_sepatu = 44

print("\n--- Data Awal ---")
print(f"Nama: {data_nama}")
print(f"Umur: {data_umur}")
print(f"Tinggi: {data_tinggi}")
print(f"Sepatu: {data_nomor_sepatu}")

# 2. Membuat String Dasar (Single Line)
print("\n--- String Single Line ---")
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(data_string)

# 3. Membuat String Multiline
print("\n--- String Multiline ---")

# Cara Pertama: Menggunakan Karakter Newline (\n)
print("\n(Menggunakan \\n)")
string_multiline_n = f"nama = {data_nama}\numur = {data_umur}\ntinggi = {data_tinggi}\nsepatu = {data_nomor_sepatu}"
print(string_multiline_n)

# Cara Kedua: Menggunakan Triple Quotes (""" atau ''')
print("\n(Menggunakan Triple Quotes)")
data_string_multiline_triplet = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(data_string_multiline_triplet)

# 4. Mengatur Lebar dan Perataan (Alignment)
print("\n--- Mengatur Lebar dan Perataan ---")

# Contoh rata kanan dengan lebar 5 (nama pendek untuk demonstrasi)
data_nama_pendek = "Ucup"
data_umur_pendek = 17
data_tinggi_pendek = 170.1
data_nomor_sepatu_pendek = 44

string_rata_kanan_contoh = f"""nama   = {data_nama_pendek:>10}
umur   = {data_umur_pendek:>10}
tinggi = {data_tinggi_pendek:>10.1f}
sepatu = {data_nomor_sepatu_pendek:>10}
"""
print(string_rata_kanan_contoh)

# Contoh rata kiri
string_rata_kiri_contoh = f"""nama   = {data_nama_pendek:<10}
umur   = {data_umur_pendek:<10}
tinggi = {data_tinggi_pendek:<10.1f}
sepatu = {data_nomor_sepatu_pendek:<10}
"""
print(string_rata_kiri_contoh)

# Contoh rata tengah
string_rata_tengah_contoh = f"""nama   = {data_nama_pendek:^10}
umur   = {data_umur_pendek:^10}
tinggi = {data_tinggi_pendek:^10.1f}
sepatu = {data_nomor_sepatu_pendek:^10}
"""
print(string_rata_tengah_contoh)