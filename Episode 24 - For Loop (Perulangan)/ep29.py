# 1. Membuat List Dasar
print("\n--- Membuat List Dasar ---")
data_angka = [1, 5, 2, 3, 4, 6]
print(f"List Angka: {data_angka}")

data_string = ["ucup", "otong", "dadang"]
print(f"List String: {data_string}")

data_boolean = [True, False, True]
print(f"List Boolean: {data_boolean}")

data_campuran = [1, "ucup", True, "otong", 2, False]
print(f"List Campuran: {data_campuran}")

# 2. Cara Alternatif Membuat List
print("\n--- Cara Alternatif Membuat List ---")
data_range_obj = range(0, 10) # Membuat objek range
print(f"Objek Range(0,10): {data_range_obj}")

data_list_range = list(data_range_obj) # Konversi objek range ke list
print(f"List dari Range: {data_list_range}")

data_list_range_step = list(range(0, 10, 2)) # Range dengan step 2
print(f"List dari Range (step 2): {data_list_range_step}")

# 3. List Comprehension
print("\n--- List Comprehension ---")
list_pake_for = [i for i in range(0, 10)]
print(f"List Comprehension (sederhana): {list_pake_for}")

list_pake_for_kuadrat = [i**2 for i in range(0, 10)] # Kuadrat
print(f"List Comprehension (kuadrat): {list_pake_for_kuadrat}")

list_pake_for_pangkat_tiga = [i**3 for i in range(0, 10)] # Pangkat tiga
print(f"List Comprehension (pangkat tiga): {list_pake_for_pangkat_tiga}")

# 4. List Comprehension dengan Kondisi (if)
print("\n--- List Comprehension dengan Kondisi ---")
list_pake_for_if = [i for i in range(0, 10) if i != 5] # Hilangkan angka 5
print(f"List (kecuali 5): {list_pake_for_if}")

list_genap = [i for i in range(0, 10) if i % 2 == 0] # Bilangan genap
print(f"List Genap: {list_genap}")

list_ganjil = [i for i in range(0, 10) if i % 2 != 0] # Bilangan ganjil
print(f"List Ganjil: {list_ganjil}")

list_ganjil_kuadrat = [i**2 for i in range(0, 10) if i % 2 != 0] # Kuadrat bilangan ganjil
print(f"List Ganjil Kuadrat: {list_ganjil_kuadrat}")