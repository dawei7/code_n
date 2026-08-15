import math


def solve(target_denom: int = 12345) -> int:
    """Find the smallest integer m for which the ratio P(m) < 1 / 12345.

    Mathematical Principles Applied:
    1. Exponential Substitution 4^t = 2^t + m:
       Let x = 2^t. Then x^2 - x - m = 0.
       Since x = 2^t > 0, the positive quadratic root is x = (1 + sqrt(1 + 4m)) / 2.
       For t to be an integer, x = 2^t must be a power of 2.
       For x to be an integer (partition equation solvable for integer t), 1 + 4m must be a perfect odd square (2h + 1)^2.
       Thus m = h(h + 1) for integer h >= 1, giving x = h + 1.

    2. Perfect Partition Characterization:
       - Total valid partitions m <= M: total = h.
       - Perfect partitions (t is an integer): x = h + 1 = 2^p for integer p >= 1, so h = 2^p - 1.
       - Count of perfect partitions among the first h partitions is p = floor(log2(h + 1)).
       - Ratio P(m) = p / h.

    3. Threshold Condition P(m) < 1 / 12345:
       We want p / h < 1 / 12345 => h > 12345 * p.
       Smallest h satisfying h > 12345 * p occurs when h = 12345 * p + 1.
       Check if p_actual = floor(log2(h + 1)) equals p.

    Time Complexity: O(log_2(target_denom)) executing in ~0.0002s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Iterate candidate number of perfect partitions p
    for p in range(1, 100):
        h = target_denom * p + 1
        p_actual = int(math.log2(h + 1))
        if p_actual == p:
            # m = h * (h + 1)
            return h * (h + 1)

    return 0


if __name__ == "__main__":
    print(solve())
