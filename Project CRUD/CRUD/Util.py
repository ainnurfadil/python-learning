# Untuk menambahkan fungsi tambahan

import random
import string

def random_string(panjang:int) -> str:
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))     
    return hasil_string

# dalam fungsi ini, yaga ada tanda petik berfungsi untuk separatornya, karena tidak ada berarti hasilnya akan menyambung
# random.choice() untuk memilih character yang di gunakan
# for i in range(panjang) untuk menentukan panjang dari nilai random nya