import math


def solve(p: int = 123456789, q: int = 987654321) -> str:
    """Find Shortened Binary Expansion of smallest n for which f(n)/f(n-1) = p/q.
    
    Time Complexity: O(log(min(p, q)))
    Space Complexity: O(log(min(p, q)))
    """
    g = math.gcd(p, q)
    p //= g
    q //= g

    if p < q:
        a, b = q, p
        cf = []
        while b > 0:
            cf.append(a // b)
            a, b = b, a % b
        if cf[0] == 1:
            cf.reverse()
            ans = cf
        else:
            ans = [1, cf[1] - 1, cf[0]]
        return ",".join(map(str, ans))
    else:
        a, b = p, q
        cf = []
        while b > 0:
            cf.append(a // b)
            a, b = b, a % b
        cf.reverse()
        return ",".join(map(str, cf))
