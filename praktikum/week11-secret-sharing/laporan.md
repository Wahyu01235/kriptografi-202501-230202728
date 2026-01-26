# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: Secret Sharing (Shamir’s Secret Sharing)  
Nama: Achmad Wahyudi   
NIM: 230202728 
Kelas: 5IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.


---

## 2. Dasar Teori
Secret Sharing merupakan teknik kriptografi yang bertujuan membagi suatu rahasia menjadi beberapa bagian (share) yang didistribusikan kepada sejumlah pihak, dengan ketentuan bahwa hanya kombinasi sejumlah minimum share tertentu yang dapat digunakan untuk merekonstruksi kembali rahasia tersebut. Pendekatan ini dirancang untuk menghilangkan masalah single point of failure, di mana keamanan tidak lagi bergantung pada satu entitas atau satu kunci saja. Skema secret sharing umumnya dinyatakan dalam bentuk (k, n), yang berarti rahasia dibagi menjadi n share dan minimal k share diperlukan untuk rekonstruksi, sementara kurang dari k share tidak memberikan informasi apa pun tentang rahasia.

Shamir’s Secret Sharing, yang diperkenalkan oleh Adi Shamir pada tahun 1979, merupakan skema secret sharing yang paling dikenal dan digunakan secara luas. Skema ini memanfaatkan sifat matematis polinomial dalam medan hingga, di mana rahasia direpresentasikan sebagai konstanta dari sebuah polinomial acak berderajat (k − 1). Setiap share dibentuk sebagai pasangan titik 
(𝑥, 𝑓(𝑥)) pada polinomial tersebut, dengan perhitungan dilakukan secara modulo bilangan prima yang cukup besar. Keamanan skema ini bergantung pada fakta bahwa sebuah polinomial berderajat (k − 1) hanya dapat direkonstruksi secara unik jika tersedia minimal k titik yang berbeda.

Proses rekonstruksi rahasia pada Shamir’s Secret Sharing dilakukan menggunakan interpolasi Lagrange, yaitu metode matematis untuk menentukan nilai polinomial pada titik tertentu berdasarkan sejumlah titik yang diketahui. Dalam konteks ini, rahasia diperoleh dengan menghitung nilai polinomial pada 𝑥=0 menggunakan minimal k share yang valid. Jika jumlah share yang digunakan kurang dari threshold k, maka proses interpolasi tidak dapat menghasilkan solusi tunggal, sehingga nilai rahasia tetap tidak dapat ditentukan.

Shamir’s Secret Sharing memiliki sifat information-theoretic security, yang berarti keamanannya tidak bergantung pada keterbatasan daya komputasi penyerang. Bahkan dengan kemampuan komputasi tak terbatas, penyerang tetap tidak dapat memperoleh informasi apa pun tentang rahasia jika jumlah share yang dimiliki kurang dari k. Dalam praktik, skema ini banyak digunakan pada manajemen kunci kriptografi terdistribusi, pemulihan kunci privat cryptocurrency, dan sistem keamanan yang memerlukan pembagian kepercayaan antar pihak. Meskipun demikian, keamanan praktisnya tetap bergantung pada kualitas implementasi, termasuk pemilihan bilangan prima, generator bilangan acak, dan keamanan penyimpanan share.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Implementasi Shamir Secret Sharing
Contoh sederhana dengan library `secretsharing`:

```python
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
```

---

### Langkah 2 — Simulasi Manual (Tanpa Library)
Mahasiswa juga dapat mencoba membuat implementasi manual berbasis **polinomial modulo p** untuk memahami konsep matematis.  
- Pilih bilangan prima p yang cukup besar.  
- Bangun polinomial f(x) = a0 + a1x + … + ak-1x^(k-1) mod p, dengan a0 = secret.  
- Bagikan (x, f(x)) sebagai share.  
- Rekonstruksi menggunakan **Lagrange Interpolation**.  

---

### Langkah 3 — Analisis Keamanan
Diskusikan:
- Mengapa skema (k, n) aman meskipun sebagian share bocor?  
- Apa risiko jika threshold k terlalu kecil atau terlalu besar?  
- Bagaimana penerapan SSS di dunia nyata (contoh: manajemen kunci cryptocurrency, recovery password)?

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# ==========================================================
# SHAMIR SECRET SHARING
# Library-based and Manual Implementation (All-in-One)
# Python 3.11+
# ==========================================================

import random
from functools import reduce

# ==========================================================
# PART 1 — LIBRARY VERSION (REFERENCE ONLY)
# ==========================================================

def library_version():
    print("\n=== LIBRARY VERSION (REFERENCE) ===")

    try:
        from secretsharing import SecretSharer
    except ImportError:
        print("Library 'secretsharing' belum terinstall.")
        print("Install dengan: pip install secretsharing")
        return

    secret = "KriptografiUPB2025"
    k, n = 3, 5

    print("Secret:", secret)
    print(f"Threshold k = {k}, Total shares n = {n}")

    shares = SecretSharer.split_secret(secret, k, n)

    print("\nGenerated Shares:")
    for s in shares:
        print(s)

    recovered = SecretSharer.recover_secret(shares[:k])
    print("\nRecovered Secret:", recovered)


