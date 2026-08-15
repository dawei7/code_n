def solve(modulus: int = 10000000000) -> int:
    """Find the last ten digits of the non-Mersenne prime 28433 * 2^7830457 + 1.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Modular Arithmetic & Binary Exponentiation:
       To extract the last 10 digits of a large integer, all calculations are performed
       modulo 10^10.
       The power 2^7830457 mod 10^10 is computed via repeated squaring (binary exponentiation)
       in O(log E) = 23 multiplications.

    2. Expression Evaluation:
       Result = (28433 * (2^7830457 mod 10^10) + 1) mod 10^10.

    Complexity:
    -----------
    - Time Complexity: O(log E) where E = 7,830,457 (terminates in ~0.0001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    coefficient = 28433
    exponent = 7830457
    base = 2
    power = 1

    # Dynamic binary exponentiation loop modulo 10^10
    while exponent > 0:
        if exponent % 2 == 1:
            power = (power * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    # Compute final last 10 digits
    last_10_digits = (coefficient * power + 1) % modulus
    return last_10_digits


if __name__ == "__main__":
    print(solve())
