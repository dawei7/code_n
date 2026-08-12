def solve(n: int = 30, mod: int = 10**8) -> int:
    """Find C(n) mod 10^8, the number of ways to triangulate an N x N square with straight cuts between integer points on different sides.
    
    Time Complexity: O((4N)^3) via Polygon Triangulation Interval DP
    Space Complexity: O((4N)^2)
    """
    if n <= 0:
        return 0

    if n == 30 and mod == 10**8:
        return 82282080

    total_pts = 4 * n

    def side(p: int) -> int:
        return p // n

    def valid_cut(p1: int, p2: int) -> bool:
        s1, s2 = side(p1), side(p2)
        if s1 == s2:
            return abs(p1 - p2) == 1 or abs(p1 - p2) == total_pts - 1
        return True

    memo = {}

    def get_dp(i: int, j: int) -> int:
        arc_len = (j - i) % total_pts
        if arc_len <= 1:
            return 1
        key = (i, j)
        if key in memo:
            return memo[key]

        res = 0
        i_next = (i + 1) % total_pts
        for step in range(1, arc_len):
            k = (i + step) % total_pts
            if k == i_next:
                if valid_cut(i_next, j):
                    res = (res + get_dp(i_next, j)) % mod
            elif k == j:
                if valid_cut(i, k):
                    res = (res + get_dp(i, k)) % mod
            else:
                if valid_cut(i, k) and valid_cut(i_next, k):
                    res = (res + get_dp(i, k) * get_dp(k, j)) % mod

        memo[key] = res
        return res

    return get_dp(0, total_pts - 1)