# ==========================================================
# PART 2 — MANUAL IMPLEMENTATION
# ==========================================================

def string_to_int(s: str) -> int:
    return int.from_bytes(s.encode(), "big")


def int_to_string(i: int) -> str:
    length = (i.bit_length() + 7) // 8
    return i.to_bytes(length, "big").decode()


def mod_inverse(a, p):
    return pow(a, -1, p)


def generate_polynomial(secret_int, k, p):
    coeffs = [secret_int]
    for _ in range(1, k):
        coeffs.append(random.randint(0, p - 1))
    return coeffs


def evaluate_polynomial(coeffs, x, p):
    result = 0
    for power, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, power, p)) % p
    return result


def generate_shares(secret, k, n, p):
    secret_int = string_to_int(secret)
    coeffs = generate_polynomial(secret_int, k, p)

    shares = []
    for x in range(1, n + 1):
        y = evaluate_polynomial(coeffs, x, p)
        shares.append((x, y))

    return shares


def lagrange_interpolation(shares, p):
    def basis(j):
        xj, _ = shares[j]
        acc = 1
        for m in range(len(shares)):
            if m != j:
                xm, _ = shares[m]
                acc = (acc * (-xm) * mod_inverse(xj - xm, p)) % p
        return acc

    secret = 0
    for j in range(len(shares)):
        _, yj = shares[j]
        secret = (secret + yj * basis(j)) % p

    return secret


def manual_version():
    print("\n=== MANUAL VERSION (POLYNOMIAL MOD p) ===")

    secret = "KriptografiUPB2025"
    k, n = 3, 5

    # Bilangan prima besar
    p = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    print("Secret:", secret)
    print(f"Threshold k = {k}, Total shares n = {n}")

    shares = generate_shares(secret, k, n, p)

    print("\nGenerated Shares:")
    for s in shares:
        print(s)

    selected = shares[:k]
    recovered_int = lagrange_interpolation(selected, p)
    recovered_secret = int_to_string(recovered_int)

    print("\nRecovered Secret:", recovered_secret)


# ==========================================================
# MAIN ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    print("SHAMIR SECRET SHARING PRACTICUM")
    print("--------------------------------")

    library_version()
    manual_version()
    print("\n=== END OF PRACTICUM ===\n")
