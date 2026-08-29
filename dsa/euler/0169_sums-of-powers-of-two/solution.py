def solve(n: int = 10**25) -> int:
    """Find f(n), the number of ways to express n as a sum of powers of 2 (each power used at most twice).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Stern's Diatomic Sequence & Hyperbinary Representations:
       Let f(n) be the number of partitions of n into powers of 2 with part multiplicity at most 2.
       This is computed iteratively over the binary representation of n:
       State (a, b) where a = f(prefix) and b = f(prefix - 1).
       For bit = 0: a' = a + b, b' = b
       For bit = 1: a' = a, b' = a + b

    Complexity:
    -----------
    - Time Complexity: O(log_2 n) operations (~0.0001s for n = 10^25).
    - Space Complexity: O(1) auxiliary memory.
    """
    # Express n in binary without '0b'
    bits = bin(n)[2:]
    a, b = 1, 0

    for bit in bits:
        if bit == "1":
            b = a + b
        else:
            a = a + b

    return a


if __name__ == "__main__":
    print(solve())
