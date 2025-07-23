import time
start_time = time.time() # menginisialisasi start time 

# cara kerja print dalam python
print("Hello")
print("World")
print("Hello World")

# comment untuk satu baris menggunakan "#"
""" Untuk comment multiline
menggunakan tanda petik tiga seperti comment ini"""

a = 10
print(a)

# untuk mencetak berapa lama waktu yang dibutuhkan untuk menjalankan program ini
print(time.time() - start_time, "detik")

# karena python adalah interpreted language
# program python bisa kita compile ke yang namanya bytecode
# cara mengkompile nya adalah dengan mencjalan kan command berikut ke terminal
# python3 -m py_compile (nama file).py
# secara default untuk filenya berada dalam folder __pycache__, dan ketika di running
# waktu menjalankannya lebih cepat

