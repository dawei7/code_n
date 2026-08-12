def phi(n: int) -> int:
    res = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            res -= res // p
        p += 1
    if temp > 1:
        res -= res // temp
    return res


def solve(a: int = 1864, b: int = 1909) -> int:
    """Find number of sides of Minkowski sum S_a + S_{a+1} + ... + S_b.
    
    Time Complexity: O(b * sqrt(b))
    Space Complexity: O(1)
    """
    total_sides = 0
    for q in range(1, b + 1):
        if b // q > (a - 1) // q:
            total_sides += phi(q)
    return total_sides
