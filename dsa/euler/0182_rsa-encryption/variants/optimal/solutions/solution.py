import math


def solve(p: int = 1009, q: int = 3643) -> int:
    """Find sum of valid e (1 < e < phi, gcd(e, phi) = 1) minimizing number of unconcealed messages.
    
    Time Complexity: O(phi)
    Space Complexity: O(1)
    """
    phi = (p - 1) * (q - 1)
    p1 = p - 1
    q1 = q - 1

    min_u = float('inf')
    sum_e = 0

    for e in range(3, phi, 2):
        if math.gcd(e, phi) == 1:
            u = (1 + math.gcd(e - 1, p1)) * (1 + math.gcd(e - 1, q1))
            if u < min_u:
                min_u = u
                sum_e = e
            elif u == min_u:
                sum_e += e

    return sum_e
