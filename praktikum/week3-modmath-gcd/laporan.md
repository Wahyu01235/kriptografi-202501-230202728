# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)
Nama: Achmad Wahyudi  
NIM: 230202728 
Kelas: 5IKRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan operasi aritmetika modular.  
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.  

---

## 2. Dasar Teori
Aritmetika modular adalah sistem bilangan di mana operasi dilakukan dalam rentang terbatas, ditentukan oleh suatu modulus n. Dalam sistem ini, angka "melingkar" setelah mencapai n, artinya hasilnya selalu antara 0 hingga n-1. Konsep ini sangat fundamental dalam kriptografi karena memungkinkan pemrosesan bilangan yang sangat besar secara efisien dan menciptakan properti "satu arah" yang menjadi dasar keamanan banyak algoritma. Operasi dasar seperti penjumlahan, pengurangan, perkalian, dan eksponensiasi modular adalah blok bangunan yang penting untuk enkripsi dan dekripsi.

Greatest Common Divisor (GCD) adalah bilangan bulat terbesar yang dapat membagi dua atau lebih bilangan tanpa sisa. Algoritma Euclidean menyediakan metode yang efisien untuk menghitung GCD. Konsep GCD ini diperluas oleh Algoritma Euclidean Diperpanjang, yang tidak hanya menghitung GCD tetapi juga menemukan koefisien x dan y yang memenuhi identitas Bézout (ax + ny = gcd(a, n)). Jika gcd(a, n) = 1, maka x adalah invers modular dari a modulo n, sebuah operasi krusial yang setara dengan "pembagian" dalam aritmetika modular dan sangat penting untuk dekripsi dalam skema kunci publik seperti RSA.

Logaritma Diskrit adalah analog dari logaritma biasa dalam aritmetika modular: mencari x sedemikian rupa sehingga a^x ≡ b (mod n). Meskipun mudah untuk menghitung a^x (mod n), membalikkan prosesnya (mencari x) secara komputasi sangat sulit untuk modulus n yang besar. Kesulitan masalah logaritma diskrit ini menjadi pilar keamanan untuk banyak algoritma kriptografi kunci publik, termasuk pertukaran kunci Diffie-Hellman dan sistem enkripsi ElGamal, membentuk dasar kekuatan enkripsi modern.

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
# file: praktikum/week3-modmath-gcd/src/modular_math.py

# --- Langkah 1: Aritmetika Modular ---
def modular_addition(num_a, num_b, modulus):
    """
    Melakukan operasi penjumlahan modular: (num_a + num_b) % modulus.
    """
    return (num_a + num_b) % modulus

def modular_subtraction(num_a, num_b, modulus):
    """
    Melakukan operasi pengurangan modular: (num_a - num_b) % modulus.
    Memastikan hasil selalu non-negatif.
    """
    return (num_a - num_b + modulus) % modulus

def modular_multiplication(num_a, num_b, modulus):
    """
    Melakukan operasi perkalian modular: (num_a * num_b) % modulus.
    """
    return (num_a * num_b) % modulus

def modular_exponentiation(base, exponent, modulus):
    """
    Melakukan operasi eksponensiasi modular: (base ^ exponent) % modulus.
    Menggunakan fungsi pow() bawaan Python yang efisien untuk ini.
    """
    return pow(base, exponent, modulus)

# --- Langkah 2: GCD & Algoritma Euclidean ---
def calculate_gcd(num_a, num_b):
    """
    Menghitung Greatest Common Divisor (GCD) dari dua bilangan
    menggunakan Algoritma Euclidean iteratif.
    """
    while num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return num_a

