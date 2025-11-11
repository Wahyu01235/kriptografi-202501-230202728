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