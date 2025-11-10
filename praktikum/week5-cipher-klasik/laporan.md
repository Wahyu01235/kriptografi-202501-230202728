# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik:  Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Achmad Wahyudi
NIM: 230202728
Kelas: 5IKRA

---

## 1. Tujuan
1. Menerapkan algoritma **Caesar Cipher** untuk enkripsi dan dekripsi teks.  
2. Menerapkan algoritma **Vigenère Cipher** dengan variasi kunci.  
3. Mengimplementasikan algoritma transposisi sederhana.  
4. Menjelaskan kelemahan algoritma kriptografi klasik.  

## 2. Dasar Teori
Sandi klasik merupakan fondasi dari kriptografi yang mengandalkan teknik-teknik manual berbasis alfabet, sebelum ditemukannya komputasi digital. Salah satu contoh paling sederhana adalah Sandi Caesar, sebuah sandi substitusi monoalfabetik. Cara kerjanya adalah dengan menggeser setiap huruf dalam pesan asli (plaintext) sejauh jumlah tetap tertentu dalam urutan alfabet. Kunci dari sandi ini adalah angka pergeseran tersebut, misalnya geser 3 huruf. Kelemahan utamanya adalah keamanannya yang sangat rendah; karena hanya ada 25 kemungkinan kunci (untuk alfabet Inggris), sandi ini dapat dengan mudah dipecahkan menggunakan analisis frekuensi, di mana penyerang mencari huruf yang paling sering muncul dalam pesan terenkripsi (ciphertext).

Sebagai pengembangan untuk mengatasi kelemahan Sandi Caesar, Sandi Vigenère diperkenalkan. Ini adalah sandi substitusi polialfabetik yang menggunakan sebuah kata kunci, bukan hanya satu angka pergeseran. Setiap huruf pada kata kunci menentukan pergeseran yang berbeda untuk setiap huruf pada plaintext, biasanya berdasarkan tabel Vigenère. Hal ini membuat frekuensi huruf dalam ciphertext menjadi lebih merata dan tahan terhadap analisis frekuensi sederhana, karena huruf yang sama pada plaintext bisa dienkripsi menjadi huruf yang berbeda di ciphertext. Meskipun jauh lebih kuat daripada Sandi Caesar, Sandi Vigenère akhirnya dapat dipecahkan, salah satunya dengan metode Kasiski untuk menentukan panjang kata kunci.

Berbeda dengan dua sandi substitusi sebelumnya, Sandi Transposisi bekerja dengan prinsip yang berbeda. Sandi ini tidak mengganti huruf dengan huruf lain, melainkan mengacak atau mengubah urutan posisi huruf-huruf dalam plaintext. Metode yang umum adalah transposisi kolom, di mana pesan ditulis dalam baris-baris di bawah sebuah kata kunci, dan ciphertext dibentuk dengan membaca kolom-kolom tersebut dalam urutan yang ditentukan oleh kata kunci. Kelemahan utama dari sandi transposisi murni adalah frekuensi kemunculan setiap huruf dalam ciphertext sama persis dengan frekuensi di plaintext, sehingga masih rentan terhadap analisis statistik meskipun urutannya telah diubah.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Implementasi Caesar Cipher
```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 2 — Implementasi Vigenère Cipher
```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 3 — Implementasi Transposisi Sederhana
```python
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

## 5. Source Code
### Caesar Cipher
```
# caesar_cipher_enhanced.py
def caesar_encrypt(plaintext, key):
    """
    Mengenkripsi teks menggunakan Caesar Cipher dengan preservasi case.
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        key (int): Kunci pergeseran (0-25)
    
    Returns:
        str: Teks terenkripsi
    """
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    """
    Mendekripsi teks menggunakan Caesar Cipher.
    
    Args:
        ciphertext (str): Teks yang akan didekripsi
        key (int): Kunci pergeseran (0-25)
    
    Returns:
        str: Teks terdekripsi
    """
    return caesar_encrypt(ciphertext, -key)

