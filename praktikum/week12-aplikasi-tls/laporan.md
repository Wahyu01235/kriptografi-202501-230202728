# Laporan Praktikum Kriptografi
Minggu ke-: 12 
Topik: Aplikasi TLS & E-commerce
Nama: Achmad Wahyudi  
NIM: 230202728 
Kelas: 5IKRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menganalisis penggunaan kriptografi pada **email** dan **SSL/TLS**.  
2. Menjelaskan enkripsi dalam transaksi **e-commerce**.  
3. Mengevaluasi isu **etika & privasi** dalam penggunaan kriptografi di kehidupan sehari-hari. 

---

## 2. Dasar Teori
Transport Layer Security (TLS) merupakan protokol kriptografi yang dirancang untuk menjamin keamanan komunikasi data pada jaringan terbuka, khususnya Internet. TLS berevolusi dari Secure Sockets Layer (SSL) sebagai respons terhadap kerentanan inheren pada model komunikasi client–server awal yang mentransmisikan data dalam bentuk plaintext. Secara fundamental, TLS bekerja dengan mengamankan tiga properti utama: kerahasiaan (confidentiality) melalui enkripsi simetris, integritas data (integrity) melalui message authentication code (MAC), serta autentikasi (authentication) menggunakan kriptografi kunci publik dan sertifikat digital. Mekanisme handshake pada TLS memungkinkan dua pihak yang belum saling mengenal untuk menyepakati parameter keamanan secara aman, termasuk algoritma kriptografi dan kunci sesi.

Dalam konteks e-commerce, TLS berfungsi sebagai tulang punggung kepercayaan digital antara konsumen dan penyedia layanan. Transaksi e-commerce melibatkan pertukaran data sensitif seperti kredensial pengguna, informasi kartu pembayaran, dan detail transaksi finansial, yang menjadikannya target utama serangan seperti man-in-the-middle, sniffing, dan session hijacking. Implementasi TLS pada protokol HTTPS memastikan bahwa data yang dikirimkan tidak dapat dibaca atau dimodifikasi oleh pihak ketiga selama transmisi. Lebih jauh, sertifikat digital yang dikeluarkan oleh Certificate Authority (CA) berperan sebagai mekanisme verifikasi identitas server, sehingga pengguna dapat memverifikasi legitimasi platform e-commerce yang diakses.

Secara sistemik, penggunaan TLS dalam e-commerce tidak hanya berdampak pada keamanan teknis, tetapi juga pada aspek kepercayaan pengguna, kepatuhan regulasi, dan keberlanjutan bisnis digital. Standar keamanan seperti PCI DSS secara eksplisit mewajibkan penggunaan enkripsi kuat dalam transmisi data pembayaran, yang secara praktis mengunci TLS sebagai komponen wajib dalam arsitektur e-commerce modern. Namun, asumsi bahwa “TLS = aman” merupakan simplifikasi yang berbahaya; konfigurasi yang lemah, penggunaan versi TLS usang, atau manajemen sertifikat yang buruk tetap membuka celah serangan. Dengan demikian, TLS harus dipahami bukan sebagai solusi tunggal, melainkan sebagai bagian dari ekosistem keamanan berlapis (defense in depth).

Dalam jangka panjang, aplikasi TLS pada e-commerce mencerminkan pergeseran paradigma dari sekadar pengamanan data menuju pengelolaan kepercayaan dalam skala global. Evolusi TLS—seperti TLS 1.3 yang mengurangi latensi dan memperketat keamanan—menunjukkan bahwa kebutuhan e-commerce tidak hanya menuntut keamanan, tetapi juga efisiensi dan pengalaman pengguna. Di sisi lain, ketergantungan besar pada infrastruktur CA menciptakan titik sentral kepercayaan yang rentan terhadap kegagalan sistemik. Oleh karena itu, pemahaman teoritis TLS dalam e-commerce perlu mencakup dimensi teknis, ekonomis, dan institusional agar implementasinya tidak hanya aman secara kriptografis, tetapi juga tangguh secara strategis.

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
# =========================================================
# PRAKTIKUM KEAMANAN JARINGAN
# LANGKAH 1–3: TLS, E-COMMERCE, ETIKA & PRIVASI
# DENGAN ANALISIS OTOMATIS (100% STANDARD LIBRARY)
# =========================================================

import ssl
import socket
import os
import urllib.request
import urllib.parse
import base64
import hashlib
from datetime import datetime

# =========================================================
# LANGKAH 1: ANALISIS SSL/TLS WEBSITE E-COMMERCE
# =========================================================

