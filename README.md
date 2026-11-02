
# Pertemuan 11 - Dictionary/Map

## Identitas Mahasiswa

- Nama: Nailah Nur Fadilah
- NIM: 2225250163
- Kelas: 3E

## Tujuan Pembelajaran

1. Memahami konsep dictionary dalam Python.
2. Memahami penggunaan key dan value.
3. Mampu mengakses dan memanipulasi data dictionary.
4. Mampu menggunakan perulangan untuk menampilkan isi dictionary.
5. Mampu membuat dictionary bersarang.
6. Mampu menggunakan fungsi untuk mengolah data dictionary.

## Struktur Data

Dictionary merupakan struktur data Python yang menyimpan pasangan key dan value.

- Key digunakan sebagai kunci untuk mengakses data.
- Value merupakan nilai yang disimpan pada setiap key.

Pada tugas ini, NIM digunakan sebagai key untuk menyimpan data mahasiswa. Setiap mahasiswa memiliki data nama, kelas, dan nilai.

## Cara Menjalankan Program

Buka terminal VS Code, kemudian jalankan perintah:

```bash
python praktik/data_mahasiswa.py
```

## Test Case

| No | Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditemukan | Berhasil |
| 2 | Mencari NIM A999 | Data tidak ditemukan | Berhasil |
| 3 | Menambahkan NIM A006 | Data Fajar berhasil ditambahkan | Berhasil |
| 4 | Mengubah nilai A002 | Nilai berubah menjadi 82 | Berhasil |
| 5 | Menampilkan seluruh data | Semua data mahasiswa tampil | Berhasil |
| 6 | Menghitung rata-rata | Rata-rata 83.50 | Berhasil |

## Refleksi

Kesalahan yang dapat terjadi ketika mengakses dictionary adalah KeyError. Kesalahan ini muncul ketika program mencoba mengambil key yang tidak tersedia menggunakan tanda kurung siku.

Cara mengatasinya adalah menggunakan method get() agar program dapat memberikan nilai alternatif ketika key tidak ditemukan. Dengan demikian, program dapat berjalan lebih aman dan tidak langsung mengalami error.
