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