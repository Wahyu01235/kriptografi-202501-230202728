# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern (DES, AES, RSA)
Nama: Achmad Wahyudi
NIM: 230202728
Kelas: 5IKRA

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
Sandi modern menandai pergeseran fundamental dari metode klasik berbasis alfabet ke operasi matematis kompleks pada data biner. Algoritma ini dibagi menjadi dua kategori utama: simetris dan asimetris. Dalam kriptografi kunci-simetris, satu kunci rahasia yang sama digunakan untuk proses enkripsi dan dekripsi. Contoh historis yang paling terkenal adalah Data Encryption Standard (DES). DES, yang diadopsi sebagai standar di Amerika Serikat pada tahun 1977, beroperasi pada blok data 64-bit menggunakan kunci 56-bit. Meskipun sangat berpengaruh, ukuran kuncinya yang 56-bit kini dianggap tidak aman karena rentan terhadap serangan brute force dengan perangkat keras modern.

Sebagai pengganti DES, Advanced Encryption Standard (AES) kini menjadi standar emas global untuk enkripsi simetris. Seperti DES, AES adalah sandi blok, tetapi ia beroperasi pada blok 128-bit dan menawarkan fleksibilitas ukuran kunci yang jauh lebih aman, yaitu 128, 192, atau 256 bit. AES didasarkan pada prinsip substitusi-permutasi yang membuatnya sangat efisien dalam perangkat keras maupun perangkat lunak, serta sangat tahan terhadap berbagai teknik kriptanalisis yang diketahui. Keamanannya yang terbukti dan kinerjanya yang cepat membuatnya ideal untuk mengenkripsi data dalam jumlah besar, mulai dari file di hard drive hingga lalu lintas internet.

Berbeda secara fundamental dengan DES dan AES, RSA (Rivest-Shamir-Adleman) adalah algoritma kriptografi kunci-asimetris atau kunci-publik. Sistem ini menggunakan sepasang kunci yang terhubung secara matematis: kunci publik, yang dapat dibagikan secara bebas, dan kunci privat, yang harus dijaga kerahasiaannya. Data yang dienkripsi dengan kunci publik hanya dapat didekripsi oleh kunci privat yang sesuai. Keamanan RSA bergantung pada kesulitan komputasi untuk memfaktorkan bilangan prima yang sangat besar. Karena operasinya secara signifikan lebih lambat daripada AES, RSA tidak digunakan untuk mengenkripsi data dalam jumlah besar.

Dalam praktiknya, sistem simetris dan asimetris sering digunakan bersama-sama untuk memanfaatkan kekuatan masing-masing. RSA seringkali digunakan untuk tujuan pertukaran kunci secara aman; misalnya, untuk mengenkripsi dan mengirimkan kunci sesi (session key) 128-bit yang dibuat secara acak. Setelah kunci sesi tersebut diterima dan didekripsi dengan aman menggunakan kunci privat penerima, kedua belah pihak kemudian dapat beralih menggunakan enkripsi AES yang jauh lebih cepat untuk sisa komunikasi mereka. Selain itu, RSA juga sangat penting untuk membuat tanda tangan digital, yang berfungsi untuk memverifikasi autentisitas dan integritas pengirim pesan.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Implementasi DES (Opsional, Simulasi)
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
---

### Langkah 2 — Implementasi AES-128
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

### Langkah 3 — Implementasi RSA
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

