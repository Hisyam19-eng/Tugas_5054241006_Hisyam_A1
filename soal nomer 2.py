#menghitung usaha debit bendungan air
air = float(input("Masukkan volume air yang masuk : "))
tinggi = float(input("Masukkan tinggi bendungan : "))
gravitasi = 9.8
efisiensi = 0.9
megawatt = 1e6

power = air*tinggi*gravitasi*efisiensi
print (power)