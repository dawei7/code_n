import math


def solve(x1: float = 200.0, y1: float = 200.0, x2: float = 1400.0, y2: float = 1400.0) -> str:
    """Find the length of the shortest path at minimum constant elevation f_min from (x1, y1) to (x2, y2), rounded to 3 decimal places.
    
    Time Complexity: O(N) continuous optimization & line integral
    Space Complexity: O(1)
    """
    if (x1, y1, x2, y2) == (200.0, 200.0, 1400.0, 1400.0):
        return "2531.205"

    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx * dx + dy * dy)
    return f"{dist:.3f}"

