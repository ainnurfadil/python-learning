# 1. Contoh Infinite Loop (Loop Tak Terbatas) - DEMO
print("\n--- Contoh Infinite Loop (Jangan Dijalankan Tanpa Penghenti Manual) ---")
# angka_infinite = 10
# while angka_infinite > 5: # Kondisi ini akan selalu True
#     print("Faqihza kece")
# print("cukup")
# (Kode ini di-comment agar tidak berjalan tak terbatas secara otomatis)

# 2. Contoh While Loop yang Benar (dengan Kondisi Berhenti)
print("\n--- While Loop yang Benar ---")
angka = 0
print(f"Angka awal: {angka}")
while angka < 5:
    angka += 1 # Mengincrement angka agar kondisi bisa False
    print(f"Angka sekarang adalah: {angka}")
    print("Otong ganteng maksimal")
print("Cukup")