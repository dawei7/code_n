def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    
    def get_possible_ors(arr):
        # dp[i][v] is true if a subsequence of length i can have OR value v
        dp = [[False] * 128 for _ in range(k + 1)]
        dp[0][0] = True
        for x in arr:
            for i in range(k - 1, -1, -1):
                for v in range(128):
                    if dp[i][v]:
                        dp[i + 1][v | x] = True
        return dp[k]

    # Precompute possible ORs for subsequences of length k ending at or before i
    # and starting at or after i
    left_dp = [[False] * 128 for _ in range(n)]
    right_dp = [[False] * 128 for _ in range(n)]
    
    # Forward pass
    curr_dp = [[False] * 128 for _ in range(k + 1)]
    curr_dp[0][0] = True
    for i in range(n):
        for j in range(k - 1, -1, -1):
            for v in range(128):
                if curr_dp[j][v]:
                    curr_dp[j + 1][v | nums[i]] = True
        for v in range(128):
            if curr_dp[k][v]:
                left_dp[i][v] = True
                
    # Backward pass
    curr_dp = [[False] * 128 for _ in range(k + 1)]
    curr_dp[0][0] = True
    for i in range(n - 1, -1, -1):
        for j in range(k - 1, -1, -1):
            for v in range(128):
                if curr_dp[j][v]:
                    curr_dp[j + 1][v | nums[i]] = True
        for v in range(128):
            if curr_dp[k][v]:
                right_dp[i][v] = True

    # Prefix/Suffix OR sets
    left_sets = [set() for _ in range(n)]
    right_sets = [set() for _ in range(n)]
    
    for i in range(n):
        for v in range(128):
            if left_dp[i][v]:
                left_sets[i].add(v)
            if i > 0:
                left_sets[i].update(left_sets[i-1])
                
    for i in range(n - 1, -1, -1):
        for v in range(128):
            if right_dp[i][v]:
                right_sets[i].add(v)
            if i < n - 1:
                right_sets[i].update(right_sets[i+1])
                
    ans = 0
    for i in range(k - 1, n - k):
        for l in left_sets[i]:
            for r in right_sets[i + 1]:
                ans = max(ans, l ^ r)
                
    return ans