# --- Langkah 3: Extended Euclidean Algorithm & Invers Modular ---
def extended_euclidean_algorithm(num_a, num_b):
    """
    Implementasi Algoritma Euclidean Diperpanjang.
    Mengembalikan tuple (g, x, y) di mana g = gcd(num_a, num_b)
    dan memenuhi persamaan num_a*x + num_b*y = g.
    """
    if num_a == 0:
        return num_b, 0, 1
    
    gcd_val, x1, y1 = extended_euclidean_algorithm(num_b % num_a, num_a)
    x = y1 - (num_b // num_a) * x1
    y = x1
    return gcd_val, x, y

def find_modular_inverse(num_a, modulus):
    """
    Mencari invers modular dari num_a modulo modulus.
    Mengembalikan x sedemikian rupa sehingga (num_a * x) % modulus == 1.
    Mengembalikan None jika invers tidak ada (yaitu, gcd(num_a, modulus) != 1).
    """
    gcd_val, x_coeff, _ = extended_euclidean_algorithm(num_a, modulus)
    if gcd_val != 1:
        return None  # Invers modular tidak ada jika bukan koprima
    return x_coeff % modulus

# --- Langkah 4: Logaritma Diskrit (Discrete Log) ---
def solve_discrete_log(base_a, target_b, modulus_n):
    """
    Menyelesaikan masalah Logaritma Diskrit sederhana:
    Mencari x sedemikian rupa sehingga (base_a ^ x) % modulus_n == target_b.
    Ini adalah implementasi brute-force dan hanya cocok untuk modulus kecil.
    """
    for x_candidate in range(modulus_n): # Mencoba setiap nilai x dari 0 hingga n-1
        if modular_exponentiation(base_a, x_candidate, modulus_n) == target_b:
            return x_candidate
    return None # Jika tidak ada solusi yang ditemukan dalam rentang

# --- Bagian Eksekusi Utama Program ---
if __name__ == "__main__":
    print("--- Aritmetika Modular ---")
    # Output untuk penjumlahan, perkalian, dan eksponensiasi tetap sama
    print(f"7 + 5 mod 12 = {modular_addition(7, 5, 12)}")
    print(f"7 * 5 mod 12 = {modular_multiplication(7, 5, 12)}")
    print(f"7 ^ 128 mod 13 = {modular_exponentiation(7, 128, 13)}")

    print("\n--- GCD & Algoritma Euclidean ---")
    # Output untuk GCD tetap sama
    print(f"gcd(54, 24) = {calculate_gcd(54, 24)}")

    print("\n--- Extended Euclidean Algorithm & Invers Modular ---")
    # Output untuk invers modular tetap sama
    print(f"Invers 3 mod 11 = {find_modular_inverse(3, 11)}")

    print("\n--- Logaritma Diskrit Sederhana ---")
    # Output untuk logaritma diskrit tetap sama
    print(f"3^x == 4 (mod 7), x = {solve_discrete_log(3, 4, 7)}")

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
1. Apa peran aritmetika modular dalam kriptografi modern?
    Aritmetika modular adalah fondasi matematis bagi hampir semua algoritma kriptografi modern. Perannya sangat krusial karena ia memungkinkan operasi bilangan bulat tetap berada dalam rentang tertentu (0 hingga n-1), yang penting untuk efisiensi komputasi saat berurusan dengan bilangan sangat besar. Lebih dari itu, properti "satu arah" dari beberapa operasi modular, terutama eksponensiasi modular, sangat dimanfaatkan. Artinya, operasi mudah dilakukan dalam satu arah (enkripsi) tetapi sangat sulit atau tidak praktis untuk dibalik (dekripsi) tanpa informasi tambahan, seperti masalah logaritma diskrit dan pemfaktoran bilangan prima besar. Properti ini menjadi dasar keamanan untuk algoritma kunci publik.
2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
    Invers modular sangat penting dalam algoritma kunci publik seperti RSA karena ia adalah kunci untuk proses dekripsi. Dalam RSA, kunci enkripsi (e) dan kunci dekripsi (d) adalah invers modular satu sama lain terhadap fungsi totient Euler dari n (yaitu, (e * d) ≡ 1 (mod φ(n))). Ketika sebuah pesan dienkripsi menggunakan kunci publik (e), hasilnya adalah ciphertext. Untuk mendekripsi ciphertext kembali menjadi pesan asli, penerima harus menggunakan kunci privat (d), yang merupakan invers modular dari e. Tanpa kemampuan untuk menghitung dan menggunakan invers modular ini, operasi kebalikan dari enkripsi tidak akan mungkin dilakukan secara matematis, sehingga dekripsi tidak dapat terjadi.
3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
    Tantangan utama dalam menyelesaikan masalah logaritma diskrit (DLP) untuk modulus besar adalah ketiadaan algoritma klasik yang efisien untuk melakukannya. Meskipun mudah untuk menghitung a^x mod n (eksponensiasi modular), mencari nilai x yang memenuhi a^x ≡ b (mod n) secara komputasi sangat sulit. Kompleksitas waktu dari algoritma terbaik yang diketahui secara klasik untuk DLP tumbuh secara sub-eksponensial atau bahkan eksponensial seiring dengan ukuran modulus n. Ini berarti bahwa untuk modulus n yang cukup besar (yang digunakan dalam praktik kriptografi, misalnya 2048-bit), waktu yang dibutuhkan untuk "memecahkan" masalah ini akan melebihi kemampuan komputasi saat ini dan masa depan yang dapat diperkirakan, bahkan dengan komputer tercepat. Kesulitan komputasi inilah yang menjadi dasar keamanan bagi banyak skema kriptografi kunci publik modern seperti Diffie-Hellman dan ElGamal.
---

## 8. Kesimpulan
Praktikum ini telah memberikan pemahaman mendalam tentang aritmetika modular dan aplikasinya dalam kriptografi. Implementasi fungsi-fungsi seperti aritmetika modular dasar, Greatest Common Divisor (GCD) menggunakan Algoritma Euclidean, Extended Euclidean Algorithm untuk menemukan invers modular, dan simulasi logaritma diskrit sederhana, menunjukkan bagaimana konsep matematika ini diimplementasikan secara praktis.

Konsep-konsep ini merupakan pilar utama di balik keamanan dan fungsionalitas algoritma kriptografi modern. Dari menjaga bilangan dalam rentang yang dapat dikelola hingga menciptakan masalah komputasi yang sulit sebagai dasar keamanan, aritmetika modular dan turunannya memainkan peran krusial dalam pertukaran kunci, enkripsi data, dan memastikan integritas serta kerahasiaan informasi di era digital.
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