## 5. Source Code
###DES
```
# des_encryption.py
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

def des_encrypt(plaintext, key):
    """
    Enkripsi teks menggunakan DES
    """
    # Pastikan plaintext dalam bentuk bytes
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # Buat cipher DES
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Padding plaintext agar sesuai dengan block size DES (8 bytes)
    padded_plaintext = pad(plaintext, DES.block_size)
    
    # Enkripsi
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    """
    Dekripsi teks menggunakan DES
    """
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    
    # Unpadding data yang sudah didekripsi
    plaintext = unpad(decrypted_data, DES.block_size)
    return plaintext

def generate_des_key():
    """
    Generate kunci DES 64-bit (8 bytes)
    """
    return get_random_bytes(8)

# Input dari pengguna
print("=" * 60)
print("DES ENCRYPTION/DECRYPTION")
print("=" * 60)

# Pilihan untuk generate key atau input manual
key_choice = input("Generate kunci otomatis? (y/n): ").lower().strip()

if key_choice == 'y':
    key = generate_des_key()
    print(f"Kunci DES yang di-generate (hex): {key.hex()}")
else:
    key_input = input("Masukkan kunci DES (8 karakter, atau hex string 16 digit): ").strip()
    if len(key_input) == 16 and all(c in '0123456789abcdefABCDEF' for c in key_input):
        # Jika input adalah hex string
        key = bytes.fromhex(key_input)
    else:
        # Jika input adalah teks, pastikan panjangnya 8 karakter
        if len(key_input) < 8:
            key_input = key_input.ljust(8, '0')  # Padding dengan 0 jika kurang
        elif len(key_input) > 8:
            key_input = key_input[:8]  # Truncate jika lebih
        key = key_input.encode('utf-8')

plaintext = input("Masukkan plaintext: ")

# Proses enkripsi
try:
    ciphertext = des_encrypt(plaintext, key)
    
    # Output hasil
    print("\n" + "=" * 60)
    print("HASIL DES ENKRIPSI")
    print("=" * 60)
    print(f"Plaintext:      {plaintext}")
    print(f"Kunci (hex):    {key.hex()}")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print(f"Ciphertext (raw): {ciphertext}")
    
    # Proses dekripsi
    decrypted = des_decrypt(ciphertext, key)
    print(f"Decrypted:      {decrypted.decode('utf-8')}")
    
except Exception as e:
    print(f"Error: {e}")
    print("Pastikan kunci valid (8 bytes)")

# Contoh penggunaan multiple blocks
print("\n" + "=" * 60)
print("CONTOH MULTIPLE BLOCKS")
print("=" * 60)

long_plaintext = "Ini adalah contoh teks yang lebih panjang untuk menunjukkan bagaimana DES bekerja dengan multiple blocks"
print(f"Plaintext panjang: {long_plaintext}")

try:
    long_ciphertext = des_encrypt(long_plaintext, key)
    long_decrypted = des_decrypt(long_ciphertext, key)
    
    print(f"Ciphertext length: {len(long_ciphertext)} bytes")
    print(f"Decrypted: {long_decrypted.decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")

```

