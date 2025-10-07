# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: Week1-Intro-CIA  
Nama: Achmad Wahyudi  
NIM: 230202728  
Kelas: 5IKRA  

---

## 1. Tujuan
Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
Kriptografi adalah seni atau ilmu yang mempelajari bahasa pengkodean untuk menjaga kerahasiaan suatu pesan. Istilah ini berasal dari Yunani yaitu "kryptos" (tersembunyi) dan "graphein" (menulis). Plaintext (naskah asli) kemudian diubah menjadi ciphertext (naskah yang formatnya diubah dengan pengkodean tertentu agar tidak dapat dibaca pihak lain). Proses pengubahan ini disebut dengan enkripsi. Sementara kelbalikannya atau mengubah ciphertext menjadi plaintext disebut sebagai dekripsi. Kedua proses ini memerlukan kunci unruk dapat melakukan enkripsi dan dekripsi. kunci ini berisi algoritma bagaimana pengkodean dibuat.

Kriptografi dimulai sejak era klasik dengan teknik yang masih sederhana. Seperti teknik skitala sparta yang digunakan bangsa sparta dengan tongkat berdiameter sama, kemusia teknis ceaesar cipher dengan menggeser huruf alfabet. pekembangan berikutnya terjadi pada kemunculkan mesin enigma pada masa penrang dunia II, dengan teknologi yang komplesks dimasanya. Memasuki era kontemporer, kriptografi telah bertransformasi melalui kehadiran algoritma-algoritma canggih seperti RSA dan AES, yang kini menjadi pilar utama dalam mengamankan infrastruktur dan aktivitas digital modern.

Prinsip-prinsip dalam kriptografi sangat menekankan keamaanan informasi. Prinsip ini beruapa:
- Kerahasiaan (Confidentiality): Menjamin bahwa informasi hanya dapat diakses oleh pihak yang memiliki wewenang atau kunci yang tepat. Ini adalah fungsi paling dasar dari enkripsi untuk mencegah penyadapan.
- Integritas (Integrity): Memastikan bahwa pesan atau data tidak mengalami perubahan, baik disengaja maupun tidak, selama proses transmisi dari pengirim ke penerima.
- Otentikasi (Authentication): Memastikan dan memverifikasi identitas asli dari pengirim dan penerima pesan, sehingga mencegah peniruan atau pemalsuan identitas.
Ketiga prinsip ini, sering disebut sebagai bagian dari pilar utama keamanan siber, menjadi fondasi dalam merancang sistem keamanan yang efektif.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Meskipun tidak ada satu nama tunggal, Claude Shannon sering dianggap sebagai "bapak kriptografi modern" karena karyanya yang meletakkan fondasi matematis dan ilmiah untuk bidang ini. Namun, era modern tidak akan lengkap tanpa kontribusi revolusioner dari Whitfield Diffie dan Martin Hellman. Mereka adalah penemu konsep kriptografi kunci publik, sebuah gagasan yang melahirkan metode pertukaran kunci Diffie-Hellman  dan menjadi dasar bagi sebagian besar sistem keamanan internet yang kita gunakan saat ini.
2. Beberapa algoritma kunci publik sangat populer dan vital untuk keamanan digital modern. Salah satu yang paling dikenal adalah RSA (Rivest-Shamir-Adleman), yang sering diandalkan untuk keperluan otentikasi dan pembuatan tanda tangan digital. Selain itu, terdapat ECC (Elliptic Curve Cryptography) yang efisien dan banyak digunakan untuk melindungi transaksi online. Ada pula protokol Diffie-Hellman Key Exchange, yang perannya sangat krusial dalam memungkinkan dua pihak untuk menyetujui sebuah kunci rahasia bersama melalui saluran komunikasi yang tidak aman.
3. MPerbedaan utama antara kriptografi klasik dan modern terletak pada kompleksitas metode dan basis keamanannya. Kriptografi klasik, seperti Caesar Cipher, bekerja pada level karakter dengan menggunakan teknik sederhana seperti pergeseran huruf (substitusi). Keamanannya seringkali bergantung pada kerahasiaan metode yang digunakan. Sebaliknya, kriptografi modern, seperti RSA dan AES, beroperasi pada level data biner dan didasarkan pada masalah matematika yang sangat kompleks. Keamanannya tidak lagi bergantung pada kerahasiaan algoritma, melainkan pada kerahasiaan kunci (key), yang membuatnya jauh lebih kuat dan tahan terhadap serangan komputasi.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
