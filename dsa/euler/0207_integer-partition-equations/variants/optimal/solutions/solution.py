import math


def solve(target_denom: int = 12345) -> int:
    """Find smallest m for which P(m) < 1 / target_denom.
    
    Time Complexity: O(log_2(target_denom))
    Space Complexity: O(1)
    """
    for p in range(1, 100):
        h = target_denom * p + 1
        p_actual = int(math.log2(h + 1))
        if p_actual == p:
            return h * (h + 1)
    return 0