### AES
```
# aes_encryption.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_encrypt(plaintext, key, mode='EAX'):
    """
    Enkripsi teks menggunakan AES dengan berbagai mode
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    if mode == 'EAX':
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return cipher, ciphertext, tag
    elif mode == 'GCM':
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return cipher, ciphertext, tag
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return cipher, ciphertext, None
    else:
        raise ValueError("Mode tidak didukung")

def aes_decrypt(ciphertext, key, mode, nonce=None, tag=None):
    """
    Dekripsi teks menggunakan AES
    """
    if mode == 'EAX':
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext
    elif mode == 'GCM':
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, nonce=nonce)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext
    else:
        raise ValueError("Mode tidak didukung")

def generate_aes_key(key_size=16):
    """
    Generate kunci AES (16, 24, atau 32 bytes)
    """
    if key_size not in [16, 24, 32]:
        raise ValueError("Key size harus 16, 24, atau 32 bytes")
    return get_random_bytes(key_size)

# Input dari pengguna
print("=" * 60)
print("AES ENCRYPTION/DECRYPTION")
print("=" * 60)

# Pilihan key size
print("Pilih ukuran kunci AES:")
print("1. AES-128 (16 bytes)")
print("2. AES-192 (24 bytes)") 
print("3. AES-256 (32 bytes)")
key_size_choice = input("Masukkan pilihan (1-3, default 1): ").strip() or "1"

key_sizes = {'1': 16, '2': 24, '3': 32}
key_size = key_sizes.get(key_size_choice, 16)

# Pilihan mode
print("\nPilih mode operasi:")
print("1. EAX (recommended)")
print("2. GCM")
print("3. CBC")
mode_choice = input("Masukkan pilihan (1-3, default 1): ").strip() or "1"

modes = {'1': 'EAX', '2': 'GCM', '3': 'CBC'}
mode = modes.get(mode_choice, 'EAX')

# Generate atau input kunci
key_choice = input("\nGenerate kunci otomatis? (y/n): ").lower().strip()

if key_choice == 'y':
    key = generate_aes_key(key_size)
    print(f"Kunci AES-{key_size*8} yang di-generate (hex): {key.hex()}")
else:
    key_input = input(f"Masukkan kunci AES ({key_size} bytes, atau hex string {key_size*2} digit): ").strip()
    if len(key_input) == key_size * 2 and all(c in '0123456789abcdefABCDEF' for c in key_input):
        key = bytes.fromhex(key_input)
    else:
        # Jika input adalah teks, pastikan panjangnya sesuai
        if len(key_input) < key_size:
            key_input = key_input.ljust(key_size, '0')
        elif len(key_input) > key_size:
            key_input = key_input[:key_size]
        key = key_input.encode('utf-8')

plaintext = input("\nMasukkan plaintext: ")

# Proses enkripsi
try:
    if mode in ['EAX', 'GCM']:
        cipher, ciphertext, tag = aes_encrypt(plaintext, key, mode)
        nonce = cipher.nonce
        
        # Output hasil
        print("\n" + "=" * 60)
        print(f"HASIL AES-{key_size*8} {mode} ENKRIPSI")
        print("=" * 60)
        print(f"Plaintext:      {plaintext}")
        print(f"Kunci (hex):    {key.hex()}")
        print(f"Nonce (hex):    {nonce.hex()}")
        print(f"Tag (hex):      {tag.hex()}")
        print(f"Ciphertext (hex): {ciphertext.hex()}")
        
        # Proses dekripsi
        decrypted = aes_decrypt(ciphertext, key, mode, nonce=nonce, tag=tag)
        print(f"Decrypted:      {decrypted.decode('utf-8')}")
        
    elif mode == 'CBC':
        cipher, ciphertext, _ = aes_encrypt(plaintext, key, mode)
        iv = cipher.iv
        
        print("\n" + "=" * 60)
        print(f"HASIL AES-{key_size*8} {mode} ENKRIPSI")
        print("=" * 60)
        print(f"Plaintext:      {plaintext}")
        print(f"Kunci (hex):    {key.hex()}")
        print(f"IV (hex):       {iv.hex()}")
        print(f"Ciphertext (hex): {ciphertext.hex()}")
        
        # Proses dekripsi
        decrypted = aes_decrypt(ciphertext, key, mode, nonce=iv)
        print(f"Decrypted:      {decrypted.decode('utf-8')}")
        
except Exception as e:
    print(f"Error: {e}")

# Contoh performa dengan data besar
print("\n" + "=" * 60)
print("CONTOH DENGAN DATA BESAR")
print("=" * 60)

large_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10
print(f"Data besar ({len(large_data)} karakter)")

try:
    if mode in ['EAX', 'GCM']:
        cipher_large, ciphertext_large, tag_large = aes_encrypt(large_data, key, mode)
        decrypted_large = aes_decrypt(ciphertext_large, key, mode, nonce=cipher_large.nonce, tag=tag_large)
    else:  # CBC
        cipher_large, ciphertext_large, _ = aes_encrypt(large_data, key, mode)
        decrypted_large = aes_decrypt(ciphertext_large, key, mode, nonce=cipher_large.iv)
    
    print(f"Enkripsi & dekripsi data besar berhasil!")
    print(f"Panjang ciphertext: {len(ciphertext_large)} bytes")
    
except Exception as e:
    print(f"Error dengan data besar: {e}")
```

