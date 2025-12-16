import random

print("=" * 60)
print("LANGKAH 1: SIMULASI DIFFIE-HELLMAN NORMAL")
print("=" * 60)

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

print(f"Parameter publik:")
print(f"  p (bilangan prima) = {p}")
print(f"  g (generator) = {g}")
print()

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

print(f"Private key:")
print(f"  a (rahasia Alice) = {a}")
print(f"  b (rahasia Bob)   = {b}")
print()

# public key
A = pow(g, a, p)  # A = g^a mod p
B = pow(g, b, p)  # B = g^b mod p

print(f"Public key:")
print(f"  A (public key Alice) = {g}^{a} mod {p} = {A}")
print(f"  B (public key Bob)   = {g}^{b} mod {p} = {B}")
print()

# pertukaran public key dan perhitungan shared secret
shared_secret_A = pow(B, a, p)  # S_A = B^a mod p
shared_secret_B = pow(A, b, p)  # S_B = A^b mod p

print(f"Shared secret setelah pertukaran:")
print(f"  Kunci bersama Alice = {B}^{a} mod {p} = {shared_secret_A}")
print(f"  Kunci bersama Bob   = {A}^{b} mod {p} = {shared_secret_B}")
print()

# Verifikasi
if shared_secret_A == shared_secret_B:
    print("✓ SUKSES: Kunci bersama Alice dan Bob SAMA")
else:
    print("✗ GAGAL: Kunci bersama Alice dan Bob BERBEDA")
print()

# ==============================================================================

print("=" * 60)
print("LANGKAH 2: SIMULASI SERANGAN MITM (MAN-IN-THE-MIDDLE)")
print("=" * 60)

# Reset random seed untuk hasil yang berbeda
random.seed()

# Alice dan Bob memilih private key yang sama seperti sebelumnya
# (Dalam simulasi ini, kita anggap Eve tidak tahu a dan b)

# Eve (penyerang) membuat private key sendiri
e1 = random.randint(1, p-1)  # private key Eve untuk Alice
e2 = random.randint(1, p-1)  # private key Eve untuk Bob

print("Skenario:")
print("  1. Alice mengirim public key A ke Bob")
print("  2. Eve mencegat dan mengganti dengan E1 = g^e1 mod p")
print("  3. Bob mengirim public key B ke Alice")
print("  4. Eve mencegat dan mengganti dengan E2 = g^e2 mod p")
print()

# Public key asli Alice dan Bob
print(f"Public key asli:")
print(f"  A (Alice) = {A}")
print(f"  B (Bob)   = {B}")

# Public key palsu yang dibuat Eve
E1 = pow(g, e1, p)  # E1 = g^e1 mod p (dikirim ke Bob atas nama Alice)
E2 = pow(g, e2, p)  # E2 = g^e2 mod p (dikirim ke Alice atas nama Bob)

print(f"Public key palsu dari Eve:")
print(f"  E1 (untuk Bob)    = {g}^{e1} mod {p} = {E1}")
print(f"  E2 (untuk Alice)  = {g}^{e2} mod {p} = {E2}")
print()

# Perhitungan shared secret dari perspektif masing-masing
print("PERHITUNGAN SHARED SECRET:")

# Alice menerima E2 (mengira itu dari Bob)
shared_secret_Alice = pow(E2, a, p)  # S_Alice = E2^a mod p

# Bob menerima E1 (mengira itu dari Alice)
shared_secret_Bob = pow(E1, b, p)    # S_Bob = E1^b mod p

# Eve menghitung shared secret dengan Alice dan Bob
shared_secret_Eve_Alice = pow(A, e2, p)  # S_Eve-Alice = A^e2 mod p
shared_secret_Eve_Bob = pow(B, e1, p)    # S_Eve-Bob = B^e1 mod p

print(f"\nDari perspektif Alice:")
print(f"  Alice menghitung: {E2}^{a} mod {p} = {shared_secret_Alice}")
print(f"  (Alice mengira ini shared secret dengan Bob)")

print(f"\nDari perspektif Bob:")
print(f"  Bob menghitung: {E1}^{b} mod {p} = {shared_secret_Bob}")
print(f"  (Bob mengira ini shared secret dengan Alice)")

print(f"\nDari perspektif Eve:")
print(f"  Shared secret Eve dengan Alice: {A}^{e2} mod {p} = {shared_secret_Eve_Alice}")
print(f"  Shared secret Eve dengan Bob: {B}^{e1} mod {p} = {shared_secret_Eve_Bob}")
print()

# Verifikasi
print("HASIL SERANGAN MITM:")
print(f"  Shared secret Alice: {shared_secret_Alice}")
print(f"  Shared secret Bob: {shared_secret_Bob}")
print(f"  Shared secret Eve dengan Alice: {shared_secret_Eve_Alice}")
print(f"  Shared secret Eve dengan Bob: {shared_secret_Eve_Bob}")

if shared_secret_Alice == shared_secret_Eve_Alice:
    print("✓ Eve BERHASIL mendapatkan shared secret yang sama dengan Alice")
else:
    print("✗ Eve GAGAL mendapatkan shared secret yang sama dengan Alice")

if shared_secret_Bob == shared_secret_Eve_Bob:
    print("✓ Eve BERHASIL mendapatkan shared secret yang sama dengan Bob")
else:
    print("✗ Eve GAGAL mendapatkan shared secret yang sama dengan Bob")

if shared_secret_Alice == shared_secret_Bob:
    print("✗ Alice dan Bob memiliki shared secret YANG SAMA (serangan gagal)")
else:
    print("✓ Alice dan Bob memiliki shared secret YANG BERBEDA (serangan berhasil!)")
print()

# ==============================================================================

print("=" * 60)
print("ANALISIS HASIL")
print("=" * 60)
print("""
KESIMPULAN:
1. Dalam skenario normal (tanpa serangan), Alice dan Bob berhasil menghasilkan
   shared secret yang sama melalui pertukaran kunci Diffie-Hellman.

2. Dalam serangan Man-in-the-Middle (MITM):
   - Eve mencegat komunikasi antara Alice dan Bob
   - Eve mengganti public key yang dipertukarkan dengan public key miliknya
   - Akibatnya:
     * Alice membuat shared secret dengan Eve (bukan dengan Bob)
     * Bob membuat shared secret dengan Eve (bukan dengan Alice)
     * Eve memiliki shared secret dengan keduanya
     * Alice dan Bob memiliki shared secret YANG BERBEDA

3. Implikasi keamanan:
   - Eve dapat menyadap dan mendekripsi semua komunikasi antara Alice dan Bob
   - Eve bahkan dapat memodifikasi pesan yang dikirimkan
   - Alice dan Bob tidak menyadari adanya penyadapan

4. Solusi pencegahan:
   - Menggunakan otentikasi (digital signature, sertifikat digital)
   - Protokol dengan otentikasi seperti TLS/SSL
   - Pertukaran kunci dengan otentikasi (Station-to-Station protocol)
""")
