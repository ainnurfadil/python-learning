# Default argument

'''
Argument, input atau parameter yang memiliki nilai bawaannya.
strukturnya sebgai berikut:
def nama_fungsi(argument = nilai_defaultnya)
'''
def say_hello(nama="Asep"):     # Memiliki nilai argument defaultnya 
    print(f"Hallo {nama}")

say_hello("Ucup")       # Nilai Argument default dari 
say_hello()             # Nilai Argument tidak akan di ganti karena nilai nya kosong, jadi akan dipakai nilai default nya.

# Contoh 1
def hitung_pangkat(angka,pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2))    # Argument yang ini akan terbaca untuk argument yang pertama, dan yang ke 2 berhubung ada nilainya tidak akan terjadi error

hasil = hitung_pangkat(pangkat=3,angka=2)   # Pemanggilan Argument bisa di switch dan akan menyesuaikan argument yang ada di dalam fugnsi
print(hasil)

# Contoh 2
def fungsi(input1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

# print(fungsi())     # Fungsi print ini akan error, karena argument yanga ada di dalam fungsi 'fungsi', ada yang memerlukan inputan
print(fungsi(1,input4=7))