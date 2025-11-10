# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik:  Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama:  Achmad Wahyudi
NIM: 230202728
Kelas: 5IKRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropi dalam kriptografi adalah ukuran ketidakpastian atau keacakan dari kunci yang digunakan. Semakin tinggi entropi sebuah kunci, semakin sulit kunci tersebut untuk ditebak atau diprediksi. Kekuatan kunci (key strength) secara langsung bergantung pada entropi ini, yang seringkali diukur dalam bit. Misalnya, kunci dengan entropi 128 bit berarti ada $2^{128}$ kemungkinan kunci unik. Kumpulan semua kemungkinan kunci ini disebut sebagai ruang kunci (keyspace). Ruang kunci yang besar sangat penting untuk melindungi data dari upaya serangan.

Evaluasi kekuatan kunci sangat erat kaitannya dengan ketahanannya terhadap serangan brute force. Serangan brute force adalah metode di mana penyerang mencoba setiap kombinasi kunci yang mungkin dalam ruang kunci sampai kunci yang benar ditemukan. Jika sebuah kunci memiliki entropi yang tinggi, seperti 128 bit atau 256 bit, jumlah kemungkinan yang harus dicoba menjadi sangat besar secara astronomis. Akibatnya, waktu dan sumber daya komputasi yang diperlukan untuk menemukan kunci yang benar melalui brute force menjadi tidak praktis, bahkan dengan teknologi superkomputer modern sekalipun.

Jarak keunikan (unicity distance) adalah konsep teoretis yang diperkenalkan oleh Claude Shannon untuk mengukur jumlah minimum ciphertext yang diperlukan agar seorang analis kripto dapat secara unik menentukan kunci yang benar. Konsep ini bergantung pada redundansi bahasa yang digunakan dalam plaintext (misalnya, dalam bahasa Indonesia, huruf 'A' lebih sering muncul daripada 'X'). Jika jumlah ciphertext yang dimiliki penyerang lebih sedikit dari jarak keunikan, mungkin ada beberapa kunci berbeda yang dapat mendekripsi ciphertext menjadi pesan yang tampak masuk akal. Namun, setelah melampaui jarak keunikan, diasumsikan hanya ada satu kunci yang benar yang akan menghasilkan plaintext asli yang bermakna.

Secara bersama-sama, entropi dan jarak keunikan memberikan evaluasi teoretis tentang keamanan sebuah sandi (cipher). Entropi menentukan kelayakan serangan brute force dengan mendefinisikan ukuran total ruang kunci. Sementara itu, jarak keunikan menunjukkan berapa banyak data terenkripsi yang diperlukan sebelum serangan statistik (yang mengeksploitasi pola bahasa) dapat berhasil menemukan kunci yang unik. Pada algoritma enkripsi modern yang kuat, entropi kunci dibuat sangat tinggi dan output ciphertext dirancang agar terlihat seperti data acak, sehingga jarak keunikan seringkali menjadi sangat besar dan membuat serangan statistik tidak efektif.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Perhitungan Entropi
Gunakan rumus:  
\[
H(K) = \log_2 |K|
\]  
dengan \(|K|\) adalah ukuran ruang kunci.  

Contoh implementasi Python:  
```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
```

### Langkah 2 — Menghitung Unicity Distance
Gunakan rumus:  
\[
U = \frac{H(K)}{R \cdot \log_2 |A|}
\]  
dengan:  
- \(H(K)\): entropi kunci,  
- \(R\): redundansi bahasa (misal bahasa Inggris \(R \approx 0.75\)),  
- \(|A|\): ukuran alfabet (26 untuk A–Z).  

Contoh implementasi Python:  
```python
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
```

### Langkah 3 — Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.  

```python
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```


## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import math

# Langkah 1: Perhitungan Entropi
def entropy(keyspace_size):
    return math.log2(keyspace_size)

# Langkah 2: Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