def analyze_tls_certificate(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            tls_version = ssock.version()

    issuer = dict(x[0] for x in cert["issuer"])

    valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z")
    valid_until = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")

    return {
        "Website": hostname,
        "Issuer CA": issuer.get("organizationName", "Unknown"),
        "Valid From": valid_from.strftime("%Y-%m-%d"),
        "Valid Until": valid_until.strftime("%Y-%m-%d"),
        "TLS Version": tls_version,
        "Cipher Suite": cipher[0],
        "Encryption": cipher[1],
        "Key Length": cipher[2]
    }

# =========================================================
# LANGKAH 2: STUDI KASUS E-COMMERCE (HTTP vs HTTPS)
# =========================================================

def send_post(url, data):
    encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=encoded)
    with urllib.request.urlopen(req) as response:
        return response.read().decode()

def ecommerce_transaction_simulation():
    data = {
        "username": "user_demo",
        "password": "password123",
        "card_number": "4111111111111111",
        "amount": "150000"
    }

    https_url = "https://httpbin.org/post"
    http_url = "http://httpbin.org/post"

    https_result = send_post(https_url, data)
    http_result = send_post(http_url, data)

    analysis = [
        "Data transaksi yang dikirim melalui HTTPS dienkripsi selama proses transmisi menggunakan TLS.",
        "Pada HTTP, data dikirim dalam bentuk plaintext sehingga dapat disadap oleh pihak ketiga.",
        "TLS melindungi kerahasiaan (confidentiality) dan integritas data transaksi.",
        "Tanpa TLS, sistem rentan terhadap serangan Man-in-the-Middle (MITM), credential theft, dan session hijacking.",
        "Penggunaan TLS meningkatkan kepercayaan pengguna terhadap platform e-commerce."
    ]

    return https_result, http_result, analysis

# =========================================================
# LANGKAH 3: ANALISIS ETIKA & PRIVASI (EMAIL TERENKRIPSI)
# =========================================================

def encrypted_email_simulation():
    message = "Email internal perusahaan bersifat rahasia"

    encoded = base64.b64encode(message.encode()).decode()
    decoded = base64.b64decode(encoded.encode()).decode()
    integrity_hash = hashlib.sha256(message.encode()).hexdigest()

    analysis_points = [
        "Email terenkripsi bertujuan melindungi kerahasiaan isi pesan dari pihak yang tidak berwenang.",
        "Hanya pihak yang memiliki mekanisme dekripsi yang sesuai yang dapat membaca isi email.",
        "Dalam konteks organisasi, enkripsi email dapat menghambat proses audit dan investigasi internal.",
        "Dekripsi email karyawan oleh perusahaan menimbulkan dilema antara keamanan organisasi dan privasi individu.",
        "Kebijakan pemerintah terkait pengawasan komunikasi terenkripsi harus menyeimbangkan keamanan nasional dan hak privasi warga.",
        "Pelemahan sistem enkripsi berisiko menciptakan kerentanan sistemik yang dapat disalahgunakan."
    ]

    return message, encoded, decoded, integrity_hash, analysis_points

# =========================================================
# EXPORT HASIL + ANALISIS KE FILE HTML
# =========================================================

