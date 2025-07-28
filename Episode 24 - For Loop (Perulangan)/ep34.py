# Import modul copy untuk deepcopy
from copy import deepcopy

# Data awal nested list
data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10] # Nested list dengan elemen non-list
print(f"Data 2D awal: {data_2D}")

# 1. Mengambil Data dari Nested List
print("\n--- Mengambil Data dari Nested List ---")
ambil_data_list_pertama = data_2D[0]
print(f"data_2D[0] = {ambil_data_list_pertama}")

ambil_elemen_pertama_dari_list_pertama = data_2D[0][0]
print(f"data_2D[0][0] = {ambil_elemen_pertama_dari_list_pertama}")

# 2. Shallow Copy (Menggunakan .copy()) - Review
print("\n--- Shallow Copy (.copy()) ---")
data_2D_shallow_copy = data_2D.copy()
print(f"Original: {data_2D}, Shallow Copy: {data_2D_shallow_copy}")

print(f"Address data_2D: {id(data_2D)}")
print(f"Address data_2D_shallow_copy: {id(data_2D_shallow_copy)}")
print(f"Address data_2D[0]: {id(data_2D[0])}")
print(f"Address data_2D_shallow_copy[0]: {id(data_2D_shallow_copy[0])}") # Sama!

# Mengubah elemen nested list pada shallow copy
data_2D_shallow_copy[0][0] = 500
print(f"\nSetelah data_2D_shallow_copy[0][0] diubah jadi 500:")
print(f"Original data_2D: {data_2D}") # Ikut berubah!
print(f"Shallow copy: {data_2D_shallow_copy}")

# Mengubah elemen non-list pada shallow copy
data_2D_shallow_copy[2] = 999
print(f"\nSetelah data_2D_shallow_copy[2] diubah jadi 999:")
print(f"Original data_2D: {data_2D}") # Tidak berubah (ini hanya untuk elemen non-list)
print(f"Shallow copy: {data_2D_shallow_copy}")

# 3. Deep Copy (Menggunakan modul copy)
print("\n--- Deep Copy (from copy import deepcopy) ---")
data_2D_deep_copy = deepcopy(data_2D) # Menggunakan deepcopy

print(f"Original: {data_2D}, Deep Copy: {data_2D_deep_copy}")
print(f"Address data_2D: {id(data_2D)}")
print(f"Address data_2D_deep_copy: {id(data_2D_deep_copy)}")
print(f"Address data_2D[0]: {id(data_2D[0])}")
print(f"Address data_2D_deep_copy[0]: {id(data_2D_deep_copy[0])}") # Berbeda!

# Mengubah elemen nested list pada deep copy
data_2D_deep_copy[0][0] = 777
print(f"\nSetelah data_2D_deep_copy[0][0] diubah jadi 777:")
print(f"Original data_2D: {data_2D}") # Tidak berubah!
print(f"Deep copy: {data_2D_deep_copy}")