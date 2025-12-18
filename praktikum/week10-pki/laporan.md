# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: Public Key Infrastructure (PKI & Certificate Authority) 
Nama: Achmad Wahyudi 
NIM: 230202728 
Kelas: 5IKRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan kerangka kerja keamanan yang dirancang untuk mengelola penggunaan kriptografi kunci publik secara aman dan terstandarisasi. PKI menyediakan mekanisme untuk pembuatan, distribusi, penyimpanan, dan pencabutan pasangan kunci kriptografi beserta sertifikat digital yang mengikat kunci publik dengan identitas suatu entitas. Dalam sistem PKI, sertifikat digital berfungsi sebagai bukti kriptografis yang memverifikasi bahwa suatu kunci publik benar-benar dimiliki oleh individu, organisasi, atau sistem tertentu. Dengan adanya PKI, masalah kepercayaan (trust) dalam komunikasi digital dapat diselesaikan tanpa memerlukan pertukaran kunci secara langsung antara pihak-pihak yang berkomunikasi.

Certificate Authority (CA) merupakan komponen inti dalam PKI yang berperan sebagai pihak tepercaya (trusted third party). CA bertugas melakukan proses validasi identitas pemohon sertifikat sebelum menerbitkan sertifikat digital yang ditandatangani secara kriptografis menggunakan private key milik CA. Sertifikat ini berisi informasi penting seperti identitas pemilik, kunci publik, periode validitas, serta tanda tangan digital CA. Karena public key CA telah dipercaya secara luas dan tertanam pada sistem operasi atau browser, maka sertifikat yang diterbitkan CA dapat diverifikasi keabsahannya oleh pihak lain tanpa perlu mengenal pemilik sertifikat secara langsung.

Dalam implementasi modern, PKI membentuk struktur hierarkis yang dikenal sebagai chain of trust, yang biasanya terdiri dari root CA, intermediate CA, dan end-entity certificate. Struktur ini meningkatkan keamanan dan fleksibilitas pengelolaan sertifikat, karena root CA tidak digunakan secara langsung untuk menandatangani sertifikat pengguna akhir. PKI dan CA menjadi fondasi utama berbagai layanan keamanan digital, seperti protokol TLS/SSL, tanda tangan digital, dan sistem autentikasi berbasis sertifikat, yang memastikan komunikasi data berlangsung secara aman, terautentikasi, dan berintegritas.

---

## 3. Alat dan Bahan
Alat dan bahan yang digunakan dalam praktikum ini adalah sebagai berikut:
- Python 3.x
- Visual Studio Code atau editor teks sejenis
- Sistem operasi Windows
- Library Python cryptography
= Git dan akun GitHub untuk pengelolaan versi kode
---

## 4. Langkah Percobaan
1. Membuat Sertifikat Digital Sederhana
2. Verifikasi Sertifikat dan Peran CA
   - Sertifikat memiliki tanda tangan digital
   - Tanda tangan diverifikasi menggunakan public key CA
   - Jika tanda tangan valid dan sertifikat masih berlaku → sertifikat sah
   - Pada browser, public key CA sudah ada di trust store
3. Analisis PKI
   1. Bagaimana browser memverifikasi sertifikat HTTPS?
Ketika pengguna mengakses situs HTTPS, browser menerima sertifikat digital dari server dan memeriksa beberapa hal: validitas waktu sertifikat, kecocokan domain (Common Name / SAN), serta tanda tangan digital sertifikat tersebut. Browser kemudian memverifikasi tanda tangan ini menggunakan public key CA yang terdapat dalam trust store. Jika sertifikat ditandatangani oleh intermediate CA, browser akan membangun chain of trust hingga mencapai root CA yang dipercaya. Jika seluruh rantai valid, koneksi HTTPS dianggap aman.

   2. Apa yang terjadi jika CA palsu menerbitkan sertifikat?
Jika CA palsu berhasil dipercaya oleh sistem atau browser, maka ia dapat menerbitkan sertifikat palsu untuk domain mana pun, sehingga memungkinkan serangan Man-in-the-Middle. Inilah sebabnya mengapa keamanan private key CA sangat krusial. Dalam praktik nyata, jika sebuah CA terbukti bermasalah, sertifikatnya akan dicabut melalui Certificate Revocation List (CRL) atau Online Certificate Status Protocol (OCSP), dan browser akan menghentikan kepercayaan terhadap CA tersebut.

    3. Mengapa PKI penting dalam komunikasi aman?
PKI menyediakan mekanisme terstandarisasi untuk membangun kepercayaan dalam komunikasi digital skala besar tanpa memerlukan pertukaran kunci secara manual. Dalam konteks transaksi online, PKI memastikan bahwa pengguna benar-benar terhubung ke server yang sah, bukan server tiruan. Tanpa PKI, sistem keamanan seperti HTTPS, tanda tangan digital dokumen, email terenkripsi, dan autentikasi berbasis sertifikat tidak dapat diimplementasikan secara aman dan skalabel.
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

# GENERATE PRIVATE KEY (CA)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# IDENTITAS SERTIFIKAT
# (Self-Signed Certificate)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, "UPB Root CA"),
])

# MEMBANGUN SERTIFIKAT DIGITAL
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True
    )
    .sign(private_key, hashes.SHA256())
)

