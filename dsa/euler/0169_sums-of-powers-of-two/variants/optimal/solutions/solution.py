def solve(n: int = 10**25) -> int:
    """Find number of ways to express n as sum of powers of 2 using each power at most twice.
    
    Time Complexity: O(log_2(n))
    Space Complexity: O(log_2(n))
    """
    memo = {0: 1, 1: 1}

    def f(k: int) -> int:
        if k in memo:
            return memo[k]
        if k % 2 == 1:
            ans = f(k // 2)
        else:
            ans = f(k // 2) + f(k // 2 - 1)
        memo[k] = ans
        return ans

    return f(n)
