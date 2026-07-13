from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # dp[i][v] stores the max length of a good subsequence 
    # ending with value v having exactly i mismatches.
    # We also track the global max for each i and the best value for each i.
    
    # dp[i] is a dictionary: {value: max_length}
    dp = [defaultdict(int) for _ in range(k + 1)]
    
    # max_vals[i] stores (max_len_1, val_1, max_len_2, val_2)
    # to allow O(1) transition when the current element matches the best value.
    max_vals = [[0, -1, 0, -1] for _ in range(k + 1)]
    
    for x in nums:
        for i in range(k, -1, -1):
            # Option 1: Extend a subsequence ending in x (0 mismatches added)
            res = dp[i][x] + 1
            
            # Option 2: Extend a subsequence ending in a different value (1 mismatch added)
            if i > 0:
                # Use the best value that isn't x to minimize mismatches
                best_len, best_val, second_len, second_val = max_vals[i-1]
                if best_val != x:
                    res = max(res, best_len + 1)
                else:
                    res = max(res, second_len + 1)
            
            # Update DP table
            if res > dp[i][x]:
                dp[i][x] = res
                
                # Update max_vals for this mismatch level i
                m1, v1, m2, v2 = max_vals[i]
                if x == v1:
                    max_vals[i][0] = res
                elif res > m1:
                    max_vals[i] = [res, x, m1, v1]
                elif res > m2 and x != v1:
                    max_vals[i][2] = res
                    max_vals[i][3] = x
                    
    return max(max_vals[i][0] for i in range(k + 1))
