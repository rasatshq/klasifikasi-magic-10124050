# Tugas P2 Representasi Data dan Prapemrosesan

Nama: Rashad Shaquille Taofik  
NIM: 10124050  
Kelas: IF2  
MK: Pembelajaran Mesin

## Isi dan ketentuan

Dataset tabular untuk klasifikasi gamma (g) dan hadron (h).
Dataset lampiran memiliki tepat 1.000 baris di luar header dan 10 calon fitur.
Label class tidak dihitung sebagai fitur. Tidak ada kolom ID atau nama pada
dataset masukan. row_id dan split pada hasil hanya informasi pendamping.

Sumber terbuka:
https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope

Sumber: Bock, R. (2004), MAGIC Gamma Telescope, UCI.
DOI: https://doi.org/10.24432/C52C8B
Data sumber berasal dari simulasi Monte Carlo oleh penyedia dataset.
Sampel 1.000 baris dipilih tanpa penggandaan sesudah deduplikasi sumber,
dengan stratifikasi kelas dan random_state=42.

## Menjalankan di Windows dan VS Code

1. Extract All paket ZIP.
2. Buka folder yang berisi klasifikasi_svm_1000.py melalui Open Folder.
3. Pilih Terminal > New Terminal.
4. Pasang pustaka:

```powershell
py -m pip install -r requirements.txt
```

5. Jalankan program:

```powershell
py klasifikasi_svm_1000.py
```

Jika py tidak dikenali, gunakan python sebagai penggantinya. Jika keduanya
tidak tersedia, pasang Python dahulu. Paket pustaka diverifikasi dengan
Python 3.12.14. Program membaca CSV lokal, bukan mengunduh ulang dataset.

Untuk menyimpan keluaran terminal:

```powershell
py klasifikasi_svm_1000.py > hasil_running.txt
```

## Urutan demo saat perkuliahan

1. Tunjukkan ukuran data: 1.000 baris dan 10 fitur ditambah label class.
2. Tunjukkan df.info() serta audit tipe kolom. Fitur float64, label string.
3. Tunjukkan missing values 0, duplikat sampel 0, serta label g dan h.
   Pembersihan spasi dan kapitalisasi tidak mengubah label karena sudah benar.
4. Jelaskan standardisasi dengan statistik data latih. Seperti menyamakan
   skala penggaris, tiap fitur diletakkan pada skala yang sebanding.
   Min-Max tidak digunakan; label tidak distandardisasi.
5. Tunjukkan 5 TERATAS dan 5 TERBAWAH hasil, yaitu row_id 0–4 dan 995–999.
   CSV hasil tetap memiliki 1.000 baris dan 10 fitur berakhiran _z.
6. Jelaskan pemeriksaan opsional: IQR, proporsi kelas, dan pencegahan leakage.
7. Jika diperlukan, tunjukkan evaluasi SVM: 800 baris latih, 200 baris uji,
   akurasi uji 85,50%. Model merupakan evaluasi tambahan untuk tugas P2.

## Berkas utama

- Laporan_Tugas_SVM_1000_Baris.docx: laporan lengkap sesuai urutan tugas.
- klasifikasi_svm_1000.py: program utama dan pemeriksaan prapemrosesan.
- dataset_magic_1000.csv: masukan 1.000 baris dengan 10 fitur dan satu label.
- dataset_magic_hasil_pemrosesan.csv: keluaran standardisasi 1.000 baris.
- audit_kolom.csv: tipe kolom awal/hasil, peran, dan jumlah nilai kosong.
- hasil_running.txt: keluaran lengkap program yang benar-benar dijalankan.
- Hasil_Running_1000.png: cuplikan visual keluaran aktual, bukan foto laptop.
- statistik_data_latih.csv: median, scaler, dan batas IQR data latih.
- prediksi_data_uji.csv dan hasil_evaluasi.json: hasil evaluasi tambahan.
- asal_baris_sampel.csv: penelusuran sampel ke indeks sumber, bukan fitur.
- requirements.txt: versi pustaka untuk reproduksi.
- siapkan_sampel.py: unduh ulang sumber dan buat sampel yang sama; opsional.

## Link data dan program untuk pengumpulan

Link data sumber UCI sudah tercantum di atas dan pada laporan.
Program disertakan di dalam ZIP. Untuk menyediakan link yang dapat dibuka
dosen, unggah ZIP ini ke Google Drive milikmu atau unggah kode dan dataset
ke repositori GitHub. Salin tautan berbagi yang sesuai, pastikan dosen
mempunyai akses, lalu tempel bersama link UCI pada pengumpulan LMS.
Jangan memakai path folder lokal atau tautan unduhan percakapan sebagai
pengganti tautan pengumpulan yang dapat diakses dosen.

Tidak diperlukan penambahan data buatan, kolom ID, atau fitur baru.
