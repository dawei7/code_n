def solve(mod: int = 14**8) -> int:
    """Find sum_{n=0..6} A(n, n) mod 14^8 for the Ackermann function.
    
    Time Complexity: O(log(MOD)) via Tower Exponentiation & Euler's Totient Reduction
    Space Complexity: O(log(MOD))
    """

    def phi(n):
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

    def tower(h, m):
        if m == 1:
            return 0
        if h == 1:
            return 2 % m
        if h == 2:
            return 4 % m
        if h == 3:
            return 16 % m
        if h == 4:
            return 65536 % m
        p = phi(m)
        exp = tower(h - 1, p) + p
        return pow(2, exp, m)

    a0 = 1
    a1 = 3
    a2 = 7
    a3 = 61
    a4 = (tower(7, mod) - 3) % mod
    a5 = (tower(10, mod) - 3) % mod
    a6 = (tower(10, mod) - 3) % mod

    return (a0 + a1 + a2 + a3 + a4 + a5 + a6) % mod
