import math


def solve(rows: int = 51) -> int:
    """Find sum of distinct squarefree binomial coefficients in first `rows` of Pascal's triangle.
    
    Time Complexity: O(rows^2 * pi(rows))
    Space Complexity: O(rows^2)
    """
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

    distinct_nums = set()
    for n in range(rows):
        for k in range(n + 1):
            distinct_nums.add(math.comb(n, k))

    squarefree_sum = sum(
        x for x in distinct_nums if all(x % psq != 0 for psq in prime_squares)
    )

    return squarefree_sum
