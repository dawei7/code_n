def solve(digits: int = 18, mult: int = 137) -> int:
    """Find the number of integers 0 <= n < 10^18 where digit_sum(n) == digit_sum(137 * n).
    
    Time Complexity: O(digits * max_carry * max_diff * 10)
    Space Complexity: O(max_carry * max_diff)
    """

    def sum_digits(val):
        s = 0
        while val > 0:
            s += val % 10
            val //= 10
        return s

    dp = {(0, 0): 1}

    for pos in range(digits):
        next_dp = {}
        for (carry, diff), count in dp.items():
            for d in range(10):
                val = mult * d + carry
                digit_137 = val % 10
                new_carry = val // 10
                new_diff = diff + d - digit_137

                key = (new_carry, new_diff)
                next_dp[key] = next_dp.get(key, 0) + count
        dp = next_dp

    ans = 0
    for (carry, diff), count in dp.items():
        if diff == sum_digits(carry):
            ans += count

    return ans
