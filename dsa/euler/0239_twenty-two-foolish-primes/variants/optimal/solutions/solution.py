from decimal import Decimal, getcontext
import math


def solve(total_disks: int = 100, num_primes: int = 25, foolish: int = 22) -> str:
    """Find probability that exactly 22 prime discs out of 25 are foolish, rounded to 12 decimal places.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Generalized Partial Derangements:
       Out of total = 100 discs, exactly num_primes = 25 are prime.
       A prime disc is 'foolish' if it is displaced from its natural position.
       We require exactly foolish = 22 prime discs to be displaced, meaning exactly
       fixed = num_primes - foolish = 3 prime discs remain in their natural positions.

    2. Inclusion-Exclusion on Constrained Subsets:
       - There are C(25, 3) ways to choose which 3 primes remain in natural positions.
       - The remaining 22 primes must all be displaced within the remaining 97 positions.
       - By inclusion-exclusion, the number of valid arrangements of the remaining 97 elements is:
           N_deranged = sum_{m=0}^{22} (-1)^m * C(22, m) * (97 - m)!.

    3. Probability Calculation:
       The total number of unrestricted permutations of 100 disks is 100!.
           P = [ C(25, 3) * sum_{m=0}^{22} (-1)^m * C(22, m) * (97 - m)! ] / 100!.

    Complexity:
    -----------
    - Time Complexity: O(foolish) = 23 iterations (< 0.001 seconds).
    - Space Complexity: O(1) high-precision Decimal state.
    """
    getcontext().prec = 50

    fixed_primes = num_primes - foolish
    ways_choose_fixed = math.comb(num_primes, fixed_primes)

    sum_terms = Decimal(0)
    for m in range(foolish + 1):
        comb_m = math.comb(foolish, m)
        fact_rem = math.factorial(total_disks - fixed_primes - m)
        term = ((-1) ** m) * comb_m * fact_rem
        sum_terms += Decimal(term)

    total_fact = Decimal(math.factorial(total_disks))
    prob = (Decimal(ways_choose_fixed) * sum_terms) / total_fact
    return f"{prob:.12f}"


if __name__ == "__main__":
    print(solve())
