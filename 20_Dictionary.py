# Data Dictionary

# Data Dictionary Standar
data_dict = {"nama": "Dio",
             "umur": 20,
             "kampus": "IPB"}

print(data_dict)
print(data_dict["nama"])

# Multikey Dictionary

mahasiswa_1 = {
    "nama": "Dio",
    "umur": 20,
    "kampus": "IPB",
    "jurusan": "Teknik Informatika",
}

mahasiswa_2 = {
    "nama" : "Thariq",
    "umur": 21,
    "kampus": "IPB",
    "jurusan": "Teknik Informatika",
}

mahasiswa_3 = {
    "nama": "Rizki",
    "umur": 22,
    "kampus": "IPB",
    "jurusan": "Teknik Informatika",
}

daftar_mahasiswa = {
    "mhs1" : mahasiswa_1,
    "mhs2" : mahasiswa_2,
    "mhs3" : mahasiswa_3
}

print(daftar_mahasiswa)
print(f"{"ID":<6} {"Nama":<10} {"Umur":<3} {"Kampus":^9} {"Jurusan":<10}")
for mahasiswa in daftar_mahasiswa:
    KEY = mahasiswa
    
    NAMA = daftar_mahasiswa[KEY]['nama']
    UMUR = daftar_mahasiswa[KEY]['umur']
    KAMPUS = daftar_mahasiswa[KEY]['kampus']
    JURUSAN = daftar_mahasiswa[KEY]['jurusan']
    
    print(f"{KEY:<6} {NAMA:<10} {UMUR:<3} {KAMPUS:^9} {JURUSAN:<10}")