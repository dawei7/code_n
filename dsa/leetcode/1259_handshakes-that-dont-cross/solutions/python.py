MODULUS = 1_000_000_007


def solve(numPeople: int) -> int:
    pairs = numPeople // 2
    catalan = 1
    for k in range(pairs):
        catalan = catalan * (2 * (2 * k + 1)) % MODULUS
        catalan = catalan * pow(k + 2, MODULUS - 2, MODULUS) % MODULUS
    return catalan
