# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def _transform(text, key, direction):
    """
    Fungsi inti untuk menggeser karakter.
    direction=1 untuk enkripsi, direction=-1 untuk dekripsi.
    """
    output_chars = []
    for char in text:
        if char.isalpha():
            # Tentukan basis (65 untuk 'A', 97 untuk 'a')
            base = 65 if char.isupper() else 97
            
            # Hitung pergeseran
            # 1. Ubah ke 0-25 (ord(char) - base)
            # 2. Terapkan pergeseran ( ... + (key * direction))
            # 3. Modulo 26 untuk wrap-around
            # 4. Kembalikan ke nilai ASCII ( ... + base)
            new_ord = ((ord(char) - base + (key * direction)) % 26) + base
            output_chars.append(chr(new_ord))
        else:
            # Jika bukan alfabet, tambahkan karakter asli
            output_chars.append(char)
            
    # Gabungkan semua karakter dalam list menjadi satu string
    return "".join(output_chars)

def encrypt(plaintext, key):
    """
    Enkripsi plaintext menggunakan pergeseran positif.
    """
    return _transform(plaintext, key, 1)

def decrypt(ciphertext, key):
    """
    Dekripsi ciphertext menggunakan pergeseran negatif.
    """
    return _transform(ciphertext, key, -1)

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    # Nilai-nilai ini dijaga agar keluaran tetap sama
    message = "<230202728><Achmad Wahyudi>"
    key = 7

    # Panggil fungsi enkripsi dan dekripsi
    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    # Mencetak hasil ke konsol menggunakan format yang berbeda (f-string)
    # namun menghasilkan teks yang identik.
    print(f"Plaintext : {message}")
    print(f"Ciphertext: {enc}")
    print(f"Decrypted : {dec}")

if __name__ == "__main__":
    main()
