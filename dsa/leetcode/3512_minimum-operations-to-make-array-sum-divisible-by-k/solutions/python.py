def solve(nums: list[int], k: int) -> int:
    total_sum = sum(nums)
    target = total_sum % k
    
    if target == 0:
        return 0
    
    # We want to find the longest subarray with sum % k == target
    # Let prefix_sum[j] % k = p_j and prefix_sum[i] % k = p_i
    # We need (p_j - p_i) % k == target
    # p_i = (p_j - target) % k
    
    prefix_map = {0: -1}
    current_sum = 0
    max_len = -1
    
    for i, num in enumerate(nums):
        current_sum = (current_sum + num) % k
        
        needed = (current_sum - target + k) % k
        if needed in prefix_map:
            max_len = max(max_len, i - prefix_map[needed])
        
        prefix_map[current_sum] = i
        
    return len(nums) - max_len if max_len != -1 else -1
