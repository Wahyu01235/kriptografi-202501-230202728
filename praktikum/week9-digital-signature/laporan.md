# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: Digital Signature (RSA/DSA)  
Nama: Achmad Wahyudi  
NIM: 230202728  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
2. Memverifikasi keaslian tanda tangan digital.  
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.  
---

## 2. Dasar Teori
Digital Signature atau Tanda Tangan Digital adalah mekanisme kriptografi yang berfungsi sebagai ekuivalen digital dari tanda tangan basah atau stempel fisik, namun dengan tingkat keamanan yang jauh lebih tinggi. Mekanisme ini menggunakan prinsip kriptografi kunci asimetris (asymmetric cryptography) untuk menjamin tiga aspek fundamental keamanan informasi: Autentikasi (memastikan identitas pengirim), Integritas (memastikan pesan tidak diubah selama transmisi), dan Nir-sangkal (Non-repudiation, mencegah pengirim menyangkal bahwa ia telah mengirim pesan tersebut). Tidak seperti tanda tangan fisik yang statis, tanda tangan digital bersifat unik untuk setiap dokumen; jika satu bit saja pada dokumen berubah, maka tanda tangan digitalnya menjadi tidak valid.

Secara teknis, proses pembuatan tanda tangan digital melibatkan penggunaan fungsi hash dan kunci privat pengirim. Pesan asli pertama-tama diproses melalui fungsi hash (seperti SHA-256) untuk menghasilkan message digest (sidik jari digital). Digest ini kemudian dienkripsi menggunakan kunci privat pengirim untuk menghasilkan tanda tangan digital. Penerima kemudian memverifikasi tanda tangan tersebut dengan mendekripsinya menggunakan kunci publik pengirim dan membandingkan hasil hash-nya dengan hash yang ia hitung sendiri dari pesan yang diterima. Jika kedua nilai hash cocok, maka integritas dan keaslian pengirim terjamin.

Dua algoritma yang paling umum digunakan untuk standar ini adalah RSA (Rivest–Shamir–Adleman) dan DSA (Digital Signature Algorithm). RSA mendasarkan keamanannya pada kesulitan memfaktorkan bilangan bulat besar (Integer Factorization Problem), di mana proses penandatanganan dan enkripsi adalah operasi matematis yang serupa namun dibalik. Sementara itu, DSA adalah standar yang ditetapkan oleh pemerintah AS (NIST) yang keamanannya didasarkan pada masalah logaritma diskrit (Discrete Logarithm Problem). DSA dirancang khusus hanya untuk penandatanganan digital dan tidak dapat digunakan untuk enkripsi data umum, berbeda dengan RSA yang bisa digunakan untuk keduanya. Dalam implementasi modern, varian DSA yang lebih efisien yaitu ECDSA (Elliptic Curve DSA) kini lebih sering digunakan pada perangkat dengan sumber daya terbatas.

---

## 3. Alat dan Bahan
Alat dan bahan yang digunakan dalam praktikum ini adalah sebagai berikut:
- Python 3.x
- Visual Studio Code sebagai editor kode
- Git dan akun GitHub untuk version control
- Library kriptografi pycryptodome untuk implementasi RSA dan digital signature

---

## 4. Langkah Percobaan
Langkah-langkah percobaan yang dilakukan pada praktikum ini adalah sebagai berikut:
1. Menginstal library pycryptodome pada lingkungan Python.
2. Membuat pasangan kunci RSA yang terdiri dari private key dan public key dengan panjang kunci 2048 bit.
3. Menginput pesan asli yang akan ditandatangani melalui terminal.
4. Melakukan proses hashing terhadap pesan menggunakan algoritma SHA-256.
5. Membuat tanda tangan digital dengan menggunakan private key RSA.
6. Melakukan proses verifikasi tanda tangan menggunakan public key RSA.
7. Mengamati hasil verifikasi untuk memastikan integritas dan keaslian pesan.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# INPUT PESAN DARI USER
user_message = input("Masukkan pesan yang akan ditandatangani: ")
original_message = user_message.encode('utf-8')

# GENERATE PASANGAN KUNCI RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Simpan kunci (opsional, best practice)
with open("private_key.pem", "wb") as f:
    f.write(private_key.export_key())

with open("public_key.pem", "wb") as f:
    f.write(public_key.export_key())

# HASH PESAN
hash_original = SHA256.new(original_message)

# BUAT TANDA TANGAN DIGITAL
signature = pkcs1_15.new(private_key).sign(hash_original)

