# 1. Import Library datetime
import datetime as dt

# 2. Input Data Kelahiran dari User
print("\nSilahkan masukkan tanggal, bulan, dan tahun lahir Anda")
tanggal_input = int(input("Tanggal \t: "))
bulan_input = int(input("Bulan \t\t: "))
tahun_input = int(input("Tahun \t\t: "))

# 3. Membuat Objek Tanggal Lahir
tanggal_lahir = dt.date(tahun_input, bulan_input, tanggal_input)
print(f"Tanggal lahir Anda : {tanggal_lahir}")

# 4. Menampilkan Hari Lahir
# %A untuk nama hari lengkap
print(f"Harinya adalah \t   : {tanggal_lahir:%A}")

# 5. Mendapatkan Tanggal Hari Ini
hari_ini = dt.date.today()
print(f"Hari ini tanggal   : {hari_ini}")

# 6. Menghitung Umur
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30 # Perkiraan bulan sisa

# 7. Menampilkan Hasil Perhitungan Umur
print(f"Umur Anda adalah   : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