def caesar_brute_force(ciphertext):
    """
    Menampilkan semua kemungkinan dekripsi untuk Caesar Cipher.
    
    Args:
        ciphertext (str): Teks terenkripsi
    """
    print("\nBrute Force Attack Results:")
    print("-" * 40)
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        print(f"Key {key:2d}: {decrypted}")

def caesar_analyze_frequency(ciphertext):
    """
    Analisis frekuensi karakter untuk membantu cryptanalysis.
    
    Args:
        ciphertext (str): Teks terenkripsi
    """
    # Hanya analisis huruf
    letters = [char.upper() for char in ciphertext if char.isalpha()]
    if not letters:
        print("Tidak ada huruf untuk dianalisis.")
        return
    
    total_letters = len(letters)
    freq = {}
    
    for char in letters:
        freq[char] = freq.get(char, 0) + 1
    
    # Konversi ke persentase
    for char in freq:
        freq[char] = (freq[char] / total_letters) * 100
    
    # Urutkan berdasarkan frekuensi
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    print("\nFrequency Analysis:")
    print("-" * 25)
    for char, percentage in sorted_freq[:8]:  # Tampilkan 8 teratas
        print(f"{char}: {percentage:.2f}%")
    
    # Frekuensi normal bahasa Inggris untuk perbandingan
    english_freq = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
        'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25
    }
    
    print("\nEnglish Letter Frequency (for comparison):")
    for char, percentage in list(english_freq.items())[:5]:
        print(f"{char}: {percentage:.1f}%")

def demo_caesar():
    """
    Demonstrasi fungsi Caesar Cipher.
    """
    print("=== CAESAR CIPHER DEMONSTRATION ===")
    
    # Test case 1
    msg = "HELLO WORLD"
    key = 3
    enc = caesar_encrypt(msg, key)
    dec = caesar_decrypt(enc, key)
    
    print(f"Plaintext:  {msg}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {enc}")
    print(f"Decrypted:  {dec}")
    
    # Test case 2 - dengan karakter non-alfabet
    msg2 = "Hello, Python 3.9!"
    key2 = 7
    enc2 = caesar_encrypt(msg2, key2)
    dec2 = caesar_decrypt(enc2, key2)
    
    print(f"\nPlaintext:  {msg2}")
    print(f"Key:        {key2}")
    print(f"Encrypted:  {enc2}")
    print(f"Decrypted:  {dec2}")
    
    # Test case 3 - Brute force
    ciphertext = "KHOOR ZRUOG"
    print(f"\nBrute force example for: '{ciphertext}'")
    caesar_brute_force(ciphertext)
    
    # Test case 4 - Frequency analysis
    print(f"\nFrequency analysis for: '{ciphertext}'")
    caesar_analyze_frequency(ciphertext)

