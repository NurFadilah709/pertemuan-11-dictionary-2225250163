
# Latihan 3: Manipulasi Dictionary

mahasiswa = {
    "nama": "Nailah Nur Fadilah",
    "nilai": 85
}

# Menambahkan data kelas
mahasiswa["kelas"] = "A"

# Mengubah nilai mahasiswa
mahasiswa["nilai"] = 90

print("Data setelah ditambahkan dan diubah:")
print(mahasiswa)

# Menghapus data kelas
mahasiswa.pop("kelas")

print("Data setelah kelas dihapus:")
print(mahasiswa)
