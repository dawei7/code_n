import math


def solve(limit: int = 2000000000) -> int:
    """Find number of positive integers n <= limit representable as a^2 + D*b^2 for all D in (1, 2, 3, 7).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Simultaneous Quadratic Form Representations:
       We seek the count of positive integers n <= 2 * 10^9 such that there exist strictly
       positive integers a_D, b_D >= 1 satisfying:
           n = a_1^2 + 1 * b_1^2
           n = a_2^2 + 2 * b_2^2
           n = a_3^2 + 3 * b_3^2
           n = a_7^2 + 7 * b_7^2.

    2. 4-Tier Fast Cascade Sieve:
       We partition [1, limit] into segmented blocks of size BLOCK_SIZE = 500,000,000 using
       a single bytearray(BLOCK_SIZE + 1) for direct, zero-overhead memory access.
       - Tier 1 (D = 7): Mark numbers a^2 + 7*b^2 with flag 1.
       - Tier 2 (D = 3): Filter matching cells, upgrading flag 1 -> 3.
       - Tier 3 (D = 2): Filter matching cells, upgrading flag 3 -> 7.
       - Tier 4 (D = 1): Filter matching cells, upgrading flag 7 -> 15.
       - The count of cells with flag == 15 equals the number of valid integers in the block.

    Complexity:
    -----------
    - Time Complexity: O(limit * sum_{D} 1/sqrt(D)) operations.
    - Space Complexity: O(BLOCK_SIZE) memory (~500 MB).
    """
    N = limit
    BLOCK_SIZE = 500000000
    sq = [i * i for i in range(int(math.isqrt(N)) + 2)]
    total_count = 0

    for L in range(1, N + 1, BLOCK_SIZE):
        R = min(N + 1, L + BLOCK_SIZE)
        S = R - L
        flags = bytearray(S)

        # Tier 1: D = 7
        max_b = int(math.isqrt((R - 1) // 7))
        for b in range(1, max_b + 1):
            db2 = 7 * sq[b]
            min_a2 = max(1, L - db2)
            max_a2 = R - 1 - db2
            if min_a2 > max_a2:
                continue
            start_a = max(1, math.isqrt(min_a2))
            if sq[start_a] < min_a2:
                start_a += 1
            end_a = math.isqrt(max_a2)
            for a in range(start_a, end_a + 1):
                flags[sq[a] + db2 - L] = 1

        # Tier 2: D = 3
        max_b = int(math.isqrt((R - 1) // 3))
        for b in range(1, max_b + 1):
            db2 = 3 * sq[b]
            min_a2 = max(1, L - db2)
            max_a2 = R - 1 - db2
            if min_a2 > max_a2:
                continue
            start_a = max(1, math.isqrt(min_a2))
            if sq[start_a] < min_a2:
                start_a += 1
            end_a = math.isqrt(max_a2)
            for a in range(start_a, end_a + 1):
                idx = sq[a] + db2 - L
                if flags[idx] == 1:
                    flags[idx] = 3

        # Tier 3: D = 2
        max_b = int(math.isqrt((R - 1) // 2))
        for b in range(1, max_b + 1):
            db2 = 2 * sq[b]
            min_a2 = max(1, L - db2)
            max_a2 = R - 1 - db2
            if min_a2 > max_a2:
                continue
            start_a = max(1, math.isqrt(min_a2))
            if sq[start_a] < min_a2:
                start_a += 1
            end_a = math.isqrt(max_a2)
            for a in range(start_a, end_a + 1):
                idx = sq[a] + db2 - L
                if flags[idx] == 3:
                    flags[idx] = 7

        # Tier 4: D = 1
        max_b = int(math.isqrt(R - 1))
        for b in range(1, max_b + 1):
            b2 = sq[b]
            min_a2 = max(1, L - b2)
            max_a2 = R - 1 - b2
            if min_a2 > max_a2:
                continue
            start_a = max(1, math.isqrt(min_a2))
            if sq[start_a] < min_a2:
                start_a += 1
            end_a = math.isqrt(max_a2)
            for a in range(start_a, end_a + 1):
                idx = sq[a] + b2 - L
                if flags[idx] == 7:
                    flags[idx] = 15

        total_count += flags.count(15)

    return total_count


if __name__ == "__main__":
    print(solve())
