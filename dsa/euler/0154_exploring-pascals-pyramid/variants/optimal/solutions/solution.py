import numpy as np


def solve(N: int = 200000) -> int:
    """Find number of coefficients in (x+y+z)^N divisible by 10^12 = 2^12 * 5^12.
    
    Time Complexity: O(N^2 / Vectorization)
    Space Complexity: O(N)
    """
    f2 = np.zeros(N + 1, dtype=np.int32)
    f5 = np.zeros(N + 1, dtype=np.int32)

    for p, f in [(2, f2), (5, f5)]:
        v = 0
        for i in range(1, N + 1):
            x = i
            while x % p == 0:
                v += 1
                x //= p
            f[i] = v

    v2_N = f2[N]
    v5_N = f5[N]

    total_count = 0

    for i in range(0, N // 3 + 1):
        f5_i = f5[i]
        rem5_i = v5_N - f5_i
        if rem5_i < 12:
            continue

        f2_i = f2[i]
        rem2_i = v2_N - f2_i
        if rem2_i < 12:
            continue

        max_j = (N - i) // 2

        # Slices: j goes from i to max_j
        # k = N - i - j goes from N - 2*i down to N - i - max_j
        f5_j = f5[i:max_j + 1]
        f5_k = f5[N - 2 * i:N - i - max_j - 1:-1]

        mask5 = (rem5_i - f5_j - f5_k >= 12)
        if not np.any(mask5):
            continue

        f2_j = f2[i:max_j + 1][mask5]
        f2_k = f2[N - 2 * i:N - i - max_j - 1:-1][mask5]
        mask2 = (rem2_i - f2_j - f2_k >= 12)

        valid_j = np.arange(i, max_j + 1, dtype=np.int32)[mask5][mask2]
        valid_k = (N - i) - valid_j

        is_all_equal = (i == valid_j) & (valid_j == valid_k)
        is_two_equal = (i == valid_j) | (valid_j == valid_k) | (i == valid_k)

        c1 = int(np.sum(is_all_equal))
        c3 = int(np.sum(is_two_equal & ~is_all_equal))
        c6 = int(np.sum(~is_two_equal))

        total_count += c1 + 3 * c3 + 6 * c6

    return total_count
