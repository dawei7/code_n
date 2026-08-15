import math


def solve(num_digits: int = 20) -> str:
    """Find the last 9 digits of the sum of all n (0 < n < 10^20) whose sum of squared digits is a perfect square.

    Mathematical Principles Applied:
    1. Digit DP State Tracking (Count and Value):
       For a 20-digit number represented from left to right at digit position idx (0 <= idx < 20):
       State is represented by `(idx, sq_sum)` where `sq_sum = sum(d_i^2)`.
       DP function `dp(idx, sq_sum)` returns tuple `(total_count, total_value)` modulo 10^9.

    2. Value Aggregation via Linear Place Values:
       At digit position `idx`, choosing digit d (0 <= d <= 9) contributes place value `d * 10^(num_digits - 1 - idx)`
       multiplied by `cnt` (the number of valid suffix completions)!
       `total_val = (total_val + val_suffix + cnt_suffix * d * 10^(num_digits - 1 - idx)) % 10^9`.

    3. Perfect Square Verification at Base Case (idx == 20):
       Check if `sq_sum` is a perfect square in `squares = {1^2, 2^2, ..., 40^2}` (max sum = 20 * 81 = 1620).

    Time Complexity: O(num_digits * Max_Sq_Sum * 10) executing in ~0.05s.
    Space Complexity: O(num_digits * Max_Sq_Sum) DP memo memory.
    """
    MOD = 10**9
    # Maximum possible squared digit sum is 20 * 81 = 1620 (sqrt(1620) = 40)
    squares = set(
        i * i for i in range(1, int(math.isqrt(num_digits * 81)) + 1)
    )
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

        # Branch on all 10 digits d (0..9)
        for d in range(10):
            cnt, val = dp(idx + 1, sq_sum + d * d)
            total_cnt = (total_cnt + cnt) % MOD
            total_val = (total_val + val + cnt * d * pow10) % MOD

        memo[key] = (total_cnt, total_val)
        return (total_cnt, total_val)

    # Evaluate DP for 20-digit numbers starting at idx=0 and sq_sum=0
    _, val = dp(0, 0)

    # Return last 9 digits formatted as zero-padded string
    return f"{val:09d}"


if __name__ == "__main__":
    print(solve())
