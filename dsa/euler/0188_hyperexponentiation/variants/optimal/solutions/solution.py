import math


def solve(a: int = 1777, b: int = 1855, m: int = 10**8) -> int:
    """Find the last 8 digits of the tetration (hyperexponentiation) 1777 ^^ 1855 modulo 10^8.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Hyperexponentiation / Tetration Definition:
       a ^^ 1 = a
       a ^^ (k + 1) = a^(a ^^ k)
       Thus, 1777 ^^ 1855 represents an exponent tower of height 1855:
       1777^(1777^(1777^...)).

    2. Euler's Totient Power Tower Reduction:
       By Euler's Totient Theorem, if gcd(a, m) = 1:
           a^X == a^(X mod phi(m)) (mod m)
       More generally (including when gcd(a, m) > 1), for sufficiently large towers X >= log_2(m):
           a^X == a^(phi(m) + (X mod phi(m))) (mod m)
       Since 1777 is odd and coprime to 10^8 (gcd(1777, 10^8) = 1), exact reduction applies:
           a ^^ b mod m = a^( (a ^^ (b - 1)) mod phi(m) ) mod m

    3. Iterated Totient Tower Chain:
       Successively applying phi(m) collapses the modulus rapidly:
           10^8 -> 4 * 10^7 -> 1.6 * 10^7 -> ... -> 1
       The chain reaches 1 in O(log* m) iterations (fewer than 20 steps).
       Evaluating from the top of the tower down to the bottom modulo m yields the exact last 8 digits.

    Complexity:
    -----------
    - Time Complexity: O(log* m * sqrt(m)) operations (~0.0001s).
    - Space Complexity: O(log* m) memory for moduli stack (~1 KB).
    """

    def phi(n: int) -> int:
        """Compute Euler's Totient function phi(n)."""
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

    # Build tower of moduli phi_stack
    moduli = [m]
    for _ in range(b):
        next_m = phi(moduli[-1])
        if next_m == 1:
            break
        moduli.append(next_m)

    # Evaluate tower from top (mod 1) to bottom (mod m)
    curr_val = 1
    for mod in reversed(moduli):
        curr_val = pow(a, curr_val, mod)

    # Return last 8 digits of the tetration
    return curr_val


if __name__ == "__main__":
    print(solve())
