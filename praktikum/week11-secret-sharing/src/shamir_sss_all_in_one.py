# ==========================================================
# SHAMIR SECRET SHARING
# Library-based and Manual Implementation (All-in-One)
# Python 3.11+
# ==========================================================

import random
from functools import reduce

# ==========================================================
# PART 1 — LIBRARY VERSION (REFERENCE ONLY)
# ==========================================================

def library_version():
    print("\n=== LIBRARY VERSION (REFERENCE) ===")

    try:
        from secretsharing import SecretSharer
    except ImportError:
        print("Library 'secretsharing' belum terinstall.")
        print("Install dengan: pip install secretsharing")
        return

    secret = "KriptografiUPB2025"
    k, n = 3, 5

    print("Secret:", secret)
    print(f"Threshold k = {k}, Total shares n = {n}")

    shares = SecretSharer.split_secret(secret, k, n)

    print("\nGenerated Shares:")
    for s in shares:
        print(s)

    recovered = SecretSharer.recover_secret(shares[:k])
    print("\nRecovered Secret:", recovered)


# ==========================================================
# PART 2 — MANUAL IMPLEMENTATION
# ==========================================================

def string_to_int(s: str) -> int:
    return int.from_bytes(s.encode(), "big")


def int_to_string(i: int) -> str:
    length = (i.bit_length() + 7) // 8
    return i.to_bytes(length, "big").decode()


def mod_inverse(a, p):
    return pow(a, -1, p)


def generate_polynomial(secret_int, k, p):
    coeffs = [secret_int]
    for _ in range(1, k):
        coeffs.append(random.randint(0, p - 1))
    return coeffs


def evaluate_polynomial(coeffs, x, p):
    result = 0
    for power, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, power, p)) % p
    return result


def generate_shares(secret, k, n, p):
    secret_int = string_to_int(secret)
    coeffs = generate_polynomial(secret_int, k, p)

    shares = []
    for x in range(1, n + 1):
        y = evaluate_polynomial(coeffs, x, p)
        shares.append((x, y))

    return shares


def lagrange_interpolation(shares, p):
    def basis(j):
        xj, _ = shares[j]
        acc = 1
        for m in range(len(shares)):
            if m != j:
                xm, _ = shares[m]
                acc = (acc * (-xm) * mod_inverse(xj - xm, p)) % p
        return acc

    secret = 0
    for j in range(len(shares)):
        _, yj = shares[j]
        secret = (secret + yj * basis(j)) % p

    return secret


def manual_version():
    print("\n=== MANUAL VERSION (POLYNOMIAL MOD p) ===")

    secret = "KriptografiUPB2025"
    k, n = 3, 5

    # Bilangan prima besar
    p = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    print("Secret:", secret)
    print(f"Threshold k = {k}, Total shares n = {n}")

    shares = generate_shares(secret, k, n, p)

    print("\nGenerated Shares:")
    for s in shares:
        print(s)

    selected = shares[:k]
    recovered_int = lagrange_interpolation(selected, p)
    recovered_secret = int_to_string(recovered_int)

    print("\nRecovered Secret:", recovered_secret)


# ==========================================================
# MAIN ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    print("SHAMIR SECRET SHARING PRACTICUM")
    print("--------------------------------")

    library_version()
    manual_version()
    print("\n=== END OF PRACTICUM ===\n")
