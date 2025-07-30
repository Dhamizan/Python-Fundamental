import datetime

data_waktu = datetime.datetime.today()
print(data_waktu)
print(f"Tahun: {data_waktu.year}")
print(f"Bulan: {data_waktu.month}")
print(f"Tanggal: {data_waktu.day}")
print(f"Hari: {data_waktu.strftime('%A')}")

# Kalau Mau Indonesia
hari = {
    "Monday" : "Senin",
    "Tuesday" : "Selasa",
    "Wednesday" : "Rabu",
    "Thursday" : "Kamis",
    "Friday" : "Jumat",
    "Saturday" : "Sabtu",
    "Sunday" : "Minggu"
}

hari_inggris = data_waktu.strftime('%A')
print(f"Hari Indonesia: {hari[hari_inggris]}")