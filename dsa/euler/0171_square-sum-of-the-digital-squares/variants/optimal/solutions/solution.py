import math


def solve(num_digits: int = 20) -> str:
    """Find last 9 digits of sum of all n (0 < n < 10^num_digits) whose sum of squared digits is a perfect square.
    
    Time Complexity: O(num_digits * Max_Sq_Sum * 10)
    Space Complexity: O(num_digits * Max_Sq_Sum)
    """
    MOD = 10**9
    squares = set(i * i for i in range(1, int(math.isqrt(num_digits * 81)) + 1))
    memo = {}

    def dp(idx: int, sq_sum: int) -> tuple[int, int]:
        if idx == num_digits:
            if sq_sum in squares:
                return (1, 0)
            return (0, 0)

        key = (idx, sq_sum)
        if key in memo:
            return memo[key]

        total_cnt = 0
        total_val = 0
        pow10 = pow(10, num_digits - 1 - idx, MOD)

        for d in range(10):
            cnt, val = dp(idx + 1, sq_sum + d * d)
            total_cnt = (total_cnt + cnt) % MOD
            total_val = (total_val + val + cnt * d * pow10) % MOD

        memo[key] = (total_cnt, total_val)
        return (total_cnt, total_val)

    _, val = dp(0, 0)
    return f"{val:09d}"
