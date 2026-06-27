def solve(nums: list[int], target: int) -> int:
    total_sum = sum(nums)
    n = len(nums)
    
    # Calculate how many full cycles of the array are needed
    num_cycles = target // total_sum
    remainder = target % total_sum
    
    # If remainder is 0, we only need full cycles
    if remainder == 0:
        return num_cycles * n
    
    # Find the shortest subarray in nums + nums that sums to 'remainder'
    # We use nums + nums to handle subarrays that wrap around the end
    extended_nums = nums + nums
    prefix_map = {0: -1}
    current_sum = 0
    min_len = float('inf')
    
    for i, val in enumerate(extended_nums):
        current_sum += val
        needed = current_sum - remainder
        
        if needed in prefix_map:
            min_len = min(min_len, i - prefix_map[needed])
            
        prefix_map[current_sum] = i
        
    if min_len == float('inf'):
        return -1
    
    return num_cycles * n + min_len