```

## 6. Hasil dan Pembahasan
Skema (k, n) pada Shamir’s Secret Sharing tetap aman meskipun sebagian share bocor karena keamanannya bersifat information-theoretic. Setiap share merupakan titik pada polinomial acak berderajat (k − 1) yang dibangun di atas medan hingga. Selama jumlah share yang dimiliki penyerang kurang dari threshold k, masih terdapat banyak kemungkinan polinomial yang konsisten dengan share tersebut, sehingga nilai rahasia tidak dapat ditentukan secara unik. Dengan kata lain, kebocoran sebagian share tidak mengurangi tingkat ketidakpastian terhadap rahasia, sehingga penyerang tidak memperoleh informasi parsial apa pun, terlepas dari kemampuan komputasi yang dimiliki.

Pemilihan nilai threshold k memiliki implikasi langsung terhadap keseimbangan antara keamanan dan ketersediaan sistem. Jika k terlalu kecil, risiko kolusi meningkat karena hanya sedikit pihak yang diperlukan untuk merekonstruksi rahasia, sehingga sistem menjadi rentan terhadap penyalahgunaan internal. Sebaliknya, jika k terlalu besar, sistem menjadi rapuh terhadap kehilangan share, karena kegagalan satu atau dua pihak saja dapat membuat rahasia tidak dapat direkonstruksi sama sekali. Oleh karena itu, penentuan k bukan sekadar parameter teknis, melainkan keputusan desain yang mencerminkan asumsi kepercayaan dan risiko operasional dalam sistem yang dibangun.

Dalam praktik, Shamir’s Secret Sharing banyak diterapkan pada sistem yang memerlukan distribusi kepercayaan dan toleransi terhadap kegagalan. Pada manajemen kunci cryptocurrency, misalnya, private key dibagi ke beberapa pihak atau perangkat sehingga tidak ada satu entitas pun yang memegang kendali penuh atas aset digital. Pada mekanisme recovery password atau key escrow tingkat tinggi, SSS digunakan untuk memastikan bahwa pemulihan hanya dapat dilakukan melalui persetujuan kolektif sejumlah pihak tertentu. Meskipun demikian, Shamir’s Secret Sharing tidak melindungi dari kompromi endpoint atau kolusi yang memenuhi threshold k, sehingga penerapannya harus dikombinasikan dengan kontrol keamanan tambahan seperti audit, kebijakan akses, dan perlindungan penyimpanan share.
---

## 7. Jawaban Pertanyaan
1. Keuntungan utama Shamir Secret Sharing dibandingkan membagikan salinan kunci secara langsung

Keuntungan utama Shamir Secret Sharing dibandingkan pembagian salinan kunci secara langsung adalah kemampuannya menghilangkan single point of failure. Pada pembagian salinan kunci, setiap pihak memegang kunci utuh sehingga kebocoran pada satu pihak saja sudah cukup untuk mengkompromikan seluruh sistem. Sebaliknya, pada Shamir Secret Sharing, tidak ada satu pun share yang mengandung informasi rahasia secara mandiri. Rahasia hanya dapat direkonstruksi apabila jumlah share yang dikumpulkan memenuhi threshold yang telah ditentukan, sehingga kebocoran sebagian share tidak berdampak pada keamanan rahasia secara keseluruhan.

2. Peran threshold (k) dalam keamanan secret sharing

Threshold (k) berperan sebagai parameter utama yang menentukan tingkat keamanan dan ketersediaan sistem secret sharing. Nilai k menetapkan jumlah minimum share yang diperlukan untuk merekonstruksi rahasia, sekaligus menjadi batas keamanan terhadap kebocoran. Selama jumlah share yang dimiliki penyerang kurang dari k, rahasia tetap tidak dapat ditentukan secara matematis. Dengan demikian, threshold (k) merepresentasikan keseimbangan antara perlindungan terhadap kolusi dan toleransi terhadap kehilangan share dalam suatu sistem terdistribusi.

3. Contoh skenario nyata penerapan Shamir Secret Sharing

Salah satu contoh penerapan nyata Shamir Secret Sharing adalah pada manajemen kunci privat cryptocurrency. Dalam skenario ini, kunci privat tidak disimpan oleh satu individu atau satu perangkat, melainkan dibagi ke beberapa pihak atau lokasi berbeda. Rekonstruksi kunci hanya dapat dilakukan apabila sejumlah pihak yang memenuhi threshold (k) bekerja sama. Pendekatan ini secara signifikan mengurangi risiko pencurian aset digital akibat kompromi satu pihak, serta meningkatkan keamanan dan keandalan pengelolaan kunci kriptografi.

---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Shamir’s Secret Sharing merupakan metode kriptografi yang efektif untuk membagi dan mengamankan suatu rahasia dalam sistem terdistribusi. Melalui implementasi menggunakan library dan implementasi manual berbasis polinomial modulo bilangan prima, terbukti bahwa rahasia hanya dapat direkonstruksi apabila jumlah share yang digunakan memenuhi threshold yang telah ditentukan. Sebaliknya, penggunaan jumlah share di bawah threshold tidak memungkinkan rekonstruksi rahasia, yang menunjukkan bahwa mekanisme keamanan skema (k, n) bekerja sesuai dengan teori.

Praktikum ini juga memperlihatkan bahwa keamanan Shamir’s Secret Sharing bersifat information-theoretic, di mana kebocoran sebagian share tidak memberikan informasi parsial apa pun mengenai rahasia. Hal ini dikarenakan setiap share merupakan titik pada polinomial acak yang dibangun di atas medan hingga, sehingga tanpa jumlah share yang cukup, terdapat banyak kemungkinan polinomial yang konsisten dengan share tersebut. Dengan demikian, keamanan skema tidak bergantung pada kekuatan komputasi penyerang, melainkan pada struktur matematis yang digunakan.

Selain aspek keamanan, praktikum ini menegaskan pentingnya pemilihan parameter, khususnya nilai threshold (k) dan bilangan prima modulus. Nilai threshold yang terlalu kecil meningkatkan risiko kolusi, sedangkan threshold yang terlalu besar dapat menurunkan ketersediaan sistem apabila terjadi kehilangan share. Oleh karena itu, penentuan parameter harus mempertimbangkan keseimbangan antara keamanan dan keandalan operasional sistem.

Secara keseluruhan, praktikum Shamir’s Secret Sharing memberikan pemahaman yang komprehensif mengenai konsep secret sharing, baik dari sisi teori maupun implementasi. Hasil praktikum menunjukkan bahwa Shamir’s Secret Sharing sangat relevan untuk diterapkan pada sistem keamanan modern yang memerlukan distribusi kepercayaan, seperti manajemen kunci kriptografi dan mekanisme pemulihan rahasia, dengan catatan bahwa implementasinya harus didukung oleh kebijakan keamanan dan pengelolaan sistem yang memadai.

---

## 9. Daftar Pustaka
Shamir, A. (1979). How to Share a Secret. Communications of the ACM, 22(11), 612–613.
Stinson, D. R. (2019). Cryptography: Theory and Practice (4th ed.). Boca Raton: CRC Press.
Katz, J., & Lindell, Y. (2021). Introduction to Modern Cryptography (3rd ed.). Boca Raton: CRC Press.
Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. Boca Raton: CRC Press.
Paar, C., & Pelzl, J. (2010). Understanding Cryptography: A Textbook for Students and Practitioners. Heidelberg: Springer.

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
