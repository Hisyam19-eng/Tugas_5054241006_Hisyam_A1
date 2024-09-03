# program toilet
populasi = int(input("Masukkan Jumlah Orang"))
toilet = populasi//3
flush_lama = 15
flush_baru = 2
flus_perhari = 2
cost_toilet_baru = toilet*150
#menghitung selisih toilet lama dan baru

hemat = (flush_lama-flush_baru)*14*toilet

print("total hemat air :",hemat)
print("total pasang toilet baru :",cost_toilet_baru)
