def solve(rows: int = 1000000000) -> int:
    """Find the number of entries not divisible by 7 in the first 1,000,000,000 rows of Pascal's triangle.

    Mathematical Principles Applied:
    1. Lucas' Theorem & Base-7 Digit Product Theorem:
       By Lucas' Theorem, the binomial coefficient C(n, k) is not divisible by prime p=7 iff
       each base-7 digit k_i <= n_i for all digit positions i.
       The number of non-divisible entries in row n is:
       f(n) = prod_{i} (n_i + 1).

    2. Fractured Base-7 Block Recurrence:
       Let n be expressed in base-7 with most significant digit d and remainder rem:
       n = d * 7^k + rem (where 0 <= d < 7, 0 <= rem < 7^k).
       - Full 7^k blocks count: (d * (d + 1) / 2) * 28^k (since a full 7x7 block has 28 non-divisible entries).
       - Partial 7^k block count: (d + 1) * f(rem).

    Time Complexity: O(log_7(rows)) executing in ~0.0000s.
    Space Complexity: O(log_7(rows)) call stack depth.
    """

    def count_not_div_7(n: int) -> int:
        if n == 0:
            return 0

        # Find largest power of 7 <= n
        p7 = 1
        power = 0
        while p7 * 7 <= n:
            p7 *= 7
            power += 1

        d = n // p7
        rem = n % p7

        # Calculate full blocks contribution (28 entries per 7^1 block)
        full_blocks = (d * (d + 1) // 2) * (28**power)
        # Calculate partial remaining block contribution recursively
        partial_block = (d + 1) * count_not_div_7(rem)

        return full_blocks + partial_block

    # Return total count of non-divisible-by-7 entries in 10^9 rows of Pascal's triangle
    return count_not_div_7(rows)


if __name__ == "__main__":
    print(solve())
