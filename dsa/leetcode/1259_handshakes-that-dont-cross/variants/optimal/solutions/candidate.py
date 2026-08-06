def solve(numPeople: int) -> int:
    modulus = 1_000_000_007
    pair_count = numPeople // 2
    factorial = 1
    pair_factorial = 1

    for value in range(2, 2 * pair_count + 1):
        factorial = factorial * value % modulus
        if value == pair_count:
            pair_factorial = factorial

    denominator = pair_factorial * pair_factorial % modulus
    denominator = denominator * (pair_count + 1) % modulus
    return factorial * pow(denominator, modulus - 2, modulus) % modulus
