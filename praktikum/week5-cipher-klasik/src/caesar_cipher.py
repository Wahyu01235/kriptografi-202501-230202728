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