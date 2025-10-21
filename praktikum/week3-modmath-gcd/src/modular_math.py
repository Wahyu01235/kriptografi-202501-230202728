# file: praktikum/week3-modmath-gcd/src/modular_math.py

# --- Langkah 1: Aritmetika Modular ---
def modular_addition(num_a, num_b, modulus):
    """
    Melakukan operasi penjumlahan modular: (num_a + num_b) % modulus.
    """
    return (num_a + num_b) % modulus

def modular_subtraction(num_a, num_b, modulus):
    """
    Melakukan operasi pengurangan modular: (num_a - num_b) % modulus.
    Memastikan hasil selalu non-negatif.
    """
    return (num_a - num_b + modulus) % modulus

def modular_multiplication(num_a, num_b, modulus):
    """
    Melakukan operasi perkalian modular: (num_a * num_b) % modulus.
    """
    return (num_a * num_b) % modulus

def modular_exponentiation(base, exponent, modulus):
    """
    Melakukan operasi eksponensiasi modular: (base ^ exponent) % modulus.
    Menggunakan fungsi pow() bawaan Python yang efisien untuk ini.
    """
    return pow(base, exponent, modulus)

# --- Langkah 2: GCD & Algoritma Euclidean ---
def calculate_gcd(num_a, num_b):
    """
    Menghitung Greatest Common Divisor (GCD) dari dua bilangan
    menggunakan Algoritma Euclidean iteratif.
    """
    while num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return num_a

# --- Langkah 3: Extended Euclidean Algorithm & Invers Modular ---
def extended_euclidean_algorithm(num_a, num_b):
    """
    Implementasi Algoritma Euclidean Diperpanjang.
    Mengembalikan tuple (g, x, y) di mana g = gcd(num_a, num_b)
    dan memenuhi persamaan num_a*x + num_b*y = g.
    """
    if num_a == 0:
        return num_b, 0, 1
    
    gcd_val, x1, y1 = extended_euclidean_algorithm(num_b % num_a, num_a)
    x = y1 - (num_b // num_a) * x1
    y = x1
    return gcd_val, x, y

def find_modular_inverse(num_a, modulus):
    """
    Mencari invers modular dari num_a modulo modulus.
    Mengembalikan x sedemikian rupa sehingga (num_a * x) % modulus == 1.
    Mengembalikan None jika invers tidak ada (yaitu, gcd(num_a, modulus) != 1).
    """
    gcd_val, x_coeff, _ = extended_euclidean_algorithm(num_a, modulus)
    if gcd_val != 1:
        return None  # Invers modular tidak ada jika bukan koprima
    return x_coeff % modulus

# --- Langkah 4: Logaritma Diskrit (Discrete Log) ---
def solve_discrete_log(base_a, target_b, modulus_n):
    """
    Menyelesaikan masalah Logaritma Diskrit sederhana:
    Mencari x sedemikian rupa sehingga (base_a ^ x) % modulus_n == target_b.
    Ini adalah implementasi brute-force dan hanya cocok untuk modulus kecil.
    """
    for x_candidate in range(modulus_n): # Mencoba setiap nilai x dari 0 hingga n-1
        if modular_exponentiation(base_a, x_candidate, modulus_n) == target_b:
            return x_candidate
    return None # Jika tidak ada solusi yang ditemukan dalam rentang

# --- Bagian Eksekusi Utama Program ---
if __name__ == "__main__":
    print("--- Aritmetika Modular ---")
    # Output untuk penjumlahan, perkalian, dan eksponensiasi tetap sama
    print(f"7 + 5 mod 12 = {modular_addition(7, 5, 12)}")
    print(f"7 * 5 mod 12 = {modular_multiplication(7, 5, 12)}")
    print(f"7 ^ 128 mod 13 = {modular_exponentiation(7, 128, 13)}")

    print("\n--- GCD & Algoritma Euclidean ---")
    # Output untuk GCD tetap sama
    print(f"gcd(54, 24) = {calculate_gcd(54, 24)}")

    print("\n--- Extended Euclidean Algorithm & Invers Modular ---")
    # Output untuk invers modular tetap sama
    print(f"Invers 3 mod 11 = {find_modular_inverse(3, 11)}")

    print("\n--- Logaritma Diskrit Sederhana ---")
    # Output untuk logaritma diskrit tetap sama
    print(f"3^x == 4 (mod 7), x = {solve_discrete_log(3, 4, 7)}")
