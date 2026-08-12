def solve(n: int = 70) -> int:
    """Find number of closed robot journeys of length n (n is multiple of 5).
    
    Time Complexity: O((n/5)^5 * 5)
    Space Complexity: O((n/5)^5 * 5)
    """
    target_c = n // 5
    memo = {}

    def dp(c0, c1, c2, c3, c4, o):
        if (
            c0 > target_c
            or c1 > target_c
            or c2 > target_c
            or c3 > target_c
            or c4 > target_c
        ):
            return 0
        if (
            c0 == target_c
            and c1 == target_c
            and c2 == target_c
            and c3 == target_c
            and c4 == target_c
        ):
            return 1 if o == 0 else 0

        state = (c0, c1, c2, c3, c4, o)
        if state in memo:
            return memo[state]

        # CW step:
        c_cw = [c0, c1, c2, c3, c4]
        c_cw[o] += 1
        res_cw = dp(c_cw[0], c_cw[1], c_cw[2], c_cw[3], c_cw[4], (o - 1) % 5)

        # CCW step:
        new_o = (o + 1) % 5
        c_ccw = [c0, c1, c2, c3, c4]
        c_ccw[new_o] += 1
        res_ccw = dp(c_ccw[0], c_ccw[1], c_ccw[2], c_ccw[3], c_ccw[4], new_o)

        res = res_cw + res_ccw
        memo[state] = res
        return res

    return dp(0, 0, 0, 0, 0, 0)