# Langkah 3: Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# Contoh perhitungan
if __name__ == "__main__":
    print("=" * 50)
    print("ANALISIS KRIPTOGRAFI")
    print("=" * 50)
    
    # Kasus 1: Caesar Cipher
    keysize_caesar = 26
    entropy_caesar = entropy(keysize_caesar)
    ud_caesar = unicity_distance(entropy_caesar)
    bf_time_caesar = brute_force_time(keysize_caesar)
    
    print("\n1. CAESAR CIPHER (Alfabet 26 karakter):")
    print(f"   - Entropi Kunci: {entropy_caesar:.2f} bit")
    print(f"   - Unicity Distance: {ud_caesar:.2f} karakter ciphertext")
    print(f"   - Waktu Brute Force: {bf_time_caesar:.6f} hari (dengan 1 juta percobaan/detik)")
    
    # Kasus 2: AES-128
    keysize_aes = 2**128
    entropy_aes = entropy(keysize_aes)
    ud_aes = unicity_distance(entropy_aes)
    bf_time_aes = brute_force_time(keysize_aes)
    
    print("\n2. AES-128:")
    print(f"   - Entropi Kunci: {entropy_aes:.2f} bit")
    print(f"   - Unicity Distance: {ud_aes:.2f} karakter ciphertext")
    print(f"   - Waktu Brute Force: {bf_time_aes:.2e} hari (dengan 1 juta percobaan/detik)")
    
    # Kasus 3: Custom Input
    print("\n3. KALKULATOR KUSTOM:")
    try:
        custom_keysize = int(input("   Masukkan ukuran ruang kunci (contoh: 256): "))
        custom_entropy = entropy(custom_keysize)
        custom_ud = unicity_distance(custom_entropy)
        custom_bf = brute_force_time(custom_keysize)
        
        print(f"   - Entropi Kunci: {custom_entropy:.2f} bit")
        print(f"   - Unicity Distance: {custom_ud:.2f} karakter ciphertext")
        print(f"   - Waktu Brute Force: {custom_bf:.2e} hari")
        
    except ValueError:
        print("   Input tidak valid! Harap masukkan bilangan bulat.")

    print("\n" + "=" * 50)
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
1. Apa arti dari nilai **entropy** dalam konteks kekuatan kunci?
    Dalam konteks kekuatan kunci, nilai entropi adalah ukuran kuantitatif dari ketidakpastian atau keacakan sebuah kunci. Angka ini, yang biasanya diukur dalam bit, menunjukkan seberapa sulit kunci tersebut untuk ditebak. Nilai entropi yang tinggi berarti ada sangat banyak kemungkinan kombinasi kunci yang valid, sehingga membuatnya sangat sulit diprediksi. Sebagai contoh, sebuah kunci yang memiliki entropi 128 bit berarti ada $2^{128}$ kemungkinan kunci yang unik dan sama-sama mungkin. Semakin tinggi nilai entropi, semakin kuat kunci tersebut terhadap tebakan acak atau serangan brute force.
     
2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
  Jarak keunikan (unicity distance) penting karena ia memberikan perkiraan teoretis tentang jumlah minimum ciphertext yang perlu dikumpulkan oleh seorang analis kripto agar dapat secara unik menentukan kunci yang benar. Konsep ini sangat bergantung pada redundansi bahasa yang digunakan dalam plaintext (misalnya, dalam bahasa Indonesia, huruf 'a' lebih sering muncul daripada 'z'). Jika jumlah ciphertext yang dimiliki penyerang lebih sedikit dari jarak keunikan, mungkin ada beberapa kunci berbeda yang bisa menghasilkan dekripsi yang tampak masuk akal. Namun, setelah melampaui jarak keunikan, diasumsikan hanya ada satu kunci yang akan menghasilkan plaintext asli yang bermakna.  
  
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?  
    Serangan brute force masih menjadi ancaman meskipun algoritma enkripsinya sudah kuat, seperti AES. Kelemahan utamanya seringkali tidak terletak pada algoritma itu sendiri, tetapi pada implementasinya, yaitu pemilihan kunci yang lemah. Jika sebuah kunci dibuat berdasarkan kata sandi yang singkat atau mudah ditebak (seperti "123456" atau "password"), penyerang tidak perlu menyerang seluruh ruang kunci teoretis algoritma tersebut (misalnya $2^{128}$). Sebaliknya, mereka dapat melakukan brute force pada ruang kunci yang jauh lebih kecil yang hanya berisi kata sandi umum atau kombinasi sederhana. Peningkatan pesat dalam kekuatan komputasi, terutama menggunakan GPU atau komputasi awan, juga membuat serangan brute force terhadap kata sandi yang "cukup rumit" sekalipun menjadi lebih cepat dan lebih mungkin dilakukan.

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
