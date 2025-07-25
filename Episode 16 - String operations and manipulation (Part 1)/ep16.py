# Operasi dan Manipulasi String

# 1. Menyambung string (concatenate)
nama_pertama = "monkey"
nama_tengah = "D"
nama_akhir = "Lufy"

nama_lengkap = nama_pertama +" "+ nama_tengah +"'"+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)     # Menggunakan operator length
# print(type(panjang))          # bertype data integer
print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk String

## Mengecek apakah ada omponen char atau string di string yang terinput

a = "c" 
status = a in nama_lengkap  # Yang di cari adalah huruf c dalam variabel nama_lengkap
print("string " + a + " ada di "+ nama_lengkap + " = " + str(status)) # Hasilnya false karena tidak ada

a = "c"
status = a not in nama_lengkap  # Yang di cari adalah huruf c dalam variabel nama_lengkap
print("string " + a + " ada di "+ nama_lengkap + " = " + str(status)) # Hasilnya True karena memang tidak ada

## Menlipat gandakan string
print(25*'wk')
print(20*'wk')

## Indexing
print("index ke-0 dari nama lengkap: "+ nama_lengkap[0])
print("index ke-6 dari nama lengkap: "+ nama_lengkap[6])
print("index ke-(-1) dari nama lengkap: "+ nama_lengkap[-1])
print("index ke-(-5) dari nama lengkap: "+ nama_lengkap[-5])
print("index dari 0 - 3 dari nama lengkap: "+ nama_lengkap[0:4]) # Disini kenapa 4, karena di dalam python index terakhir di abaikan
print("index dari setiap naik 2 huruf dari nama lengkap: "+ nama_lengkap[0:10:2]) # Disini cara baca indexing nya [index_pertama:index terakhir:increment/lompatan]

## Mencari Item paling kecil berdasarkan nomor order ASCII Code
print("paling kecil : " + min(nama_lengkap))

## Mencari Item paling besar berdasarkan nomor order ASCII Code
print("paling kecil : " + max(nama_lengkap))

### Untuk mencari dan melihat order ASCII code
ascii_code = ord(" ")   # Untuk mengassign nomor order space
print("ASCII code untuk space adalah "+ str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah" + chr(data))

# 4. Operator dalam bentuk method

data = "Aqua 100 persen Murni"
jumlah = data.count("a")
print("Jumlah a pada " + data + " = " + str(jumlah)) # Terhitung satu karena untuk character 'a' hanya ada satu.