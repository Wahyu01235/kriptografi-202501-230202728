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