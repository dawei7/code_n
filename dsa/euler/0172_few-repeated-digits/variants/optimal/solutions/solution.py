import math


def solve(length: int = 18, max_repeat: int = 3) -> int:
    """Find number of length-digit numbers without leading zero where no digit occurs more than max_repeat times.
    
    Time Complexity: O((max_repeat + 1)^10)
    Space Complexity: O(length)
    """
    fact = [math.factorial(i) for i in range(length + 1)]
    total_count = 0

    def dfs(digit: int, rem_length: int, curr_fact_prod: int, c0: int):
        nonlocal total_count
        if digit == 9:
            c9 = rem_length
            if 0 <= c9 <= max_repeat:
                fact_prod = curr_fact_prod * fact[c9]
                valid_perms = (length - c0) * (fact[length - 1] // fact_prod)
                total_count += valid_perms
            return

        for c in range(min(max_repeat, rem_length) + 1):
            dfs(
                digit + 1,
                rem_length - c,
                curr_fact_prod * fact[c],
                c if digit == 0 else c0
            )

    dfs(0, length, 1, 0)
    return total_count
