def phi(n: int) -> int:
    """Compute Euler's totient function phi(n)."""
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def tetration_mod(a: int, b: int, m: int) -> int:
    """Compute tetration a ^^ b mod m recursively."""
    if m == 1:
        return 0
    if b == 1:
        return a % m
    p_m = phi(m)
    exp = tetration_mod(a, b - 1, p_m)
    return pow(a, exp, m)


def solve(a: int = 1777, b: int = 1855, m: int = 10**8) -> int:
    """Find last 8 digits of a ^^ b.
    
    Time Complexity: O(log* m * sqrt(m))
    Space Complexity: O(log* m)
    """
    return tetration_mod(a, b, m)
