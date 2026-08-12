def is_bouncy(n: int) -> bool:
    """Check if number n is bouncy (neither strictly non-decreasing nor non-increasing)."""
    s = str(n)
    inc = dec = False
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            inc = True
        elif s[i] > s[i + 1]:
            dec = True
        if inc and dec:
            return True
    return False


def solve(target_pct: int = 99) -> int:
    """Find least number n for which proportion of bouncy numbers is target_pct %.
    
    Time Complexity: O(N * D)
    Space Complexity: O(1)
    """
    bouncy_count = 0
    n = 100

    while True:
        if is_bouncy(n):
            bouncy_count += 1

        if 100 * bouncy_count == target_pct * n:
            return n

        n += 1
