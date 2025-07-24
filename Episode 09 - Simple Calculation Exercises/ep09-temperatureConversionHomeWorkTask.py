# Tugas Konversi suhu Fahrenheit ke Kelvin dan Kelvin ke Fahrenheit

print("\n FAHRENHEIT KE KELVIN \n")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit : "))

# Program konversi

kelvin = (fahrenheit + 459.67) * (5/9)
print("Suhu dalam kelvin : ", kelvin)


print("\n KELVIN KE FAHRENHEIT \n")

kelvin = float(input("Masukkan suhu dalam kelvin : "))

# Program konversi

fahrenheit = ((9/5) * kelvin) - 459.67
print("Suhu dalam fahrenheit : ", fahrenheit)