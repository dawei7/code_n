def cycle_length(d: int) -> int:
    """Find length of recurring cycle in 1/d using long division remainder tracking."""
    seen = {}
    rem = 1
    pos = 0
    while rem != 0:
        if rem in seen:
            return pos - seen[rem]
        seen[rem] = pos
        rem = (rem * 10) % d
        pos += 1
    return 0


def solve(limit: int = 1000) -> int:
    """Find d < limit with the longest recurring decimal cycle.
    
    Time Complexity: O(limit^2)
    Space Complexity: O(limit)
    """
    max_len = 0
    best_d = 0

    for d in range(limit - 1, 1, -1):
        if d <= max_len:
            break
        length = cycle_length(d)
        if length > max_len:
            max_len = length
            best_d = d

    return best_d