def export_to_html(tls_results, ecommerce_data, email_data):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "laporan_praktikum_tls.html")

    https_data, http_data, ecommerce_analysis = ecommerce_data
    msg, enc, dec, hash_val, email_analysis = email_data

    html = f"""
    <html>
    <head>
        <title>Laporan Praktikum TLS & E-Commerce</title>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
            th {{ background-color: #f0f0f0; }}
            ul {{ margin-top: 10px; }}
            pre {{ background: #fafafa; padding: 10px; overflow-x: auto; }}
        </style>
    </head>
    <body>

    <h1>Laporan Praktikum Keamanan Jaringan</h1>

    <h2>Langkah 1 — Analisis SSL/TLS</h2>
    <table>
        <tr>
            <th>Website</th><th>Issuer CA</th><th>Valid From</th><th>Valid Until</th>
            <th>TLS Version</th><th>Cipher Suite</th><th>Encryption</th><th>Key Length</th>
        </tr>
    """

    for r in tls_results:
        html += f"""
        <tr>
            <td>{r['Website']}</td>
            <td>{r['Issuer CA']}</td>
            <td>{r['Valid From']}</td>
            <td>{r['Valid Until']}</td>
            <td>{r['TLS Version']}</td>
            <td>{r['Cipher Suite']}</td>
            <td>{r['Encryption']}</td>
            <td>{r['Key Length']}</td>
        </tr>
        """

    html += f"""
    </table>

    <h2>Langkah 2 — Studi Kasus E-Commerce</h2>
    <p><b>HTTPS (dengan TLS):</b></p>
    <pre>{https_data}</pre>

    <p><b>HTTP (tanpa TLS):</b></p>
    <pre>{http_data}</pre>

    <h3>Analisis Langkah 2</h3>
    <ul>
    {''.join(f"<li>{point}</li>" for point in ecommerce_analysis)}
    </ul>

    <h2>Langkah 3 — Analisis Etika & Privasi</h2>
    <p><b>Pesan Asli:</b> {msg}</p>
    <p><b>Pesan Terenkripsi (simulasi):</b> {enc}</p>
    <p><b>Pesan Terdekripsi:</b> {dec}</p>
    <p><b>Hash Integritas (SHA-256):</b> {hash_val}</p>

    <h3>Analisis Langkah 3</h3>
    <ul>
    {''.join(f"<li>{point}</li>" for point in email_analysis)}
    </ul>

    </body>
    </html>
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("\nLaporan berhasil dibuat:")
    print(file_path)

# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":
    websites = [
        "www.tokopedia.com",
        "www.shopee.co.id",
        "www.bukalapak.com"
    ]

    tls_results = [analyze_tls_certificate(w) for w in websites]
    ecommerce_data = ecommerce_transaction_simulation()
    email_data = encrypted_email_simulation()

    export_to_html(tls_results, ecommerce_data, email_data)
```

---

## 6. Hasil dan Pembahasan
Berdasarkan hasil pengujian dan analisis yang dilakukan, seluruh website e-commerce yang diamati telah menerapkan protokol SSL/TLS pada koneksi HTTPS dengan sertifikat digital yang diterbitkan oleh Certificate Authority (CA) terpercaya dan masa berlaku yang aktif. Informasi TLS yang diperoleh menunjukkan penggunaan versi TLS modern serta cipher suite yang kuat, yang menandakan bahwa proses komunikasi antara klien dan server telah diamankan melalui mekanisme enkripsi, autentikasi, dan integritas data. Kondisi ini menunjukkan bahwa platform e-commerce telah memenuhi standar keamanan dasar dalam melindungi pertukaran data di jaringan publik.

Pada studi kasus e-commerce, hasil simulasi pengiriman data transaksi melalui HTTP dan HTTPS memperlihatkan bahwa isi data yang diterima oleh server secara fungsional tampak sama, namun proses transmisi keduanya memiliki tingkat keamanan yang sangat berbeda. Pada koneksi HTTPS, data transaksi dilindungi oleh TLS sehingga tidak dapat dibaca atau dimodifikasi oleh pihak ketiga selama transmisi. Sebaliknya, pada koneksi HTTP data dikirimkan dalam bentuk plaintext, sehingga sangat rentan terhadap serangan seperti penyadapan, Man-in-the-Middle (MITM), pencurian kredensial, dan pembajakan sesi. Temuan ini menegaskan bahwa keamanan e-commerce tidak hanya bergantung pada aplikasi, tetapi sangat ditentukan oleh mekanisme pengamanan pada lapisan komunikasi jaringan.

Analisis etika dan privasi pada penggunaan email terenkripsi menunjukkan bahwa mekanisme enkripsi berperan penting dalam menjaga kerahasiaan dan integritas komunikasi. Melalui simulasi, ditunjukkan bahwa pesan hanya dapat dipahami oleh pihak yang memiliki mekanisme dekripsi yang sesuai, sementara nilai hash digunakan untuk memastikan bahwa isi pesan tidak mengalami perubahan. Namun, penerapan enkripsi email juga menimbulkan dilema etika, khususnya dalam lingkungan organisasi dan kebijakan publik. Di satu sisi, enkripsi melindungi privasi individu dan mencegah kebocoran informasi sensitif. Di sisi lain, enkripsi dapat membatasi kemampuan perusahaan dalam melakukan audit internal atau pemerintah dalam pengawasan keamanan. Oleh karena itu, hasil praktikum ini menunjukkan bahwa enkripsi bukan hanya persoalan teknis, melainkan juga isu tata kelola dan etika yang memerlukan keseimbangan antara keamanan, privasi, dan kepentingan bersama.

---

## 7. Jawaban Pertanyaan
# Pembahasan Pertanyaan

## 1. Perbedaan Utama antara HTTP dan HTTPS

Perbedaan utama antara HTTP (Hypertext Transfer Protocol) dan HTTPS (Hypertext Transfer Protocol Secure) terletak pada aspek keamanannya. HTTP mentransmisikan data antara klien dan server dalam bentuk plaintext tanpa mekanisme enkripsi, sehingga informasi yang dikirim dapat dengan mudah disadap, dibaca, atau dimodifikasi oleh pihak ketiga. Kondisi ini menjadikan HTTP sangat rentan terhadap serangan seperti sniffing, Man-in-the-Middle (MITM), dan pencurian data sensitif.

Sebaliknya, HTTPS mengintegrasikan protokol TLS (Transport Layer Security) untuk mengamankan proses komunikasi. Melalui TLS, data yang dikirim dienkripsi, diverifikasi integritasnya, dan server diautentikasi menggunakan sertifikat digital. Dengan demikian, HTTPS tidak hanya melindungi kerahasiaan data, tetapi juga memastikan bahwa komunikasi berlangsung dengan pihak yang sah. Perbedaan ini menjadikan HTTPS sebagai standar wajib dalam sistem e-commerce dan layanan digital modern.

---

## 2. Pentingnya Sertifikat Digital dalam Komunikasi TLS

Sertifikat digital berperan sebagai mekanisme autentikasi dalam komunikasi TLS untuk memastikan identitas pihak yang berkomunikasi, khususnya server. Sertifikat ini diterbitkan oleh Certificate Authority (CA) yang dipercaya dan berisi informasi identitas server beserta kunci publik yang digunakan dalam proses enkripsi. Melalui sertifikat digital, klien dapat memverifikasi bahwa server yang diakses benar-benar sah dan bukan pihak yang menyamar.

Tanpa sertifikat digital, proses enkripsi TLS kehilangan makna kepercayaannya, karena klien tidak memiliki jaminan bahwa kunci publik yang digunakan berasal dari server yang benar. Hal ini membuka peluang terjadinya serangan Man-in-the-Middle, di mana penyerang dapat memalsukan identitas server. Oleh karena itu, sertifikat digital merupakan fondasi utama dalam membangun kepercayaan dan keamanan komunikasi berbasis TLS.

---

## 3. Peran Kriptografi dalam Privasi serta Tantangan Hukum dan Etika

Kriptografi mendukung privasi dalam komunikasi digital dengan menyediakan mekanisme enkripsi dan integritas data, sehingga hanya pihak yang berwenang yang dapat membaca dan memverifikasi isi pesan. Dalam konteks e-commerce dan email terenkripsi, kriptografi melindungi data sensitif seperti informasi pribadi, kredensial, dan transaksi keuangan dari penyadapan dan manipulasi. Dengan demikian, kriptografi menjadi pilar utama dalam menjaga kepercayaan dan keamanan di dunia digital.

Namun, penerapan kriptografi yang kuat juga menimbulkan tantangan hukum dan etika. Enkripsi dapat membatasi kemampuan perusahaan untuk melakukan audit internal atau investigasi keamanan, serta menyulitkan pemerintah dalam penegakan hukum dan pengawasan terhadap aktivitas ilegal. Upaya untuk melemahkan atau memberikan akses khusus (backdoor) terhadap sistem enkripsi demi kepentingan pengawasan berisiko menciptakan kerentanan sistemik yang dapat disalahgunakan. Oleh karena itu, penggunaan kriptografi memerlukan keseimbangan antara perlindungan privasi, kebutuhan keamanan, dan kepatuhan terhadap hukum yang berlaku.

---

## 8. Kesimpulan
Berdasarkan hasil dan pembahasan yang diperoleh, dapat disimpulkan bahwa TLS merupakan komponen esensial dalam menjaga keamanan dan kepercayaan pada sistem e-commerce, khususnya dalam melindungi data transaksi selama transmisi. Perbandingan antara HTTP dan HTTPS menunjukkan bahwa keamanan tidak ditentukan oleh aplikasi semata, melainkan oleh mekanisme perlindungan pada lapisan komunikasi jaringan. Selain itu, penggunaan enkripsi pada email menegaskan pentingnya keseimbangan antara perlindungan privasi dan kebutuhan pengawasan. Enkripsi tidak hanya menjadi solusi teknis, tetapi juga memunculkan konsekuensi etika dan kebijakan yang harus dipertimbangkan secara matang. Oleh karena itu, penerapan teknologi keamanan harus selalu disertai dengan pemahaman konseptual, etika, dan tata kelola yang tepat agar sistem digital tidak hanya aman secara teknis, tetapi juga berkelanjutan dan dapat dipercaya.

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
