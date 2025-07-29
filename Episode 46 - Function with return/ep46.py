# Function With Return

'''
Fungsi dengan nilai kembalian dalam pemrograman berfungsi untuk memberikan output dari
hasil fungsinya.

Kalo dalam fungsi matematika :
        y = f(x)
          ^ ^ ^
  output__| | |_____ input
            |_____ nama fungsi

Kita mengetahui bahwa struktur dalam bahasa python sebagai contoh berikut:
def nama_fungsi (input):
    hasil = assignment
    return hasil   ------> nilai dari hasil akan mengeluarkan nilai output

y = nama_fungsi (x)

Jika kita lihat struktur dari bahas python dengan fungsi matematika sama, sudah memiliki 
input, fungsi dan output. Jadi, dari contoh tersebut nilai y akan mendapatkan hasil outputan
dari proses nama_fungsi.

===============================
|  input -> fungsi -> output  |
===============================
'''
# Contoh Program Single Input

def fungsi_pangkat(a):
    nilai_a = a
    perpangkatan = nilai_a**2
    return perpangkatan

y = fungsi_pangkat(5)

print(y)  # hasilnya dari input fungsi_pangkat akan dipangkatkan, di dapat dari output nilai return perpangkatan
          # ke dalam nilai y.

print(fungsi_pangkat(7))  # Bisa memanggil fungsi dengan bentuk seperti ini


# Contoh multi input

def multi_masukan(masukan_01,masukan_02):
    return masukan_01 * masukan_02        # Bisa tanpa membuat variable baru

b = multi_masukan(8,9)
print(b)

# Contoh dengan fungsi return banyak

def operasi_matematika(angka_01,angka_02):
    tambah = angka_01 + angka_02
    kurang = angka_01 - angka_02
    kali = angka_01 * angka_02
    bagi = angka_01 + angka_02

    return tambah,kurang,kali,bagi

o,p,q,r = operasi_matematika(9,5)   # nilai dari o,p,q,r akan urut dengan nilai return dari fungsi operasi_matematika

print(f"Hasil tambah = {o}")
print(f"Hasil kurang = {p}")
print(f"Hasil kali = {q}")
print(f"Hasil bagi = {r}")