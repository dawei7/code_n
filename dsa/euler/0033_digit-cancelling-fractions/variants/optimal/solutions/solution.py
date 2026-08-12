import math


def solve() -> int:
    """Find denominator of product of four non-trivial digit-cancelling fractions in lowest terms.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    num_prod = 1
    den_prod = 1

    for a in range(10, 100):
        for b in range(a + 1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue

            sa, sb = str(a), str(b)
            common = set(sa) & set(sb)
            if common:
                for digit in common:
                    new_sa = sa.replace(digit, "", 1)
                    new_sb = sb.replace(digit, "", 1)
                    if new_sa and new_sb and new_sb != "0":
                        c, e = int(new_sa), int(new_sb)
                        if a * e == b * c:
                            num_prod *= a
                            den_prod *= b
                            break

    return den_prod // math.gcd(num_prod, den_prod)