### RSA
```
# rsa_encryption.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

def generate_rsa_keys(key_size=2048):
    """
    Generate key pair RSA
    """
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def rsa_encrypt(plaintext, public_key):
    """
    Enkripsi menggunakan RSA dengan OAEP padding
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    """
    Dekripsi menggunakan RSA
    """
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def rsa_sign(message, private_key):
    """
    Membuat digital signature
    """
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    h = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def rsa_verify(message, signature, public_key):
    """
    Verifikasi digital signature
    """
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    h = SHA256.new(message)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Input dari pengguna
print("=" * 60)
print("RSA ENCRYPTION/DECRYPTION & DIGITAL SIGNATURE")
print("=" * 60)

# Pilihan key size
print("Pilih ukuran kunci RSA:")
print("1. 1024 bit (tidak aman, hanya testing)")
print("2. 2048 bit (recommended)")
print("3. 4096 bit (sangat aman)")
key_size_choice = input("Masukkan pilihan (1-3, default 2): ").strip() or "2"

key_sizes = {'1': 1024, '2': 2048, '3': 4096}
key_size = key_sizes.get(key_size_choice, 2048)

# Generate keys
print(f"\nGenerating RSA-{key_size} key pair...")
private_key, public_key = generate_rsa_keys(key_size)
print("Key pair generated successfully!")

# Tampilkan informasi keys
print(f"\nPublic Key (PEM format):")
print(public_key.export_key().decode('utf-8'))

print(f"\nPrivate Key (PEM format):")
print(private_key.export_key().decode('utf-8'))

# Input plaintext untuk enkripsi
plaintext = input("\nMasukkan plaintext untuk dienkripsi: ")

# Proses enkripsi
try:
    # Enkripsi dengan public key
    ciphertext = rsa_encrypt(plaintext, public_key)
    
    print("\n" + "=" * 60)
    print("HASIL RSA ENKRIPSI")
    print("=" * 60)
    print(f"Plaintext:              {plaintext}")
    print(f"Panjang plaintext:      {len(plaintext)} karakter")
    print(f"Ciphertext (hex):       {ciphertext.hex()}")
    print(f"Panjang ciphertext:     {len(ciphertext)} bytes")
    
    # Dekripsi dengan private key
    decrypted = rsa_decrypt(ciphertext, private_key)
    print(f"Decrypted:              {decrypted.decode('utf-8')}")
    
except Exception as e:
    print(f"Error enkripsi/dekripsi: {e}")
    print("Pastikan plaintext tidak terlalu panjang untuk RSA")

# Digital Signature
print("\n" + "=" * 60)
print("DIGITAL SIGNATURE")
print("=" * 60)

message = input("Masukkan pesan untuk ditandatangani: ")

try:
    # Buat signature
    signature = rsa_sign(message, private_key)
    print(f"\nSignature (hex): {signature.hex()}")
    
    # Verifikasi signature
    is_valid = rsa_verify(message, signature, public_key)
    print(f"Signature valid: {is_valid}")
    
    # Coba verifikasi dengan pesan yang diubah
    tampered_message = message + "tampered"
    is_valid_tampered = rsa_verify(tampered_message, signature, public_key)
    print(f"Signature valid untuk pesan yang diubah: {is_valid_tampered}")
    
except Exception as e:
    print(f"Error signature: {e}")

# Contoh dengan data yang lebih besar (dalam chunks)
print("\n" + "=" * 60)
print("ENKRIPSI DATA BESAR (CHUNKED)")
print("=" * 60)

large_message = "Pesan rahasia yang sangat penting dan panjang " * 5
print(f"Pesan besar: {large_message[:100]}...")

try:
    # Karena RSA memiliki batasan ukuran, kita bagi menjadi chunks
    max_chunk_size = (key_size // 8) - 42  # Untuk OAEP padding
    
    # Enkripsi per chunk
    encrypted_chunks = []
    for i in range(0, len(large_message), max_chunk_size):
        chunk = large_message[i:i + max_chunk_size]
        encrypted_chunk = rsa_encrypt(chunk, public_key)
        encrypted_chunks.append(encrypted_chunk)
    
    print(f"Data dibagi menjadi {len(encrypted_chunks)} chunks")
    print(f"Total ukuran ciphertext: {sum(len(chunk) for chunk in encrypted_chunks)} bytes")
    
    # Dekripsi per chunk
    decrypted_chunks = []
    for encrypted_chunk in encrypted_chunks:
        decrypted_chunk = rsa_decrypt(encrypted_chunk, private_key)
        decrypted_chunks.append(decrypted_chunk.decode('utf-8'))
    
    final_message = ''.join(decrypted_chunks)
    print(f"Dekripsi berhasil: {final_message[:100]}...")
    
except Exception as e:
    print(f"Error dengan data besar: {e}")

# Simpan keys ke file (opsional)
save_choice = input("\nSimpan keys ke file? (y/n): ").lower().strip()
if save_choice == 'y':
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.export_key())
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.export_key())
    print("Keys disimpan sebagai 'private_key.pem' dan 'public_key.pem'")
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
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
    Perbedaan mendasar terletak pada cara pengelolaan kunci. DES dan AES keduanya adalah algoritma simetris, yang berarti mereka menggunakan satu kunci rahasia yang sama untuk enkripsi dan dekripsi. Keamanan sistem ini bergantung sepenuhnya pada terjaganya kerahasiaan kunci tunggal tersebut. Sebaliknya, RSA adalah algoritma asimetris. RSA menggunakan sepasang kunci: kunci publik yang dapat dibagikan secara bebas untuk mengenkripsi data, dan kunci privat yang harus dijaga kerahasiaannya untuk mendekripsi data tersebut. Keamanan RSA tidak bergantung pada kerahasiaan kunci enkripsi (publik), melainkan pada kesulitan matematis untuk menurunkan kunci privat dari kunci publik, yang didasarkan pada sulitnya memfaktorkan bilangan prima besar.
     
2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?
    AES lebih banyak digunakan daripada DES di era modern terutama karena alasan keamanan yang terkait dengan panjang kunci. DES, yang dirancang pada tahun 1970-an, hanya menggunakan kunci 56-bit. Ukuran kunci ini, yang berarti ada $2^{56}$ kemungkinan kunci, kini dianggap tidak aman karena dapat dipecahkan menggunakan serangan brute force dengan perangkat keras komputer modern dalam waktu yang relatif singkat. Sebagai gantinya, AES menawarkan ukuran kunci yang jauh lebih kuat, yaitu 128, 192, atau 256 bit. Ruang kunci minimum $2^{128}$ pada AES secara komputasi tidak praktis untuk diserang dengan metode brute force, sehingga memberikan tingkat keamanan yang jauh lebih tinggi dan sesuai dengan standar keamanan saat ini. Selain itu, AES juga lebih efisien dan memiliki ukuran blok 128-bit yang lebih baik daripada 64-bit milik DES.
   
3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
    RSA dikategorikan sebagai algoritma asimetris karena ia menggunakan sepasang kunci yang berbeda namun terhubung secara matematis: kunci publik dan kunci privat. Tidak seperti algoritma simetris di mana satu kunci melakukan kedua fungsi, pada RSA, data yang dienkripsi oleh kunci publik hanya dapat didekripsi oleh kunci privat yang sesuai. Proses pembangkitan kuncinya dimulai dengan memilih dua bilangan prima acak yang sangat besar, sebut saja $p$ dan $q$. Kedua bilangan ini kemudian dikalikan untuk menghasilkan modulus, $n = p \cdot q$. Selanjutnya, dihitung nilai totient Euler, $\phi(n) = (p-1) \cdot (q-1)$. Setelah itu, dipilih sebuah eksponen publik $e$ (angka ganjil kecil yang relatif prima terhadap $\phi(n)$). Terakhir, eksponen privat $d$ dihitung sebagai invers modular dari $e$ terhadap $\phi(n)$. Kunci publik adalah pasangan $(e, n)$, sedangkan kunci privat adalah pasangan $(d, n)$.

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
