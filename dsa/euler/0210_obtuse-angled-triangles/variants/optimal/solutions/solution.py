import math


def solve(r: int = 10**9) -> int:
    """Find N(r), the number of points B in S(r) such that triangle OBC is obtuse.
    
    Time Complexity: O(r / 8) with integer circle stepping.
    Space Complexity: O(1)
    """
    R_TOTAL = r
    K = R_TOTAL // 8
    R_sq = 2 * K * K - 1
    max_X = math.isqrt(R_sq)

    total = 0
    Y = max_X
    for X in range(1, max_X + 1):
        rem = R_sq - X * X
        while Y * Y > rem:
            Y -= 1
        total += Y

    total_disk_points = 1 + 4 * total
    collinear_inside = 2 * K - 1
    cnt_B = total_disk_points - collinear_inside
    cnt_OC = (3 * R_TOTAL * R_TOTAL) // 2

    return cnt_OC + cnt_B