print("\nTanda tangan digital berhasil dibuat.")
print("Signature (hex):", signature.hex())

# VERIFIKASI PESAN ASLI
try:
    hash_verify = SHA256.new(original_message)
    pkcs1_15.new(public_key).verify(hash_verify, signature)
    print("Verifikasi berhasil: tanda tangan VALID.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK valid.")
```

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
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
   Enkripsi RSA dan tanda tangan digital RSA sama-sama menggunakan algoritma kunci publik, tetapi memiliki tujuan dan mekanisme yang berbeda secara fundamental. Enkripsi RSA berfokus pada kerahasiaan (confidentiality) pesan, di mana pengirim mengenkripsi data menggunakan public key milik penerima sehingga hanya penerima yang dapat mendekripsinya dengan private key. Sebaliknya, tanda tangan digital RSA bertujuan untuk menjamin keaslian dan keutuhan pesan, bukan menyembunyikan isinya. Pada tanda tangan digital, pengirim menandatangani hash dari pesan menggunakan private key-nya sendiri, dan siapa pun dapat memverifikasinya menggunakan public key pengirim. Dengan demikian, enkripsi menjawab pertanyaan “siapa yang boleh membaca pesan,” sedangkan tanda tangan digital menjawab “siapa pengirim pesan dan apakah pesan telah diubah.”
   
2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
   Tanda tangan digital menjamin integritas dan otentikasi pesan melalui kombinasi fungsi hash kriptografis dan kriptografi kunci publik. Integritas terjamin karena tanda tangan dibuat dari nilai hash pesan; perubahan sekecil apa pun pada isi pesan akan menghasilkan hash yang berbeda dan menyebabkan proses verifikasi gagal. Otentikasi terjamin karena tanda tangan hanya dapat dibuat menggunakan private key yang secara eksklusif dimiliki oleh pengirim, sehingga keberhasilan verifikasi dengan public key yang sesuai membuktikan bahwa pesan benar-benar berasal dari pemilik kunci tersebut. Selain itu, mekanisme ini juga memberikan sifat non-repudiation, yaitu pengirim tidak dapat menyangkal telah menandatangani pesan selama private key tetap aman.
   
3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern? 
   Dalam sistem tanda tangan digital modern, Certificate Authority (CA) berperan sebagai pihak tepercaya yang menjembatani identitas pengguna dengan public key yang digunakan untuk verifikasi tanda tangan. CA menerbitkan sertifikat digital yang mengikat identitas suatu entitas—seperti individu, organisasi, atau server—dengan public key tertentu melalui proses validasi yang terstandarisasi. Dengan adanya CA, pihak penerima tidak perlu secara langsung mempercayai pengirim, melainkan cukup mempercayai CA yang menandatangani sertifikat tersebut. Mekanisme ini membentuk chain of trust yang menjadi fondasi keamanan pada protokol modern seperti TLS/SSL, memastikan bahwa tanda tangan digital diverifikasi tidak hanya secara kriptografis, tetapi juga secara identitas dan kepercayaan.

---

## 8. Kesimpulan
Berdasarkan hasil eksekusi program, sistem berhasil menghasilkan tanda tangan digital untuk pesan yang diinput oleh pengguna. Proses verifikasi menunjukkan bahwa tanda tangan dinyatakan valid ketika pesan tidak mengalami perubahan, yang menandakan bahwa pesan berasal dari pengirim yang sah dan tidak mengalami modifikasi.

Ketika pesan dimodifikasi, proses verifikasi menghasilkan status tidak valid, yang membuktikan bahwa mekanisme tanda tangan digital RSA mampu mendeteksi perubahan isi pesan. Hasil ini sesuai dengan teori tanda tangan digital yang menjamin integritas dan otentikasi data. Selama proses pengujian, tidak ditemukan error yang menghambat jalannya program.

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa algoritma RSA dapat diimplementasikan untuk membangun sistem tanda tangan digital dengan baik. Tanda tangan digital mampu menjamin integritas, otentikasi, dan non-repudiation pada pesan yang dikirimkan. Hasil percobaan menunjukkan bahwa perubahan pesan akan menyebabkan verifikasi gagal, sesuai dengan konsep kriptografi kunci publik.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. Introduction to Modern Cryptography. CRC Press.
- Stallings, W. Cryptography and Network Security: Principles and Practice. Pearson.
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. Handbook of Applied Cryptography. CRC Press.
- NIST. Digital Signature Standard (DSS), FIPS PUB 186-4.

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
