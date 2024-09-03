#ngitung Taxi
ordometer_awal =float(input("Masukkan Meter Awal"))
ordometer_akhir = float(input("Masukkan Meter Akhir"))
#menghitung jarak
jarak = round(ordometer_akhir - ordometer_awal,1)
print(jarak*1.5)
tarif = round(jarak*1.5,2)
print("Jarak Yang Ditempuh ",jarak,"Tarif",tarif)