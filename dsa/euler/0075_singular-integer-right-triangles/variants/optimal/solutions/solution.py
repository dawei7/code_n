import math


def solve(limit: int = 1500000) -> int:
    """Find number of wire lengths L <= limit that can form EXACTLY ONE integer right triangle.
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(limit)
    """
    counts = [0] * (limit + 1)
    max_m = int((limit // 2) ** 0.5)

    for m in range(2, max_m + 1):
        for n in range(1 + (m % 2), m, 2):  # Ensure opposite parity
            if math.gcd(m, n) == 1:
                l0 = 2 * m * (m + n)
                for perim in range(l0, limit + 1, l0):
                    counts[perim] += 1

    return sum(1 for c in counts if c == 1)
