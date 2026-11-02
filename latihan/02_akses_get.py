
# Latihan 2: Mengakses Dictionary dengan get()

mahasiswa = {
    "nama": "Nailah Nur Fadilah",
    "nilai": 85
}

print("Nama:", mahasiswa.get("nama"))
print("Kelas:", mahasiswa.get("kelas", "Belum ada"))
