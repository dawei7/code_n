def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    
    # Find indices of all 1s
    ones_indices = [i for i, val in enumerate(nums) if val == 1]
    
    # If there are no 1s, it's impossible to have a subarray with exactly one 1
    if not ones_indices:
        return 0
    
    # If there is only one 1, there is exactly 1 way (the whole array)
    if len(ones_indices) == 1:
        return 1
    
    # The number of ways to split is the product of (number of zeros between consecutive 1s + 1)
    ans = 1
    for i in range(len(ones_indices) - 1):
        # The number of zeros between ones_indices[i] and ones_indices[i+1]
        # is (ones_indices[i+1] - ones_indices[i] - 1)
        # The number of ways to place a split is (zeros + 1)
        gap = ones_indices[i+1] - ones_indices[i]
        ans = (ans * gap) % MOD
        
    return ans
