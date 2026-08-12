from fractions import Fraction
import math


def solve(k: int = 35) -> int:
    """Find u + v where u/v = sum of distinct s(x,y,z) = x+y+z for golden triples of order k.
    
    Time Complexity: O(Rationals(k)^2)
    Space Complexity: O(Rationals(k)^2)
    """
    rationals = []
    for b in range(2, k + 1):
        for a in range(1, b):
            if math.gcd(a, b) == 1:
                rationals.append(Fraction(a, b))

    rational_set = set(rationals)
    distinct_sums = set()

    for i in range(len(rationals)):
        x = rationals[i]
        for j in range(len(rationals)):
            y = rationals[j]

            # 1. z = x + y
            z1 = x + y
            if z1 in rational_set:
                distinct_sums.add(x + y + z1)

            # 2. 1/z = 1/x + 1/y => z = xy / (x + y)
            z2 = (x * y) / (x + y)
            if z2 in rational_set:
                distinct_sums.add(x + y + z2)

            # 3. z^2 = x^2 + y^2
            sq3 = x * x + y * y
            num_sq3, den_sq3 = sq3.numerator, sq3.denominator
            isq_num, isq_den = math.isqrt(num_sq3), math.isqrt(den_sq3)
            if isq_num * isq_num == num_sq3 and isq_den * isq_den == den_sq3:
                z3 = Fraction(isq_num, isq_den)
                if z3 in rational_set:
                    distinct_sums.add(x + y + z3)

                # 4. 1/z^2 = 1/x^2 + 1/y^2 => z = xy / sqrt(x^2 + y^2)
                z4 = (x * y) / z3
                if z4 in rational_set:
                    distinct_sums.add(x + y + z4)

    t = sum(distinct_sums)
    return t.numerator + t.denominator
