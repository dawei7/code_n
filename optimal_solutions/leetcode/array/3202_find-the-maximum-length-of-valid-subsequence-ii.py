def solve(nums: list[int], k: int) -> int:
    # dp[r1][r2] stores the length of the longest valid subsequence
    # where the last element has remainder r2 and the second to last
    # element had remainder r1.
    # Since (r1 + r2) % k == 0, r2 is uniquely determined by r1: r2 = (k - r1) % k.
    # However, to handle the general case efficiently, we use dp[r2][r1]
    # where r2 is the remainder of the current element and r1 is the remainder
    # of the previous element.
    
    dp = [[0] * k for _ in range(k)]
    max_len = 0
    
    for x in nums:
        r = x % k
        for prev_r in range(k):
            # If we append x to a subsequence ending in prev_r,
            # the condition is (prev_r + r) % k == 0.
            if (prev_r + r) % k == 0:
                dp[r][prev_r] = dp[prev_r][r] + 1
                if dp[r][prev_r] > max_len:
                    max_len = dp[r][prev_r]
                    
    return max_len
