def solve(nums: list[int], k: int) -> int:
    if k == 0:
        return 1
    
    n = len(nums)
    min_len = float('inf')
    bit_counts = [0] * 32
    current_or = 0
    left = 0
    
    def update_or(val, delta):
        nonlocal current_or
        for i in range(32):
            if (val >> i) & 1:
                bit_counts[i] += delta
        
        new_or = 0
        for i in range(32):
            if bit_counts[i] > 0:
                new_or |= (1 << i)
        return new_or

    for right in range(n):
        current_or = update_or(nums[right], 1)
        
        while current_or >= k:
            min_len = min(min_len, right - left + 1)
            current_or = update_or(nums[left], -1)
            left += 1
            
    return int(min_len) if min_len != float('inf') else -1
