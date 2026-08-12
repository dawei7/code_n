import itertools


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve() -> int:
    """Find the largest n-digit pandigital prime.
    
    Time Complexity: O(7! * sqrt(P))
    Space Complexity: O(1)
    """
    # 9-digit (sum 45) and 8-digit (sum 36) pandigitals are always divisible by 3.
    # Largest pandigital prime must be a 7-digit number!
    for perm in itertools.permutations("7654321"):
        val = int("".join(perm))
        if is_prime(val):
            return val
    return -1
