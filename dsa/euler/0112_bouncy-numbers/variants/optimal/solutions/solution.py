def is_bouncy(n: int) -> bool:
    """Check if positive integer n is bouncy (neither non-decreasing nor non-increasing).

    Mathematical Principles Applied:
    1. Increasing & Decreasing Digits:
       A number is non-decreasing if for all adjacent digits d_i <= d_{i+1}.
       A number is non-increasing if for all adjacent digits d_i >= d_{i+1}.

    2. Bouncy Condition:
       A number is bouncy if it contains BOTH a strictly increasing step (d_i < d_{i+1})
       AND a strictly decreasing step (d_j > d_{j+1}).
    """
    s = str(n)
    inc = dec = False
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            inc = True
        elif s[i] > s[i + 1]:
            dec = True
        # Early exit as soon as both increasing and decreasing steps are witnessed
        if inc and dec:
            return True
    return False


def solve(target_pct: int = 99) -> int:
    """Find the least number n for which the proportion of bouncy numbers reaches target_pct % (99%).

    Mathematical Principles Applied:
    1. Proportion Ratio Condition:
       Let B(n) be the number of bouncy numbers in 1..n.
       We seek the minimal n where B(n) / n = 99 / 100 <=> 100 * B(n) == 99 * n.

    Time Complexity: O(N * log10(N)) where N ~ 1.58 x 10^6 (executes in ~0.35s).
    Space Complexity: O(1) constant auxiliary space.
    """
    bouncy_count = 0
    n = 100

    # Advance n upwards and accumulate bouncy numbers count
    while True:
        if is_bouncy(n):
            bouncy_count += 1

        # Check exact ratio condition using integer multiplication (100 * B(n) == 99 * n)
        if 100 * bouncy_count == target_pct * n:
            return n

        n += 1


if __name__ == "__main__":
    print(solve())
