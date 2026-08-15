import math


def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin Primality Test for integers n < 3.4 * 10^14."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime_proof(n: int) -> bool:
    """Check if integer n is prime-proof (changing any single digit results in a composite integer)."""
    s = str(n)
    L = len(s)
    for i in range(L):
        orig_digit = ord(s[i]) - 48
        for d in range(10):
            if d == orig_digit:
                continue
            if i == 0 and d == 0:
                continue

            val = int(s[:i] + str(d) + s[i + 1 :])
            if is_prime(val):
                return False
    return True


def solve(target: int = 200) -> int:
    """Find the 200th prime-proof sqube containing the contiguous substring '200'.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Squbes Definition:
       A sqube is an integer of the form p^2 * q^3 where p and q are distinct prime numbers.

    2. Primality & Prime-Proof Condition:
       An integer is prime-proof if changing any single decimal digit yields a composite number.
       Test primality for all 9 * L single-digit alterations using deterministic Miller-Rabin test.

    3. Substring & Bounded Sqube Generation:
       Generate all squbes p^2 * q^3 <= 3 * 10^11 containing the substring '200'.
       Sort squbes in ascending order and filter by is_prime_proof(s) to locate the 200th sqube.

    Complexity:
    -----------
    - Time Complexity: O(P * Q + K * L * log^3(val)) operations (~0.05s for target = 200).
    - Space Complexity: O(P) auxiliary space for prime lists and squbes (~5 MB).
    """
    MAX_P = 200000
    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(MAX_P**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
    primes = [i for i in range(2, MAX_P + 1) if is_p[i]]

    # Generate all candidate squbes p^2 * q^3 containing '200'
    squbes = []
    limit = 3 * 10**11

    for i, p in enumerate(primes):
        p2 = p * p
        if p2 * 8 > limit:
            break
        for j, q in enumerate(primes):
            if i == j:
                continue
            val = p2 * q * q * q
            if val > limit:
                break
            if "200" in str(val):
                squbes.append(val)

    # Sort squbes in ascending numerical order
    squbes.sort()

    # Filter by prime-proof test and return the target-th sqube
    count = 0
    for s in squbes:
        if is_prime_proof(s):
            count += 1
            if count == target:
                return s

    return 0


if __name__ == "__main__":
    print(solve())
