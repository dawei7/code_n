from math import gcd


def solve(n):
    fractions = []
    for denominator in range(2, n + 1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                fractions.append(f"{numerator}/{denominator}")
    return fractions
