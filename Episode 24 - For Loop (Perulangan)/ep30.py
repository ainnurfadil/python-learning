data = ["Ucup", "Otong", "Dudung", "Ujang", "Asep", "Jajang"]
print(f"Data awal: {data}")

# 1. Mengambil Data dari List (Indexing)
print("\n--- Mengambil Data (Indexing) ---")
data_pertama = data[0]
print(f"Data pertama (index 0) = {data_pertama}")

data_terakhir = data[-1]
print(f"Data terakhir (index -1) = {data_terakhir}")

data_ketiga = data[2]
print(f"Data ketiga (index 2) = {data_ketiga}")

# 2. Mengambil Informasi Jumlah Data dalam List (len())
print("\n--- Jumlah Data (len()) ---")
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

# 3. Manipulasi Data List
print("\n--- Manipulasi Data ---")

# a. Menambahkan Item pada List Sesuai Posisi (insert)
print(f"Data sebelum insert = {data}")
data.insert(1, "Mario") # Menambahkan "Mario" di indeks ke-1
print(f"Data sesudah insert 'Mario' di index 1 = {data}")

# b. Menambah Item di Akhir List (append)
data.append("Faqih") # Menambahkan "Faqih" di akhir list
print(f"Data sesudah append 'Faqih' = {data}")

# c. Menambahkan List dengan List (extend)
data_tambahan = ["Gilang", "Reza", "Dani"]
data.extend(data_tambahan) # Menggabungkan data_tambahan ke data
print(f"Data sesudah extend = {data}")

# d. Merubah Data (Mengganti Item)
data[0] = "Ucup si Ganteng" # Mengubah elemen di indeks 0
print(f"Data sesudah rubah index 0 = {data}")

# e. Menghilangkan Data (remove)
data.remove("Mario") # Menghapus item "Mario"
print(f"Data sesudah remove 'Mario' = {data}")

# f. Menghapus Data Paling Belakang (pop)
data_akhir_dihapus = data.pop() # Menghapus dan mengambil item terakhir
print(f"Data akhir yang dihapus oleh pop: {data_akhir_dihapus}")
print(f"Data setelah pop = {data}")