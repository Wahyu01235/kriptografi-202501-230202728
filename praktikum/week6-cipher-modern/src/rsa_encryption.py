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