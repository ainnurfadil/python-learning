data_awal = ["Ucup", "Otong", "Dudung"]
print(f"Data Awal = {data_awal}")

# 1. Penyalinan Langsung (Pass by Reference)
print("\n--- Penyalinan Langsung (Referensial) ---")
A = data_awal
print(f"A = {A}")
print(f"Address Data Awal = {hex(id(data_awal))}")
print(f"Address A         = {hex(id(A))}")

# Perubahan pada A mempengaruhi data_awal
A[1] = "Michael"
print(f"Setelah A[1] diubah jadi 'Michael':")
print(f"Data Awal = {data_awal}")
print(f"A         = {A}")

# 2. Menyalin dengan Metode .copy() (Shallow Copy)
print("\n--- Menyalin dengan .copy() (Shallow Copy) ---")
B = data_awal.copy()
print(f"B = {B}")
print(f"Address Data Awal = {hex(id(data_awal))}")
print(f"Address B         = {hex(id(B))}")

# Perubahan pada B tidak mempengaruhi data_awal
B[0] = "Dadang"
print(f"Setelah B[0] diubah jadi 'Dadang':")
print(f"Data Awal = {data_awal}")
print(f"B         = {B}")

# Perubahan pada data_awal tidak mempengaruhi B (setelah copy)
data_awal[2] = "Jajang"
print(f"Setelah Data Awal[2] diubah jadi 'Jajang':")
print(f"Data Awal = {data_awal}")
print(f"B         = {B}")
