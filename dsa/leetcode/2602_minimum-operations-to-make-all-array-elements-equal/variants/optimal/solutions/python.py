import bisect

def solve(nums, queries):
    nums.sort()
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    results = []
    for q in queries:
        # Find index where elements are >= q
        idx = bisect.bisect_left(nums, q)
        
        # Elements smaller than q: nums[0...idx-1]
        # Count: idx
        # Sum: prefix_sum[idx]
        # Cost: (q * idx) - prefix_sum[idx]
        left_cost = (q * idx) - prefix_sum[idx]
        
        # Elements greater than or equal to q: nums[idx...n-1]
        # Count: n - idx
        # Sum: prefix_sum[n] - prefix_sum[idx]
        # Cost: (prefix_sum[n] - prefix_sum[idx]) - (q * (n - idx))
        right_cost = (prefix_sum[n] - prefix_sum[idx]) - (q * (n - idx))
        
        results.append(left_cost + right_cost)
        
    return results
