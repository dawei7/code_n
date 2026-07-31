def solve(n: int, k: int) -> int:
    modulus = 1_000_000_007

    def combinations(top: int, bottom: int) -> int:
        bottom = min(bottom, top - bottom)
        numerator = 1
        denominator = 1

        for offset in range(1, bottom + 1):
            numerator = numerator * (top - bottom + offset) % modulus
            denominator = denominator * offset % modulus

        return numerator * pow(denominator, modulus - 2, modulus) % modulus

    total = combinations(n - 1, k - 1)
    if (n - k) % 2 == 1:
        return total

    all_odd = combinations((n + k) // 2 - 1, k - 1)
    return (total - all_odd) % modulus
