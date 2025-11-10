import math

# Langkah 1: Perhitungan Entropi
def entropy(keyspace_size):
    return math.log2(keyspace_size)

# Langkah 2: Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

# Langkah 3: Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# Contoh perhitungan
if __name__ == "__main__":
    print("=" * 50)
    print("ANALISIS KRIPTOGRAFI")
    print("=" * 50)
    
    # Kasus 1: Caesar Cipher
    keysize_caesar = 26
    entropy_caesar = entropy(keysize_caesar)
    ud_caesar = unicity_distance(entropy_caesar)
    bf_time_caesar = brute_force_time(keysize_caesar)
    
    print("\n1. CAESAR CIPHER (Alfabet 26 karakter):")
    print(f"   - Entropi Kunci: {entropy_caesar:.2f} bit")
    print(f"   - Unicity Distance: {ud_caesar:.2f} karakter ciphertext")
    print(f"   - Waktu Brute Force: {bf_time_caesar:.6f} hari (dengan 1 juta percobaan/detik)")
    
    # Kasus 2: AES-128
    keysize_aes = 2**128
    entropy_aes = entropy(keysize_aes)
    ud_aes = unicity_distance(entropy_aes)
    bf_time_aes = brute_force_time(keysize_aes)
    
    print("\n2. AES-128:")
    print(f"   - Entropi Kunci: {entropy_aes:.2f} bit")
    print(f"   - Unicity Distance: {ud_aes:.2f} karakter ciphertext")
    print(f"   - Waktu Brute Force: {bf_time_aes:.2e} hari (dengan 1 juta percobaan/detik)")
    
    # Kasus 3: Custom Input
    print("\n3. KALKULATOR KUSTOM:")
    try:
        custom_keysize = int(input("   Masukkan ukuran ruang kunci (contoh: 256): "))
        custom_entropy = entropy(custom_keysize)
        custom_ud = unicity_distance(custom_entropy)
        custom_bf = brute_force_time(custom_keysize)
        
        print(f"   - Entropi Kunci: {custom_entropy:.2f} bit")
        print(f"   - Unicity Distance: {custom_ud:.2f} karakter ciphertext")
        print(f"   - Waktu Brute Force: {custom_bf:.2e} hari")
        
    except ValueError:
        print("   Input tidak valid! Harap masukkan bilangan bulat.")

    print("\n" + "=" * 50)
