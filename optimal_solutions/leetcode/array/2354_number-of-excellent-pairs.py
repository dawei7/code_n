def solve(nums: list[int], k: int) -> int:
    # Deduplicate the input array to get unique numbers
    unique_nums = set(nums)
    
    # Count frequencies of each popcount (number of set bits)
    # Since nums[i] <= 10^9, the maximum number of set bits is 30.
    count = [0] * 31
    for x in unique_nums:
        count[bin(x).count('1')] += 1
        
    ans = 0
    # Iterate over all possible pairs of popcounts
    for i in range(31):
        for j in range(31):
            if i + j >= k:
                ans += count[i] * count[j]
                
    return ans
