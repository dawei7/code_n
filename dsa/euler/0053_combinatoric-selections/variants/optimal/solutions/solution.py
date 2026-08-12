import math


def solve(limit: int = 100, threshold: int = 1000000) -> int:
    """Count values of (n choose r) for 1 <= n <= 100 that exceed threshold.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    count = 0
    for n in range(1, limit + 1):
        for r in range(1, n // 2 + 1):
            if math.comb(n, r) > threshold:
                # By symmetry, all values between r and n-r exceed threshold
                count += n - 2 * r + 1
                break
    return count
