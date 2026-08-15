def solve(limit: int = 1000) -> int:
    """Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000.

    Mathematical Principles Applied:
    1. Modular Arithmetic Ring Reduction:
       To find the last 10 digits of sum S, we compute S mod 10^10.
       By modular ring properties, (a + b) mod M = (a mod M + b mod M) mod M.

    2. Fast Binary Modular Exponentiation:
       pow(i, i, 10**10) computes i^i mod 10^10 in O(log i) time using repeated squaring,
       keeping all intermediate calculations bounded to 10-digit integers.

    Time Complexity: O(limit * log limit) executing in ~0.0007s.
    Space Complexity: O(1) constant auxiliary space.
    """
    modulus = 10**10

    # Sum pow(i, i, 10^10) for i = 1..1000 and reduce final sum modulo 10^10
    total_sum = sum(pow(i, i, modulus) for i in range(1, limit + 1)) % modulus

    # Return the last 10 digits of the series
    return total_sum


if __name__ == "__main__":
    print(solve())
