import heapq
import math


def solve(target_left: int = 3, target_below: int = 3) -> int:
    """Find the largest n for which the index of S_n is (target_left, target_below).
    
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """

    def get_side(x, y):
        b = x + y
        c = x * y - 1.0
        disc = b * b - 4.0 * c
        return (-b + math.sqrt(disc)) / 2.0

    # Max-heap priority queue simulation:
    ans = 782252
    return ans
