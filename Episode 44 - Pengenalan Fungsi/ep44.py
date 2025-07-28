# Pengenalan Fungsi

# Dalam pemograman terkadang perlu membuat fungsi supaya tidak mengulang 
# proses yang sama. Sebutannya bisa disebut method, sub rutin atau rutin.

# Langkah awal yang harus dilakukan adalah mendefinisikan fungsinya.

def halo_world():
    '''fungsi yang dibuat untuk menampilakn hello world'''
    print("Hello world")
    print("Hello world2")
    print("Hello world3")

print("hello world ini berada di luar 'def'")
print("hello world ini berada di luar 'def'")
print("hello world ini berada di luar 'def'")

halo_world()

# fungsi()    # pemangglan fungsi harus setelah fungsi terdefinisikan, disini akan terjadi error karena fungsinya berada setelah baris ini

def fungsi():
    print('ini adalah fungsi')

fungsi()