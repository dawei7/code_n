def solve(nums: list[int], k: int) -> int:
    if not nums:
        return 0
    
    max_val = max(nums)
    n = len(nums)
    count = 0
    ans = 0
    left = 0
    
    for right in range(n):
        if nums[right] == max_val:
            count += 1
        
        while count >= k:
            # If the current window [left, right] has k max elements,
            # then all subarrays starting at 'left' and ending at 
            # any index from 'right' to 'n-1' are valid.
            # There are (n - right) such subarrays.
            ans += (n - right)
            
            if nums[left] == max_val:
                count -= 1
            left += 1
            
    return ans
