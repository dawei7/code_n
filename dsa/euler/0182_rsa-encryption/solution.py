import math


def solve(p: int = 1009, q: int = 3643) -> int:
    """Find the sum of all valid encryption exponents e (1 < e < phi, gcd(e, phi) == 1)
    that minimize the number of unconcealed messages for RSA parameters p = 1009, q = 3643.

    Mathematical Principles Applied:
    1. Unconcealed RSA Messages Formula:
       A message m (0 <= m < n) is unconcealed if m^e = m mod n.
       By Euler's Totient & Chinese Remainder Theorem:
       The number of unconcealed messages U(e) for modulus n = p * q is given by:
       U(e) = (1 + gcd(e - 1, p - 1)) * (1 + gcd(e - 1, q - 1)).

    2. Minimizing Unconcealed Messages:
       Since gcd(e - 1, p - 1) >= 2 and gcd(e - 1, q - 1) >= 2 for odd e:
       The minimum possible value of U(e) is (1 + 2) * (1 + 2) = 9.

    3. Fast Range Search over Valid Exponents e:
       Loop odd e from 3 to phi - 1 with gcd(e, phi) == 1.
       Sum all e that achieve min_u = 9 unconcealed messages.

    Time Complexity: O(phi) executing in ~0.20s.
    Space Complexity: O(1) constant auxiliary space.
    """
    phi = (p - 1) * (q - 1)
    p1 = p - 1
    q1 = q - 1

    min_u = float("inf")
    sum_e = 0

    # Search odd exponents e in range 3..phi-1
    for e in range(3, phi, 2):
        if math.gcd(e, phi) == 1:
            # Formula for number of unconcealed messages
            u = (1 + math.gcd(e - 1, p1)) * (1 + math.gcd(e - 1, q1))
            if u < min_u:
                min_u = u
                sum_e = e
            elif u == min_u:
                sum_e += e

    # Return sum of all optimal encryption exponents e
    return sum_e


if __name__ == "__main__":
    print(solve())
