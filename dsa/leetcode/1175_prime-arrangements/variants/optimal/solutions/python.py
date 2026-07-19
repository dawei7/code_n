MODULUS = 1_000_000_007


def solve(n: int) -> int:
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    candidate = 2
    while candidate * candidate <= n:
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, n + 1, candidate):
                is_prime[multiple] = False
        candidate += 1

    prime_count = sum(is_prime)
    result = 1
    for value in range(2, prime_count + 1):
        result = result * value % MODULUS
    for value in range(2, n - prime_count + 1):
        result = result * value % MODULUS
    return result
