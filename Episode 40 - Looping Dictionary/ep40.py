print("===== LOOPING DICTIONARY =====")

teman_teman = {
    "Cup": "Ucup Surucup",
    "Tong": "Otong Surotong",
    "Dung": "Dudung Surudung",
    "Sep": "Asep Sikasep",
    "Cuy": "Ucuy Surucuy"
}
print(f"Dictionary teman_teman: {teman_teman}")

# 1. Looping Dasar (Mengambil Keys)
print("\n--- Looping Dasar (Mengambil Keys) ---")
for key_teman in teman_teman:
    print(key_teman)

# 2. Mengambil Keys Secara Eksplisit (.keys())
print("\n--- Mengambil Keys Secara Eksplisit (.keys()) ---")
keys_obj = teman_teman.keys()
print(f"Object keys: {keys_obj}")
for key in teman_teman.keys():
    print(f"Key: {key}, Value: {teman_teman.get(key)}")

# 3. Mengambil Values Secara Eksplisit (.values())
print("\n--- Mengambil Values Secara Eksplisit (.values()) ---")
values_obj = teman_teman.values()
print(f"Object values: {values_obj}")
for value in teman_teman.values():
    print(f"Value: {value}")

# 4. Mengambil Pasangan Key-Value (.items())
print("\n--- Mengambil Pasangan Key-Value (.items()) ---")
items_obj = teman_teman.items()
print(f"Object items: {items_obj}")

print("\n--- Looping Items (sebagai tuple) ---")
for item in teman_teman.items():
    print(f"Item (tuple): {item}")

print("\n--- Looping Items (unpacking key, value) ---")
for key, value in teman_teman.items():
    print(f"Key = {key}, Value = {value}")