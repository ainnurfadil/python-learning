# Membuat operasi sederhana untuk mengkonversi suhu

print("\n TEMPERATUR CONVERTER \n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah", celcius, " Celcius")

# Konversi Celcius ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah: ",reamur, " Reamur")

# Konversi Celcius ke Kelvin
kelvin = 273.15 + celcius
print("Suhu dalam kelvin adalah: ",kelvin, " Kelvin")

# Konversi Celcius ke Fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print("Suhu dalam fahrenheit adalah: ", fahrenheit, " Fahrenheit")

