def solve(nums: list[int]) -> int:
    # Transform the condition: nums[j] - nums[i] >= j - i
    # nums[j] - j >= nums[i] - i
    # Let b[i] = nums[i] - i. We want to find a subsequence with non-decreasing b[i]
    # that maximizes the sum of nums[i].
    
    n = len(nums)
    b = [nums[i] - i for i in range(n)]
    
    # Coordinate compression for b values
    sorted_b = sorted(list(set(b)))
    rank = {val: i + 1 for i, val in enumerate(sorted_b)}
    
    # Fenwick Tree to store the maximum sum for a given rank
    # bit[i] stores the max sum of a balanced subsequence ending with a value of rank i
    bit = [0] * (len(sorted_b) + 1)
    
    def update(idx, val):
        while idx < len(bit):
            bit[idx] = max(bit[idx], val)
            idx += idx & (-idx)
            
    def query(idx):
        res = 0
        while idx > 0:
            res = max(res, bit[idx])
            idx -= idx & (-idx)
        return res
    
    max_total_sum = float('-inf')
    
    for i in range(n):
        r = rank[b[i]]
        # Current max sum ending at this b[i] is nums[i] + max sum of previous elements with b[j] <= b[i]
        # We only add nums[i] if it improves the sum (or if it's the first element)
        prev_max = query(r)
        current_sum = max(nums[i], prev_max + nums[i])
        
        update(r, current_sum)
        max_total_sum = max(max_total_sum, current_sum)
        
    return max_total_sum
