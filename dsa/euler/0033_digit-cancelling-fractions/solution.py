import math


def solve() -> int:
    """Find the denominator of the product of the four non-trivial digit-cancelling fractions in lowest terms.

    Mathematical Principles Applied:
    1. Fraction Definition & Domain:
       A fraction a / b where 10 <= a < b < 100 has a non-trivial cancellation if:
       - a and b share a common digit d != 0.
       - Trivial cases like 30/50 = 3/5 (trailing zeros) are explicitly excluded.
       - The simplified fraction after removing d equals the original fraction a / b.

    2. Cross-Multiplication Equality:
       If cancelling digit d leaves remaining digits c and e (where a = 10d + c or 10c + d, etc.),
       a / b == c / e iff a * e == b * c.

    3. Product Reduction to Lowest Terms:
       Multiply numerators num_prod = prod(a_i) and denominators den_prod = prod(b_i).
       Simplified denominator = den_prod // gcd(num_prod, den_prod).

    Time Complexity: O(1) over 90x90 fraction pairs (executes in ~0.001s).
    Space Complexity: O(1) constant auxiliary space.
    """
    num_prod = 1
    den_prod = 1

    # Iterate through all 2-digit numerators a from 10 to 98
    for a in range(10, 100):
        # Iterate through all 2-digit denominators b from a + 1 to 99 (strictly less than 1)
        for b in range(a + 1, 100):
            # Exclude trivial multiples of 10 (e.g. 30/50)
            if a % 10 == 0 and b % 10 == 0:
                continue

            sa, sb = str(a), str(b)

            # Find common digits between numerator string and denominator string
            common = set(sa) & set(sb)

            if common:
                for digit in common:
                    # Cancel the first occurrence of common digit
                    new_sa = sa.replace(digit, "", 1)
                    new_sb = sb.replace(digit, "", 1)

                    # Ensure non-empty remaining strings and non-zero denominator
                    if new_sa and new_sb and new_sb != "0":
                        c, e = int(new_sa), int(new_sb)

                        # Test cross-multiplication: a / b == c / e <=> a * e == b * c
                        if a * e == b * c:
                            num_prod *= a
                            den_prod *= b
                            break

    # Reduce product fraction to lowest terms and return denominator
    return den_prod // math.gcd(num_prod, den_prod)


if __name__ == "__main__":
    print(solve())
