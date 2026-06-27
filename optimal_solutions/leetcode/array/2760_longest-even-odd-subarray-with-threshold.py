def solve(nums: list[int], threshold: int) -> int:
    max_len = 0
    current_len = 0
    
    for i in range(len(nums)):
        # Check if the current element is valid (<= threshold)
        if nums[i] <= threshold:
            # If we are currently tracking a subarray, check parity alternation
            if current_len > 0 and nums[i] % 2 != nums[i - 1] % 2:
                current_len += 1
            # If we are starting a new subarray, it must begin with an even number
            elif nums[i] % 2 == 0:
                current_len = 1
            else:
                current_len = 0
        else:
            # Element exceeds threshold, reset current tracking
            current_len = 0
            
        max_len = max(max_len, current_len)
        
    return max_len
