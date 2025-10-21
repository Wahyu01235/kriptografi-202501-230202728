# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)
Nama: Achmad Wahyudi 
NIM: 230202728
Kelas: 5IKRA


---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).  
2. Menggambarkan proses enkripsi dan dekripsi sederhana.  
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).  

---

## 2. Dasar Teori
Sebuah kriptosistem adalah kerangka kerja lengkap yang digunakan untuk mengamankan data, terdiri dari lima komponen inti: plaintext (pesan asli yang dapat dibaca), ciphertext (pesan tersandi yang acak), algoritma enkripsi, algoritma dekripsi, dan kunci. Proses utamanya, enkripsi, adalah mengubah plaintext menjadi ciphertext menggunakan algoritma dan sebuah kunci. Sementara dekripsi adalah proses kebalikannya, yakni mengubah ciphertext kembali menjadi plaintext menggunakan algoritma dan kunci yang sesuai, sehingga hanya penerima yang sah yang dapat membaca pesan tersebut.

Berdasarkan manajemen kuncinya, kriptosistem terbagi dua: Simetris dan Asimetris. Kriptografi Simetris (seperti AES atau DES) menggunakan satu kunci rahasia yang sama untuk enkripsi dan dekripsi; metode ini sangat cepat namun memiliki kelemahan dalam distribusi kunci yang aman. Sebaliknya, Kriptografi Asimetris (seperti RSA atau ECC) menggunakan sepasang kunci (kunci publik dan kunci privat); kunci publik digunakan untuk mengenkripsi dan dapat dibagikan secara bebas, sementara hanya pemilik kunci privat yang dapat mendekripsinya. Sistem asimetris ini memecahkan masalah distribusi kunci, meskipun prosesnya lebih lambat secara komputasi.

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
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def _transform(text, key, direction):
    """
    Fungsi inti untuk menggeser karakter.
    direction=1 untuk enkripsi, direction=-1 untuk dekripsi.
    """
    output_chars = []
    for char in text:
        if char.isalpha():
            # Tentukan basis (65 untuk 'A', 97 untuk 'a')
            base = 65 if char.isupper() else 97
            
            # Hitung pergeseran
            # 1. Ubah ke 0-25 (ord(char) - base)
            # 2. Terapkan pergeseran ( ... + (key * direction))
            # 3. Modulo 26 untuk wrap-around
            # 4. Kembalikan ke nilai ASCII ( ... + base)
            new_ord = ((ord(char) - base + (key * direction)) % 26) + base
            output_chars.append(chr(new_ord))
        else:
            # Jika bukan alfabet, tambahkan karakter asli
            output_chars.append(char)
            
    # Gabungkan semua karakter dalam list menjadi satu string
    return "".join(output_chars)

def encrypt(plaintext, key):
    """
    Enkripsi plaintext menggunakan pergeseran positif.
    """
    return _transform(plaintext, key, 1)

def decrypt(ciphertext, key):
    """
    Dekripsi ciphertext menggunakan pergeseran negatif.
    """
    return _transform(ciphertext, key, -1)

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    # Nilai-nilai ini dijaga agar keluaran tetap sama
    message = "<nim><nama>"
    key = 5

    # Panggil fungsi enkripsi dan dekripsi
    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    # Mencetak hasil ke konsol menggunakan format yang berbeda (f-string)
    # namun menghasilkan teks yang identik.
    print(f"Plaintext : {message}")
    print(f"Ciphertext: {enc}")
    print(f"Decrypted : {dec}")

if __name__ == "__main__":
    main()

---

## 6. Hasil dan Pembahasan
Diagram
+-----------+
| Plaintext |
+-----------+
      |
      v
+-----------------------+
|   Algoritma Enkripsi  |
|         +             |
|       Kunci           |
+-----------------------+
      |
      v
+------------+
| Ciphertext |
+------------+
      |
      v
+-----------------------+
|   Algoritma Dekripsi  |
|         +             |
|       Kunci           |
+-----------------------+
      |
      v
+-----------+
| Plaintext |
+-----------+
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

### Komponen Utama Kriptosistem

Sebuah kriptosistem terdiri dari lima komponen utama:
1.  **Plaintext (Pesan Asli):** Data atau pesan asli yang dapat dibaca dan dimengerti.
2.  **Ciphertext (Pesan Tersandi):** Data atau pesan setelah dienkripsi; tampak acak dan tidak dapat dibaca.
3.  **Algoritma Enkripsi:** Fungsi matematis atau aturan yang mengubah plaintext menjadi ciphertext.
4.  **Algoritma Dekripsi:** Fungsi matematis atau aturan kebalikan yang mengubah ciphertext kembali menjadi plaintext.
5.  **Kunci (Key):** Sebuah nilai (bisa berupa angka, kata, atau frasa) yang digunakan oleh algoritma enkripsi dan dekripsi. Keamanan kriptosistem modern bergantung pada kerahasiaan kuncinya, bukan algoritmanya.

### Perbedaan Kriptografi Simetris vs Asimetris

#### Kriptografi Simetris (Symmetric-Key Cryptography)
Kriptografi simetris menggunakan **satu kunci yang sama** untuk proses enkripsi dan dekripsi. Pengirim dan penerima harus memiliki dan menjaga kerahasiaan kunci yang sama ini.

