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