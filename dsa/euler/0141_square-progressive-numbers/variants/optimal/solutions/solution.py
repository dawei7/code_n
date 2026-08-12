import math


def solve(limit: int = 1000000000000) -> int:
    """Find sum of all progressive perfect squares below limit.
    
    Time Complexity: O(Limit^(1/3) * a)
    Space Complexity: O(N_squares)
    """
    prog_squares = set()

    for a in range(2, int(limit**(1 / 3)) + 1):
        a3 = a * a * a
        if a3 >= limit:
            break
        for b in range(1, a):
            if math.gcd(a, b) != 1:
                continue
            a3_b = a3 * b
            if a3_b >= limit:
                break
            b2 = b * b
            max_c = int((limit / a3_b)**0.5) + 1
            for c in range(1, max_c):
                n = c * c * a3_b + c * b2
                if n >= limit:
                    break
                r = math.isqrt(n)
                if r * r == n:
                    prog_squares.add(n)

    return sum(prog_squares)