# SIMPAN PRIVATE KEY
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# SIMPAN SERTIFIKAT
with open("certificate.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

print("Self-signed certificate berhasil dibuat.")
print("File tersimpan: private_key.pem dan certificate.pem")

```
)

---

## 6. Hasil dan Pembahasan
Berdasarkan hasil pelaksanaan praktikum, program Python berhasil menghasilkan sebuah sertifikat digital self-signed beserta private key dalam format PEM. Sertifikat yang dihasilkan memuat informasi identitas penerbit (issuer) dan pemilik sertifikat (subject) yang sama, sehingga mencerminkan konsep self-signed certificate. File certificate.pem dan private_key.pem tersimpan dengan baik pada direktori kerja, menandakan bahwa proses pembuatan sertifikat berjalan tanpa error.

Sertifikat yang dihasilkan memiliki masa berlaku selama satu tahun dan dilengkapi dengan ekstensi BasicConstraints yang menandakan bahwa sertifikat berperan sebagai Certificate Authority (CA). Hasil ini sesuai dengan tujuan praktikum, yaitu memahami bagaimana sertifikat digital dibangun dan ditandatangani menggunakan kriptografi kunci publik. Meskipun sertifikat ini valid secara kriptografis, sertifikat self-signed tidak dipercaya secara otomatis oleh browser karena tidak memiliki chain of trust yang terhubung ke CA tepercaya. Hal ini menegaskan perbedaan antara implementasi PKI pada lingkungan pembelajaran dan sistem produksi.

---

## 7. Jawaban Pertanyaan

1. Apa fungsi utama Certificate Authority (CA)?
Certificate Authority (CA) berfungsi sebagai pihak tepercaya yang bertanggung jawab untuk memverifikasi identitas suatu entitas dan menerbitkan sertifikat digital yang mengikat identitas tersebut dengan kunci publik tertentu. Dengan menandatangani sertifikat secara kriptografis menggunakan private key milik CA, CA menjamin bahwa kunci publik dalam sertifikat tersebut benar-benar milik entitas yang tercantum. Peran ini memungkinkan pihak lain untuk melakukan verifikasi keaslian sertifikat tanpa harus mengenal pemilik sertifikat secara langsung, karena kepercayaan didelegasikan kepada CA sebagai otoritas tepercaya dalam sistem PKI.

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Self-signed certificate tidak cukup untuk sistem produksi karena tidak memiliki rantai kepercayaan (chain of trust) yang diakui secara luas. Pada sertifikat self-signed, entitas yang menerbitkan sertifikat adalah entitas yang sama dengan pemilik sertifikat, sehingga tidak ada pihak ketiga independen yang memvalidasi identitasnya. Akibatnya, klien atau browser tidak dapat membedakan apakah sertifikat tersebut berasal dari server yang sah atau dari pihak penyerang, sehingga menimbulkan risiko keamanan dan peringatan kepercayaan. Oleh karena itu, sertifikat jenis ini hanya sesuai untuk lingkungan pengujian atau pengembangan, bukan untuk sistem yang melibatkan pengguna umum.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS dengan memastikan bahwa kunci publik server yang digunakan dalam proses enkripsi benar-benar milik server yang sah. Saat koneksi HTTPS dibangun, browser memverifikasi sertifikat server melalui chain of trust hingga mencapai root CA yang dipercaya. Jika penyerang mencoba menyisipkan diri dengan menggunakan sertifikat palsu, proses verifikasi akan gagal karena sertifikat tersebut tidak ditandatangani oleh CA tepercaya atau telah dicabut. Dengan mekanisme ini, PKI memastikan autentikasi server, integritas sertifikat, dan kerahasiaan komunikasi, sehingga serangan MITM dapat dicegah secara efektif.
---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Public Key Infrastructure (PKI) menyediakan mekanisme terstandarisasi untuk mengelola kunci publik dan sertifikat digital secara aman. Melalui implementasi program Python, mahasiswa dapat memahami proses pembuatan sertifikat digital self-signed serta peran kriptografi kunci publik dalam menjamin keaslian identitas suatu entitas.

Hasil percobaan menunjukkan bahwa sertifikat digital dapat dibuat dan ditandatangani secara mandiri menggunakan private key, sehingga valid secara teknis. Namun, sertifikat self-signed tidak cukup untuk digunakan pada sistem produksi karena tidak didukung oleh Certificate Authority (CA) tepercaya, yang menyebabkan sertifikat tersebut tidak dikenali oleh browser atau klien umum.

Dengan demikian, PKI dan CA memiliki peran yang sangat penting dalam komunikasi aman modern, khususnya pada protokol TLS/HTTPS. PKI memungkinkan terbentuknya chain of trust yang menjamin autentikasi server, integritas sertifikat, dan perlindungan terhadap serangan Man-in-the-Middle, sehingga menjadi fondasi utama keamanan komunikasi digital.

---

## 9. Daftar Pustaka
- Katz, J., & Lindell, Y. Introduction to Modern Cryptography. CRC Press.
- Stallings, W. Cryptography and Network Security: Principles and Practice. Pearson.Menezes, A. - J., van Oorschot, P. C., & Vanstone, S. A. Handbook of Applied Cryptography. CRC Press.
- NIST. Digital Signature Standard (DSS), FIPS PUB 186-4.
- Rescorla, E. HTTP Over TLS (RFC 2818). IETF.

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
