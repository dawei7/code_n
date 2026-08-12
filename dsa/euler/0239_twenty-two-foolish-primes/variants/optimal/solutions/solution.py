import math
from decimal import Decimal, getcontext


def solve() -> str:
    """Find probability that exactly 22 prime number discs out of 25 are away from their natural positions in a line of 100 disks.
    
    Time Complexity: O(P) where P = 22
    Space Complexity: O(1)
    """
    getcontext().prec = 50

    num_primes = 25
    fixed_primes = 3  # 25 - 22 = 3
    deranged_primes = 22
    total = 100

    ways_choose_3 = math.comb(num_primes, fixed_primes)

    sum_terms = Decimal(0)
    for m in range(deranged_primes + 1):
        comb_m = math.comb(deranged_primes, m)
        fact = math.factorial(total - fixed_primes - m)
        term = ((-1) ** m) * comb_m * fact
        sum_terms += Decimal(term)

    total_fact = Decimal(math.factorial(total))
    prob = (Decimal(ways_choose_3) * sum_terms) / total_fact
    return f"{prob:.12f}"
