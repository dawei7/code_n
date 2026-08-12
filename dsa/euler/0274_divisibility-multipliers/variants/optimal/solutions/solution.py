def solve(limit: int = 10**7) -> int:
    """Find the sum of divisibility multipliers m = 10^(-1) mod p for all primes p < 10^7 coprime to 10.
    
    Time Complexity: O(limit / log(limit)) via Modular Inverse Sieve
    Space Complexity: O(limit / log(limit))
    """
    is_p = bytearray([1]) * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    primes = [i for i in range(2, limit + 1) if is_p[i] and i not in (2, 5)]
    ans = sum(pow(10, -1, p) for p in primes)
    return ans
