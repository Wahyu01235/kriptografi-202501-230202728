from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# INPUT PESAN DARI USER
user_message = input("Masukkan pesan yang akan ditandatangani: ")
original_message = user_message.encode('utf-8')

# GENERATE PASANGAN KUNCI RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Simpan kunci (opsional, best practice)
with open("private_key.pem", "wb") as f:
    f.write(private_key.export_key())

with open("public_key.pem", "wb") as f:
    f.write(public_key.export_key())

# HASH PESAN
hash_original = SHA256.new(original_message)

# BUAT TANDA TANGAN DIGITAL
signature = pkcs1_15.new(private_key).sign(hash_original)

print("\nTanda tangan digital berhasil dibuat.")
print("Signature (hex):", signature.hex())

# VERIFIKASI PESAN ASLI
try:
    hash_verify = SHA256.new(original_message)
    pkcs1_15.new(public_key).verify(hash_verify, signature)
    print("Verifikasi berhasil: tanda tangan VALID.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK valid.")
