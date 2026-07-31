def solve(sx, sy, fx, fy, t):
    horizontal = abs(sx - fx)
    vertical = abs(sy - fy)
    if horizontal == 0 and vertical == 0 and t == 1:
        return False
    return max(horizontal, vertical) <= t
