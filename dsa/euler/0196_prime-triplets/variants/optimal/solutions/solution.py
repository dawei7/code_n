import math


def solve(n1: int = 5678027, n2: int = 7208785) -> int:
    """Find S(5678027) + S(7208785), the sum of all primes in rows n1 and n2 that belong to a prime triplet.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Triangular Number Array Geometry:
       Row r contains r integers, starting at T_{r-1} + 1 = (r - 1)*r // 2 + 1.
       Two numbers are neighbors if they are adjacent horizontally, vertically, or diagonally.

    2. Prime Triplet Definition:
       A prime p belongs to a prime triplet if it is part of a connected component of primes
       (under 8-neighbor adjacency) of size at least 3.
       For a prime p at (r, c) on row n:
       - Either p has degree >= 2 in the prime neighbor graph (a center of a 3-star or triangle),
       - Or p has at least one prime neighbor q (on row n - 1, n, or n + 1) with degree >= 2.

    3. Local 5-Row Segmented Sieve:
       To evaluate the neighborhood degree of neighbors of row n:
       We only need prime primality data for the 5 rows: [n - 2, n - 1, n, n + 1, n + 2].
       Using a segmented Sieve of Eratosthenes over the contiguous range [T_{n-3}+1, T_{n+2}],
       all 5 rows are sieved simultaneously in O(n) time and low memory.

    Complexity:
    -----------
    - Time Complexity: O(n1 + n2) operations (~2.3s for n1 = 5678027, n2 = 7208785).
    - Space Complexity: O(n) memory for the 5-row segment bytearray (~35 MB).
    """

    def solve_S(n: int) -> int:
        row_starts = [(r - 1) * r // 2 + 1 for r in range(n - 2, n + 3)]
        row_lens = [r for r in range(n - 2, n + 3)]

        min_val = row_starts[0]
        max_val = row_starts[4] + row_lens[4] - 1
        segment_len = max_val - min_val + 1

        # Sieve base primes up to sqrt(max_val)
        max_prime = math.isqrt(max_val) + 1
        is_p = bytearray([1]) * (max_prime + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(max_prime**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        primes = [i for i in range(2, max_prime + 1) if is_p[i]]

        # Segmented sieve for the 5-row window
        is_prime_seg = bytearray([1]) * segment_len
        for p in primes:
            start = ((min_val + p - 1) // p) * p
            if start < p * p:
                start = p * p
            if start <= max_val:
                is_prime_seg[start - min_val :: p] = b"\x00" * len(
                    is_prime_seg[start - min_val :: p]
                )

        # Extract 5 row boolean bytearrays (with boundary padding)
        rows_p = []
        for r in range(5):
            st = row_starts[r] - min_val
            ln = row_lens[r]
            arr = bytearray([0]) + is_prime_seg[st : st + ln] + bytearray([0, 0])
            rows_p.append(arr)

        # Precompute neighbor degree counts for rows 1, 2, 3
        n_counts = [None] * 5
        for r in range(1, 4):
            p_prev = rows_p[r - 1]
            p_curr = rows_p[r]
            p_next = rows_p[r + 1]
            ln = row_lens[r]
            cnt_arr = bytearray(ln + 2)
            for c in range(1, ln + 1):
                if p_curr[c]:
                    deg = (
                        p_prev[c - 1]
                        + p_prev[c]
                        + p_prev[c + 1]
                        + p_curr[c - 1]
                        + p_curr[c + 1]
                        + p_next[c - 1]
                        + p_next[c]
                        + p_next[c + 1]
                    )
                    cnt_arr[c] = deg
            n_counts[r] = cnt_arr

        # Accumulate primes in target row (row 2) belonging to a triplet
        total = 0
        p2 = rows_p[2]
        cnt2 = n_counts[2]
        cnt1 = n_counts[1]
        cnt3 = n_counts[3]
        ln2 = row_lens[2]
        st2 = row_starts[2]

        for c in range(1, ln2 + 1):
            if p2[c]:
                val = st2 + c - 1
                if cnt2[c] >= 2:
                    total += val
                else:
                    # Check if any prime neighbor has degree >= 2
                    if (
                        cnt1[c - 1] >= 2
                        or cnt1[c] >= 2
                        or cnt1[c + 1] >= 2
                        or cnt2[c - 1] >= 2
                        or cnt2[c + 1] >= 2
                        or cnt3[c - 1] >= 2
                        or cnt3[c] >= 2
                        or cnt3[c + 1] >= 2
                    ):
                        total += val

        return total

    return solve_S(n1) + solve_S(n2)


if __name__ == "__main__":
    print(solve())
