import math


def solve(max_tiles: int = 1000000) -> int:
    """Find number of different square laminae that can be formed using up to max_tiles.
    
    Time Complexity: O(sqrt(max_tiles))
    Space Complexity: O(1)
    """
    M = max_tiles // 4
    return sum(M // x - x for x in range(1, int(math.isqrt(M)) + 1))