* **Contoh Algoritma:** AES (Advanced Encryption Standard), DES (Data Encryption Standard), 3DES, RC4, Blowfish.
* **Analogi:** Kunci rumah. Anda menggunakan kunci yang sama untuk mengunci dan membuka pintu. Jika Anda ingin teman Anda masuk, Anda harus menduplikasi kunci itu dan memberikannya kepadanya.

#### Kriptografi Asimetris (Asymmetric-Key Cryptography)
Kriptografi asimetris menggunakan **sepasang kunci** yang berbeda namun terhubung secara matematis: **Kunci Publik (Public Key)** dan **Kunci Privat (Private Key)**.
* Kunci Publik boleh disebarluaskan ke siapa saja.
* Kunci Privat harus dijaga kerahasiaannya oleh pemiliknya.
* Pesan yang dienkripsi dengan Kunci Publik hanya bisa didekripsi dengan Kunci Privat pasangannya.

* **Contoh Algoritma:** RSA (Rivest-Shamir-Adleman), ECC (Elliptic Curve Cryptography), DSA (Digital Signature Algorithm).
* **Analogi:** Gembok dan Kunci Gembok. Anda menyebarkan gembok (Kunci Publik) ke semua orang. Siapa pun bisa menggunakannya untuk mengunci kotak. Tapi, hanya Anda yang memegang kunci gembok (Kunci Privat) yang bisa membukanya.

**1. Sebutkan komponen utama dalam sebuah kriptosistem.**
   Seperti yang telah dijelaskan di atas, lima komponen utamanya adalah:
   1.  Plaintext
   2.  Ciphertext
   3.  Algoritma Enkripsi
   4.  Algoritma Dekripsi
   5.  Kunci (atau sepasang kunci)

2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?

Kelebihan utama kriptografi simetris adalah kecepatannya yang superior, membuatnya sangat efisien untuk mengenkripsi volume data yang besar seperti file video atau database. Namun, kelemahan utamanya terletak pada "masalah distribusi kunci," yaitu kesulitan dalam membagikan kunci rahasia secara aman kepada semua pihak yang terlibat, dan juga tidak dapat digunakan untuk tanda tangan digital karena kunci enkripsi dan dekripsi yang sama.

Sebaliknya, kriptografi asimetris unggul dalam menyelesaikan masalah distribusi kunci karena menggunakan pasangan kunci publik dan privat, di mana kunci publik dapat dibagikan secara terbuka. Kelebihan lainnya adalah kemampuannya untuk memfasilitasi tanda tangan digital, yang memungkinkan pembuktian keaslian pengirim dan non-repudiasi. Namun, kelemahan mendasar dari kriptografi asimetris adalah kecepatan pemrosesannya yang jauh lebih lambat dan lebih intensif secara komputasi, membuatnya tidak efisien untuk mengenkripsi data dalam jumlah besar.

3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?**
   Masalah ini (dikenal sebagai *Key Distribution Problem*) muncul karena **pengirim dan penerima harus memiliki kunci rahasia yang identik** sebelum mereka dapat berkomunikasi dengan aman.

   Pertanyaannya adalah: *Bagaimana cara Anda mengirimkan kunci rahasia itu kepada penerima dengan aman?*
   * Jika Anda mengirim kunci melalui saluran komunikasi yang sama (misal: internet), musuh (penyadap) dapat menyadap kunci tersebut. Jika kunci bocor, seluruh sistem keamanan runtuh.
   * Anda tidak bisa mengenkripsi kuncinya, karena untuk mengenkripsi kunci, Anda butuh kunci lain (ini menjadi masalah "ayam dan telur").
   
   Inilah mengapa kriptografi asimetris diciptakan. Dalam praktiknya, sistem *hybrid* sering digunakan: Kriptografi **asimetris** dipakai untuk **mengenkripsi dan bertukar Kunci Sesi (Session Key) simetris** dengan aman. Setelah Kunci Sesi diterima, kedua belah pihak menggunakan kriptografi **simetris** (yang cepat) untuk mengenkripsi sisa data komunikasi mereka.

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa kriptosistem merupakan fondasi keamanan data yang esensial, berlandaskan pada proses enkripsi dan dekripsi menggunakan algoritma dan kunci. Pemahaman mengenai komponen dasar seperti plaintext, ciphertext, algoritma, dan kunci sangat penting untuk merancang dan menganalisis sistem keamanan informasi yang efektif.

Lebih lanjut, praktikum ini menegaskan perbedaan mendasar antara kriptografi simetris dan asimetris. Kriptografi simetris menawarkan efisiensi komputasi yang tinggi untuk data bervolume besar, namun menghadapi tantangan signifikan dalam distribusi kunci yang aman. Sebaliknya, kriptografi asimetris memecahkan masalah distribusi kunci dan mendukung tanda tangan digital, meskipun dengan biaya komputasi yang lebih tinggi. Integrasi kedua pendekatan ini, seringkali dalam bentuk sistem hibrida, menjadi solusi praktis untuk mencapai keseimbangan antara keamanan dan performa.
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
