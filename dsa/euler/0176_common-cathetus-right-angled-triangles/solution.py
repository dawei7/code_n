import math


def solve(target_triangles: int = 47547) -> int:
    """Find the smallest integer a that can be the length of a cathetus (leg) of exactly target_triangles right triangles.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Right-Angled Triangles with Common Leg a:
       Let the right triangle sides be a, b, c with a^2 + b^2 = c^2.
       Then c^2 - b^2 = (c - b)(c + b) = a^2.
       Let u = c - b and v = c + b. Then u * v = a^2 with u == v mod 2.
       - If a is odd: u and v are both odd factors of a^2 with u < v.
         The number of solutions is N(a) = (d(a^2) - 1) / 2.
       - If a is even: let a = 2^{e_0} * p_1^{e_1} * p_2^{e_2} * ...
         Then u and v must both be even, so (u/2) * (v/2) = a^2 / 4 = 2^{2e_0 - 2} * p_1^{2e_1} * ...
         The number of solutions is:
         N(a) = ( (2e_0 - 1) * (2e_1 + 1) * (2e_2 + 1) * ... - 1 ) / 2.

    2. Inverse Divisor Count Equation:
       In all cases:
           2 * N(a) + 1 = (2e_0 - 1) * (2e_1 + 1) * (2e_2 + 1) * ... * (2e_k + 1)
       For target_triangles = 47,547:
           Target Product = 2 * 47,547 + 1 = 95,095.

    3. Dynamic Multiplicative Partition & Greedy Prime Assignment:
       - Dynamically factor Target into all possible multiplicative partitions (f_0, f_1, ..., f_m).
       - For each partition, assign one factor f_0 to prime 2 with exponent e_0 = (f_0 + 1) // 2.
       - Sort remaining factors f_i in descending order and assign to smallest odd primes {3, 5, 7, 11, ...}
         with exponents e_i = (f_i - 1) // 2 to minimize the total product a.

    Complexity:
    -----------
    - Time Complexity: O(Multiplicative_Partitions(2N + 1)) operations (~0.0001s).
    - Space Complexity: O(log(2N + 1)) memory (~1 KB).
    """
    target = 2 * target_triangles + 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Generate all multiplicative partitions of target dynamically
    def get_factorizations(n: int, min_div: int = 2) -> list[list[int]]:
        res = [[n]]
        for d in range(min_div, int(math.isqrt(n)) + 1):
            if n % d == 0:
                for sub in get_factorizations(n // d, d):
                    res.append([d] + sub)
        return res

    factorizations = get_factorizations(target)
    min_a = float("inf")

    # Evaluate all factor groups and prime assignments
    for factor_group in factorizations:
        for i, f_2 in enumerate(factor_group):
            # Exponent for prime 2: (2e_0 - 1) = f_2 => e_0 = (f_2 + 1) // 2
            e_0 = (f_2 + 1) // 2
            rem_factors = factor_group[:i] + factor_group[i + 1 :]
            # Greedy heuristic: largest exponents to smallest odd primes
            rem_factors.sort(reverse=True)

            a = 2**e_0
            for j, f_odd in enumerate(rem_factors):
                e_j = (f_odd - 1) // 2
                a *= primes[j + 1] ** e_j
            min_a = min(min_a, a)

    # Return minimal integer leg a
    return int(min_a)


if __name__ == "__main__":
    print(solve())
