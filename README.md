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

## Cara Clone dan Menjalankan Program

### 1. Clone Repositori dari GitHub

Buka terminal (Git Bash, Command Prompt, atau PowerShell) lalu jalankan perintah berikut:

```bash
git clone https://github.com/rasatshq/klasifikasi-magic-10124050.git
cd klasifikasi-magic-10124050
```

*(Atau jika menggunakan berkas ZIP, ekstrak paket ZIP dan buka foldernya di VS Code melalui menu **File > Open Folder**).*

### 2. (Opsional) Buat dan Aktifkan Virtual Environment

Disarankan membuat lingkungan virtual Python agar dependensi terisolasi:

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Pasang Pustaka / Dependensi

Pastikan pustaka pendukung terpasang dari `requirements.txt`:

```powershell
pip install -r requirements.txt
# atau di Windows jika menggunakan python launcher:
py -m pip install -r requirements.txt
```

### 4. Jalankan Program

Jalankan skrip klasifikasi SVM utama:

```powershell
python klasifikasi_svm_1000.py
# atau:
py klasifikasi_svm_1000.py
```

Untuk menyimpan seluruh keluaran terminal langsung ke dalam berkas teks:

```powershell
python klasifikasi_svm_1000.py > hasil_running.txt
```

> **Catatan:**
> - Jika perintah `py` tidak dikenali, gunakan `python` (atau sebaliknya).
> - Paket pustaka telah diverifikasi berjalan dengan Python 3.12.x.
> - Program membaca berkas CSV lokal (`dataset_magic_1000.csv`) yang telah disediakan di repositori, sehingga tidak memerlukan koneksi internet untuk mengunduh ulang dataset saat dijalankan.

### 5. Melakukan Push Kembali ke GitHub (Jika Ada Perubahan)

Jika Anda melakukan modifikasi atau pembaruan berkas dan ingin menyimpannya kembali ke repositori GitHub:

```bash
git add .
git commit -m "Deskripsi perubahan yang dilakukan"
git push origin main
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

- **Dataset Sumber (UCI)**: https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope
- **Repositori GitHub Program & Data**: https://github.com/rasatshq/klasifikasi-magic-10124050

Seluruh kode program, dataset hasil prapemrosesan, dan berkas analisis telah di-push ke repositori GitHub di atas. Tautan repositori GitHub ini dapat langsung digunakan dan diserahkan bersama tautan sumber UCI untuk pengumpulan pada LMS.

Tidak diperlukan penambahan data buatan, kolom ID, atau fitur baru.
