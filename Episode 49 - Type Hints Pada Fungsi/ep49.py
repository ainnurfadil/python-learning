# Type Hints

'''
Berguna untuk memberikan informasi pad fungsi yang telah di buat.
sebagai contoh untuk memberikan informasi dari fungsi yang sudah dibuat, 
akan menghasilkan output type data apa ketika fungsi tersebut digunakan dan 
juga user bisa menginput nilai menggunakan type data apa saja.

Akan sangat berguna ketika sudah memproduksi program dalam sekala besar.
'''

'''
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi('Ucup') # Dalam hal ini, nilai ucup tidak akan bisa di eksekusi, fungsi hint inilah yang diperlukan untuk memberitahu programer untuk memberikan inputan type data apa.
fungsi(True)
'''
import string

def fungsi_dengan_hints(argument:int=2) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

hasil = fungsi_dengan_hints()   # Ketika cursor di hover ke fungsinya, akan muncul hints popup yang akan muncul memberikan informasi tentang fungsinya
print(hasil)

# Contoh lain

def tampilan(argument:string): # Kita bisa memberitahu bahwa fungsi ini tidak memiliki return value dengan tidak memberikan detail tanda panah di akhir fungsi
    print(argument)

tampilan("Wahid")

# Contoh lain

import os

hasil = os.system("cls")
''' 
Jika kita hover cursor ke fungsi system(), ternyata memiliki nilai output bertype data
integer. jadi kita bisa membuktikan hasil dari nilainya berapa dengan memanggilnya
menggunakan print().
'''
print(hasil)