def input_caesar():
    """
    Fungsi input interaktif untuk Caesar Cipher.
    """
    print("\n" + "="*50)
    print("CAESAR CIPHER - INPUT INTERAKTIF")
    print("="*50)
    
    while True:
        print("\nPilih operasi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Brute Force Attack")
        print("4. Analisis Frekuensi")
        print("5. Kembali ke Menu Utama")
        
        choice = input("Masukkan pilihan (1-5): ").strip()
        
        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            try:
                key = int(input("Masukkan key (0-25): "))
                if key < 0 or key > 25:
                    print("Key harus antara 0-25!")
                    continue
                encrypted = caesar_encrypt(plaintext, key)
                print(f"\nHasil Enkripsi: {encrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            try:
                key = int(input("Masukkan key (0-25): "))
                if key < 0 or key > 25:
                    print("Key harus antara 0-25!")
                    continue
                decrypted = caesar_decrypt(ciphertext, key)
                print(f"\nHasil Dekripsi: {decrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '3':
            ciphertext = input("Masukkan ciphertext untuk brute force: ")
            caesar_brute_force(ciphertext)
            
        elif choice == '4':
            ciphertext = input("Masukkan ciphertext untuk analisis frekuensi: ")
            caesar_analyze_frequency(ciphertext)
            
        elif choice == '5':
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("CAESAR CIPHER PROGRAM")
        print("="*50)
        print("1. Lihat Demo")
        print("2. Input Interaktif")
        print("3. Keluar")
        
        main_choice = input("Pilih menu (1-3): ").strip()
        
        if main_choice == '1':
            demo_caesar()
        elif main_choice == '2':
            input_caesar()
        elif main_choice == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
```
### Vigenere Chiper
```
# vigenere_cipher_enhanced.py
def preprocess_key(key):
    """
    Membersihkan dan memproses kunci untuk Vigenère Cipher.
    
    Args:
        key (str): Kunci input
    
    Returns:
        str: Kunci yang sudah diproses (huruf kecil)
    """
    return ''.join(char.lower() for char in key if char.isalpha())

def vigenere_encrypt(plaintext, key):
    """
    Mengenkripsi teks menggunakan Vigenère Cipher.
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        key (str): Kunci enkripsi
    
    Returns:
        str: Teks terenkripsi
    """
    result = []
    processed_key = preprocess_key(key)
    
    if not processed_key:
        raise ValueError("Key harus mengandung setidaknya satu huruf")
    
    key_index = 0
    key_length = len(processed_key)
    
    for char in plaintext:
        if char.isalpha():
            # Hitung shift dari kunci
            shift = ord(processed_key[key_index % key_length]) - 97
            
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            
            key_index += 1
        else:
            result.append(char)
    
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    """
    Mendekripsi teks menggunakan Vigenère Cipher.
    
    Args:
        ciphertext (str): Teks yang akan didekripsi
        key (str): Kunci dekripsi
    
    Returns:
        str: Teks terdekripsi
    """
    result = []
    processed_key = preprocess_key(key)
    
    if not processed_key:
        raise ValueError("Key harus mengandung setidaknya satu huruf")
    
    key_index = 0
    key_length = len(processed_key)
    
    for char in ciphertext:
        if char.isalpha():
            # Hitung shift dari kunci (negatif untuk dekripsi)
            shift = ord(processed_key[key_index % key_length]) - 97
            
            if char.isupper():
                result.append(chr((ord(char) - 65 - shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - shift) % 26 + 97))
            
            key_index += 1
        else:
            result.append(char)
    
    return "".join(result)

def vigenere_analyze_key_length(ciphertext, max_key_length=10):
    """
    Menganalisis panjang kunci yang mungkin menggunakan Index of Coincidence.
    
    Args:
        ciphertext (str): Teks terenkripsi
        max_key_length (int): Panjang kunci maksimum yang akan dianalisis
    """
    # Hanya analisis huruf
    text = ''.join(char.upper() for char in ciphertext if char.isalpha())
    
    if len(text) < 2:
        print("Teks terlalu pendek untuk analisis.")
        return
    
    print(f"\nKey Length Analysis (max: {max_key_length}):")
    print("-" * 45)
    
    for key_len in range(1, max_key_length + 1):
        # Pisahkan menjadi kelompok berdasarkan suspected key length
        groups = [''] * key_len
        for i, char in enumerate(text):
            groups[i % key_len] += char
        
        # Hitung Index of Coincidence untuk setiap kelompok
        total_ic = 0
        valid_groups = 0
        
        for group in groups:
            if len(group) > 1:
                freq = {}
                for char in group:
                    freq[char] = freq.get(char, 0) + 1
                
                # Hitung IC
                ic = sum(f * (f - 1) for f in freq.values()) / (len(group) * (len(group) - 1))
                total_ic += ic
                valid_groups += 1
        
        if valid_groups > 0:
            avg_ic = total_ic / valid_groups
            # IC untuk English ~0.065, random text ~0.038
            print(f"Key length {key_len}: IC = {avg_ic:.4f} {'*' if avg_ic > 0.055 else ''}")

def vigenere_frequency_analysis(ciphertext, key_length):
    """
    Analisis frekuensi untuk setiap posisi dalam kunci.
    
    Args:
        ciphertext (str): Teks terenkripsi
        key_length (int): Panjang kunci yang diduga
    """
    text = ''.join(char.upper() for char in ciphertext if char.isalpha())
    
    print(f"\nFrequency Analysis for Key Length {key_length}:")
    print("-" * 50)
    
    for i in range(key_length):
        segment = text[i::key_length]  # Ambil setiap karakter ke-i
        if segment:
            freq = {}
            total_chars = len(segment)
            
            for char in segment:
                freq[char] = freq.get(char, 0) + 1
            
            # Konversi ke persentase
            for char in freq:
                freq[char] = (freq[char] / total_chars) * 100
            
            # Cari huruf paling sering
            most_common = max(freq.items(), key=lambda x: x[1])
            # Dalam English, 'E' adalah yang paling umum (12.7%)
            # Jadi shift = (most_common - 'E') mod 26
            shift = (ord(most_common[0]) - ord('E')) % 26
            
            print(f"Position {i}: most common '{most_common[0]}' ({most_common[1]:.1f}%) -> shift ~{shift}")

def demo_vigenere():
    """
    Demonstrasi fungsi Vigenère Cipher.
    """
    print("=== VIGENÈRE CIPHER DEMONSTRATION ===")
    
    # Test case 1
    msg = "ATTACK AT DAWN"
    key = "KEY"
    enc = vigenere_encrypt(msg, key)
    dec = vigenere_decrypt(enc, key)
    
    print(f"Plaintext:  {msg}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {enc}")
    print(f"Decrypted:  {dec}")
    
    # Test case 2 - dengan karakter non-alfabet
    msg2 = "Hello, World! 123"
    key2 = "SECRET"
    enc2 = vigenere_encrypt(msg2, key2)
    dec2 = vigenere_decrypt(enc2, key2)
    
    print(f"\nPlaintext:  {msg2}")
    print(f"Key:        {key2}")
    print(f"Encrypted:  {enc2}")
    print(f"Decrypted:  {dec2}")
    
    # Test case 3 - Analisis kriptografi
    ciphertext = "LXFOPVEFRNHR"
    print(f"\nCryptanalysis for: '{ciphertext}'")
    vigenere_analyze_key_length(ciphertext)
    vigenere_frequency_analysis(ciphertext, 3)

def input_vigenere():
    """
    Fungsi input interaktif untuk Vigenère Cipher.
    """
    print("\n" + "="*50)
    print("VIGENÈRE CIPHER - INPUT INTERAKTIF")
    print("="*50)
    
    while True:
        print("\nPilih operasi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Analisis Panjang Kunci")
        print("4. Analisis Frekuensi")
        print("5. Kembali ke Menu Utama")
        
        choice = input("Masukkan pilihan (1-5): ").strip()
        
        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            key = input("Masukkan key: ")
            try:
                encrypted = vigenere_encrypt(plaintext, key)
                print(f"\nHasil Enkripsi: {encrypted}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            key = input("Masukkan key: ")
            try:
                decrypted = vigenere_decrypt(ciphertext, key)
                print(f"\nHasil Dekripsi: {decrypted}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            ciphertext = input("Masukkan ciphertext untuk analisis panjang kunci: ")
            try:
                max_length = int(input("Masukkan panjang kunci maksimum (default 10): ") or "10")
                vigenere_analyze_key_length(ciphertext, max_length)
            except ValueError:
                print("Panjang kunci harus berupa angka!")
                
        elif choice == '4':
            ciphertext = input("Masukkan ciphertext untuk analisis frekuensi: ")
            try:
                key_length = int(input("Masukkan panjang kunci yang diduga: "))
                vigenere_frequency_analysis(ciphertext, key_length)
            except ValueError:
                print("Panjang kunci harus berupa angka!")
                
        elif choice == '5':
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("VIGENÈRE CIPHER PROGRAM")
        print("="*50)
        print("1. Lihat Demo")
        print("2. Input Interaktif")
        print("3. Keluar")
        
        main_choice = input("Pilih menu (1-3): ").strip()
        
        if main_choice == '1':
            demo_vigenere()
        elif main_choice == '2':
            input_vigenere()
        elif main_choice == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
```
### Transpose Cipher
```
# transposition_cipher_enhanced.py
import math

def transpose_encrypt(plaintext, key=5, padding='X'):
    """
    Mengenkripsi teks menggunakan Transposition Cipher.
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        key (int): Jumlah kolom (panjang kunci)
        padding (str): Karakter untuk mengisi kekosongan
    
    Returns:
        str: Teks terenkripsi
    """
    # Bersihkan teks (opsional: bisa dihapus jika ingin preservasi spasi)
    clean_text = plaintext.replace(" ", "").upper()
    
    # Hitung jumlah baris yang dibutuhkan
    num_rows = math.ceil(len(clean_text) / key)
    
    # Buat matriks
    matrix = [[''] * key for _ in range(num_rows)]
    
    # Isi matriks dengan plaintext
    for i, char in enumerate(clean_text):
        row = i // key
        col = i % key
        matrix[row][col] = char
    
    # Tambahkan padding jika diperlukan
    if len(clean_text) % key != 0:
        for col in range(len(clean_text) % key, key):
            matrix[-1][col] = padding
    
    # Baca per kolom untuk mendapatkan ciphertext
    ciphertext = ''
    for col in range(key):
        for row in range(num_rows):
            ciphertext += matrix[row][col]
    
    return ciphertext

def transpose_decrypt(ciphertext, key=5):
    """
    Mendekripsi teks menggunakan Transposition Cipher.
    
    Args:
        ciphertext (str): Teks yang akan didekripsi
        key (int): Jumlah kolom (panjang kunci)
    
    Returns:
        str: Teks terdekripsi
    """
    # Hitung dimensi matriks
    total_chars = len(ciphertext)
    num_rows = math.ceil(total_chars / key)
    num_shaded = (num_rows * key) - total_chars
    
    # Buat matriks kosong
    matrix = [[''] * key for _ in range(num_rows)]
    
    # Isi matriks per kolom (cara enkripsi)
    index = 0
    for col in range(key):
        for row in range(num_rows):
            # Handle shaded boxes di baris terakhir
            if row == num_rows - 1 and col >= key - num_shaded:
                continue
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1
    
    # Baca per baris untuk mendapatkan plaintext
    plaintext = ''
    for row in range(num_rows):
        for col in range(key):
            plaintext += matrix[row][col]
    
    return plaintext

def transpose_encrypt_preserve_spaces(plaintext, key=5, padding='X'):
    """
    Versi enkripsi yang mempertahankan spasi.
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        key (int): Jumlah kolom
        padding (str): Karakter padding
    
    Returns:
        str: Teks terenkripsi
    """
    # Pisahkan kata-kata
    words = plaintext.split()
    encrypted_words = []
    
    for word in words:
        encrypted_word = transpose_encrypt(word, key, padding)
        encrypted_words.append(encrypted_word)
    
    return ' '.join(encrypted_words)

def transpose_decrypt_preserve_spaces(ciphertext, key=5):
    """
    Versi dekripsi yang mempertahankan spasi.
    
    Args:
        ciphertext (str): Teks terenkripsi
        key (int): Jumlah kolom
    
    Returns:
        str: Teks terdekripsi
    """
    # Pisahkan kata-kata terenkripsi
    encrypted_words = ciphertext.split()
    decrypted_words = []
    
    for word in encrypted_words:
        decrypted_word = transpose_decrypt(word, key)
        decrypted_words.append(decrypted_word)
    
    return ' '.join(decrypted_words)

def transpose_brute_force(ciphertext, max_key=10):
    """
    Mencoba semua kunci yang mungkin untuk Transposition Cipher.
    
    Args:
        ciphertext (str): Teks terenkripsi
        max_key (int): Kunci maksimum yang akan dicoba
    """
    print(f"\nBrute Force Attack (max key: {max_key}):")
    print("-" * 50)
    
    # Hanya coba kunci yang valid (2 <= key < panjang ciphertext)
    possible_keys = [k for k in range(2, min(max_key + 1, len(ciphertext))) 
                    if len(ciphertext) % k == 0 or k <= len(ciphertext)]
    
    found_valid = False
    for key in possible_keys:
        try:
            decrypted = transpose_decrypt(ciphertext, key)
            # Beri rating berdasarkan kemungkinan kata bahasa Inggris
            common_words = ['THE', 'AND', 'ING', 'ION', 'ENT', 'FOR', 'THAT', 'WITH']
            score = sum(1 for word in common_words if word in decrypted)
            
            if score > 0:
                print(f"Key {key}: {decrypted} [score: {score}]")
                found_valid = True
        except:
            continue
    
    if not found_valid:
        print("Tidak ditemukan hasil yang tampak valid.")
        # Tampilkan beberapa hasil meski score 0
        for key in possible_keys[:3]:  # Tampilkan 3 pertama
            try:
                decrypted = transpose_decrypt(ciphertext, key)
                print(f"Key {key}: {decrypted}")
            except:
                continue

def demo_transposition():
    """
    Demonstrasi fungsi Transposition Cipher.
    """
    print("=== TRANSPOSITION CIPHER DEMONSTRATION ===")
    
    # Test case 1 - Basic
    msg = "WEAREDISCOVEREDFLEEATONCE"
    key = 6
    enc = transpose_encrypt(msg, key)
    dec = transpose_decrypt(enc, key)
    
    print(f"Plaintext:  {msg}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {enc}")
    print(f"Decrypted:  {dec}")
    
    # Test case 2 - Dengan spasi
    msg2 = "HELLO WORLD"
    key2 = 4
    enc2 = transpose_encrypt_preserve_spaces(msg2, key2)
    dec2 = transpose_decrypt_preserve_spaces(enc2, key2)
    
    print(f"\nPlaintext:  {msg2}")
    print(f"Key:        {key2}")
    print(f"Encrypted:  {enc2}")
    print(f"Decrypted:  {dec2}")
    
    # Test case 3 - Brute force
    ciphertext = "WAEICVRDLREEOCEEDFTEANOE"
    print(f"\nBrute force example for: '{ciphertext}'")
    transpose_brute_force(ciphertext, max_key=8)

def input_transposition():
    """
    Fungsi input interaktif untuk Transposition Cipher.
    """
    print("\n" + "="*50)
    print("TRANSPOSITION CIPHER - INPUT INTERAKTIF")
    print("="*50)
    
    while True:
        print("\nPilih operasi:")
        print("1. Enkripsi (tanpa spasi)")
        print("2. Dekripsi (tanpa spasi)")
        print("3. Enkripsi (dengan spasi)")
        print("4. Dekripsi (dengan spasi)")
        print("5. Brute Force Attack")
        print("6. Kembali ke Menu Utama")
        
        choice = input("Masukkan pilihan (1-6): ").strip()
        
        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            try:
                key = int(input("Masukkan key (jumlah kolom): "))
                padding = input("Masukkan karakter padding (default 'X'): ") or 'X'
                encrypted = transpose_encrypt(plaintext, key, padding)
                print(f"\nHasil Enkripsi: {encrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            try:
                key = int(input("Masukkan key (jumlah kolom): "))
                decrypted = transpose_decrypt(ciphertext, key)
                print(f"\nHasil Dekripsi: {decrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '3':
            plaintext = input("Masukkan plaintext: ")
            try:
                key = int(input("Masukkan key (jumlah kolom): "))
                padding = input("Masukkan karakter padding (default 'X'): ") or 'X'
                encrypted = transpose_encrypt_preserve_spaces(plaintext, key, padding)
                print(f"\nHasil Enkripsi: {encrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '4':
            ciphertext = input("Masukkan ciphertext: ")
            try:
                key = int(input("Masukkan key (jumlah kolom): "))
                decrypted = transpose_decrypt_preserve_spaces(ciphertext, key)
                print(f"\nHasil Dekripsi: {decrypted}")
            except ValueError:
                print("Key harus berupa angka!")
                
        elif choice == '5':
            ciphertext = input("Masukkan ciphertext untuk brute force: ")
            try:
                max_key = int(input("Masukkan key maksimum (default 15): ") or "15")
                transpose_brute_force(ciphertext, max_key)
            except ValueError:
                print("Key maksimum harus berupa angka!")
                
        elif choice == '6':
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("TRANSPOSITION CIPHER PROGRAM")
        print("="*50)
        print("1. Lihat Demo")
        print("2. Input Interaktif")
        print("3. Keluar")
        
        main_choice = input("Pilih menu (1-3): ").strip()
        
        if main_choice == '1':
            demo_transposition()
        elif main_choice == '2':
            input_transposition()
        elif main_choice == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
```

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
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
    Kelemahan utama Sandi Caesar adalah sifatnya yang monoalfabetik. Ini berarti setiap huruf plaintext selalu diganti dengan huruf ciphertext yang sama (misalnya, jika 'A' menjadi 'D', maka setiap 'A' lain dalam pesan juga akan menjadi 'D'). Karena hanya ada 25 kemungkinan kunci (pergeseran), sandi ini dapat dipecahkan dalam hitungan detik menggunakan serangan brute force atau analisis frekuensi sederhana.
    Kelemahan Sandi Vigenère, meskipun jauh lebih kuat karena bersifat polialfabetik (menggunakan banyak alfabet pergeseran), terletak pada sifat periodik atau pengulangan kata kuncinya. Jika penyerang dapat menebak panjang kata kunci (misalnya menggunakan Metode Kasiski), mereka dapat membagi ciphertext menjadi beberapa bagian. Setiap bagian tersebut pada dasarnya adalah pesan yang dienkripsi dengan Sandi Caesar yang berbeda, yang kemudian dapat diserang secara individual menggunakan analisis frekuensi.
    
2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
   Cipher klasik mudah diserang dengan analisis frekuensi karena mereka gagal menyembunyikan properti statistik dan redundansi dari bahasa asli yang digunakan dalam plaintext. Setiap bahasa alami memiliki pola frekuensi huruf yang dapat diprediksi; misalnya, dalam bahasa Indonesia, huruf 'A' adalah yang paling umum, diikuti oleh 'N', 'I', dan 'E'.
    Pada sandi substitusi monoalfabetik (seperti Caesar atau sandi substitusi sederhana lainnya), pola frekuensi ini tetap terjaga di dalam ciphertext, meskipun hurufnya telah diganti. Seorang analis kripto dapat dengan mudah menghitung frekuensi setiap huruf dalam ciphertext, lalu mencocokkannya dengan pola frekuensi bahasa yang diketahui. Huruf yang paling sering muncul di ciphertext hampir pasti mewakili huruf yang paling sering muncul di bahasa aslinya.
   
3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
   Perbandingan utama antara kedua metode sandi klasik ini terletak pada cara mereka mengaburkan pesan. Sandi substitusi, seperti Sandi Caesar dan Vigenère, bekerja dengan mengganti identitas elemen plaintext, misalnya mengubah huruf 'A' menjadi 'X'. Kelebihan dari metode ini adalah pesan asli menjadi tidak dapat dikenali secara langsung. Namun, kelemahannya adalah kerentanannya terhadap analisis frekuensi, terutama jika substitusinya sederhana (monoalfabetik), karena ia mempertahankan urutan asli huruf relatif satu sama lain meskipun nilainya telah berubah.
    Di sisi lain, sandi transposisi, seperti transposisi kolom, beroperasi dengan cara yang berbeda. Ia tidak mengubah identitas huruf, sehingga 'A' tetap 'A', tetapi fokus pada pengubahan urutan atau posisi elemen plaintext. Kelebihan utamanya adalah kemampuannya merusak pola bahasa, seperti memecah kata atau pasangan huruf yang umum (digraf), yang membuat pembacaan langsung menjadi sulit. Akan tetapi, kelemahannya adalah frekuensi kemunculan setiap huruf di ciphertext sama persis dengan di plaintext, sehingga ia rentan terhadap metode analisis yang berbeda, seperti mencari anagram atau menggunakan statistik untuk menyusun ulang kolom-kolomnya. 
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
