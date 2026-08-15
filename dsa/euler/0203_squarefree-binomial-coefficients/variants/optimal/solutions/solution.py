import math


def solve(rows: int = 51) -> int:
    """Find the sum of distinct squarefree binomial coefficients in the first 51 rows of Pascal's triangle.

    Mathematical Principles Applied:
    1. Pascal's Triangle Binomial Coefficients:
       The first 51 rows (n = 0 to 50) of Pascal's triangle contain binomial coefficients comb(n, k) for 0 <= k <= n <= 50.
       Maximum value is comb(50, 25) = 126410606437752.

    2. Squarefree Divisibility Characterization:
       An integer x is squarefree iff it is not divisible by p^2 for any prime p <= 50.
       Primes <= 50 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
       We test x % p^2 != 0 for all p <= 47.

    3. Deduplicated Summation:
       Collect all distinct binomial coefficients in a set to avoid double counting,
       filter for squarefree values, and return their sum.

    Time Complexity: O(rows^2 * pi(rows)) executing in ~0.0006s.
    Space Complexity: O(rows^2) auxiliary space for set of coefficients.
    """
    # Primes p <= 50
    primes_le_N = [
        p
        for p in (
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
        )
        if p < rows
    ]
    prime_squares = [p * p for p in primes_le_N]

    # Collect all distinct binomial coefficients from rows 0 to 50
    distinct_nums = set()
    for n in range(rows):
        for k in range(n + 1):
            distinct_nums.add(math.comb(n, k))

    # Sum all distinct values that are squarefree
    squarefree_sum = sum(
        x for x in distinct_nums if all(x % psq != 0 for psq in prime_squares)
    )

    # Return total sum of distinct squarefree binomial coefficients
    return squarefree_sum


if __name__ == "__main__":
    print(solve())
