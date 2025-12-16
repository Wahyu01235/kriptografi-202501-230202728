# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange  
Nama: Achmad Wahyudi  
NIM: 230202728  
Kelas: 5IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie-Hellman Key Exchange (DHKE) adalah protokol kriptografi kunci publik yang memungkinkan dua pihak untuk menyepakati sebuah kunci rahasia bersama (shared secret key) melalui saluran komunikasi yang tidak aman tanpa perlu bertemu sebelumnya. Protokol ini menjadi fondasi bagi keamanan jaringan modern karena memecahkan masalah distribusi kunci yang krusial dalam komunikasi data. Dalam implementasinya, kedua pihak menyepakati parameter publik berupa bilangan prima besar p dan generator g, lalu masing-masing membangkitkan kunci privat acak. Kunci privat ini tidak pernah dikirimkan melalui jaringan; sebaliknya, turunan matematisnya (kunci publik) yang dipertukarkan. Nilai kunci rahasia bersama kemudian dihitung secara independen oleh masing-masing pihak menggunakan kunci privat mereka sendiri dan kunci publik lawan, menghasilkan nilai yang identik untuk digunakan dalam enkripsi simetris selanjutnya.

Keamanan algoritma Diffie-Hellman bersandar pada kesulitan komputasi dari masalah logaritma diskrit (Discrete Logarithm Problem - DLP) dalam aritmatika modular. Secara matematis, jika diketahui g, p, dan A = g^a (mod p), sangat mudah untuk menghitung A jika a diketahui. Namun, sebaliknya, sangat sulit secara komputasi untuk mencari nilai a (kunci privat) hanya dengan mengetahui A, g, dan p, terutama jika p adalah bilangan prima yang sangat besar (misalnya 2048-bit atau lebih). Hal ini memastikan bahwa meskipun penyerang menyadap kunci publik yang dipertukarkan (A dan B), mereka tidak dapat merekonstruksi kunci rahasia bersama (s = g^ab (mod p)) dalam waktu yang wajar menggunakan teknologi komputasi saat ini.

Meskipun kuat terhadap serangan pasif, implementasi dasar Diffie-Hellman rentan terhadap serangan aktif seperti Man-in-the-Middle (MitM) karena tidak menyediakan mekanisme autentikasi identitas. Penyerang dapat mencegat pertukaran kunci dan menyamar sebagai pihak yang sah. Oleh karena itu, dalam standar keamanan terkini, DHKE jarang digunakan secara berdiri sendiri; ia digabungkan dengan algoritma tanda tangan digital atau infrastruktur kunci publik (PKI) untuk memverifikasi identitas, seperti pada protokol TLS 1.3. Selain itu, riset terbaru di tahun 2023 dan 2024 banyak berfokus pada varian Elliptic Curve Diffie-Hellman (ECDH) yang lebih efisien untuk perangkat Internet of Things (IoT) serta pengembangan algoritma yang tahan terhadap ancaman komputasi kuantum (post-quantum cryptography).

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
1. Simulasi Diffie-Hellman
2. Analisis Serangan MITM (Man-in-the-Middle)

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
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Diffie-Hellman memungkinkan dua pihak untuk menghasilkan shared secret (rahasia bersama) di saluran yang tidak aman karena keamanan protokol ini didasarkan pada kesulitan komputasi masalah matematika satu arah, khususnya Masalah Logaritma Diskrit (Discrete Logarithm Problem atau DLP).
Menurut Stallings (2022), meskipun penyerang menyadap nilai g (generator), p (bilangan prima), dan kunci publik (A dan B), penyerang tidak dapat membalikkan proses perhitungan untuk menemukan kunci privat (a atau b) dalam waktu yang wajar. Hal ini karena fungsi eksponensial modular (g^x (mod p)) mudah dihitung satu arah, tetapi sangat sulit dibalikkan (mencari x) jika angkanya sangat besar.
Hal ini juga ditegaskan dalam buku Jamaludin, dkk. (2022) yang menjelaskan bahwa kekuatan algoritma ini terletak pada kompleksitas faktorisasi bilangan besar dalam aritmatika modular, yang membuat kunci privat tetap aman meskipun kunci publik dipertukarkan secara terbuka.

2. Apa kelemahan utama protokol Diffie-Hellman murni?
Kelemahan paling fundamental dari protokol Diffie-Hellman "murni" atau dasar adalah tidak adanya autentikasi (ketiadaan verifikasi identitas). Saepulrohman & Negara (2021) dalam analisis keamanannya menyoroti bahwa protokol dasar hanya menjamin bahwa dua pihak memiliki kunci yang sama, tetapi tidak menjamin siapa pihak di ujung sana. Alice tahu dia berbagi kunci dengan seseorang, tetapi dia tidak bisa memastikan apakah itu Bob atau penyerang.
Celah ini membuka peluang serangan Man-in-the-Middle (MitM), di mana penyerang mencegat komunikasi dan menyamar sebagai pihak yang sah. Stallings (2022) juga menyebutkan bahwa tanpa identitas yang terverifikasi, protokol ini rentan terhadap penyadapan aktif (active eavesdropping).

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
Untuk mencegah serangan Man-in-the-Middle (MitM), protokol Diffie-Hellman harus digabungkan dengan mekanisme autentikasi sebelum atau selama proses pertukaran kunci. Cara yang paling umum adalah menggunakan Tanda Tangan Digital (Digital Signatures) atau Sertifikat Digital.
Berdasarkan Musa (2023), penggunaan sertifikat digital (seperti dalam infrastruktur PKI) memungkinkan Alice memverifikasi bahwa kunci publik yang dia terima benar-benar milik Bob yang sah, bukan milik penyerang.
Dalam Tanksale (2024), dijelaskan bahwa pada perangkat modern (seperti IoT), implementasi Diffie-Hellman sering kali menggunakan varian Authenticated Key Exchange (seperti protokol Station-to-Station atau ECDH yang diautentikasi) di mana kunci publik ditandatangani secara digital untuk menjamin integritas dan keaslian pengirim.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
-Stallings, W. (2022). Cryptography and Network Security: Principles and Practice (Global Edition). Pearson.
-Jamaludin, Arizal, Mardalius, & Pakpahan, A. F. (2022). Kriptografi: Teknik Keamanan Data. Yayasan Kita Menulis.
-Tanksale, V. (2024). Efficient Elliptic Curve Diffie–Hellman Key Exchange for Resource-Constrained IoT Devices. Electronics, 13(18), 3631.
-Musa, S. M. (2023). Network Security and Cryptography: A Self-Teaching Introduction (2nd ed.). Mercury Learning and Information.
-Saepulrohman, A., & Negara, R. M. (2021). Security Analysis of Diffie-Hellman Algorithm in Cryptographic Key Exchange. Jurnal Teknik Informatika (JUTI), 19(2).
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
