def solve(nums: list[int]) -> int:
    max_xor = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i, n):
            x = nums[i]
            y = nums[j]
            
            # Check the strong pair condition: |x - y| <= min(x, y)
            if abs(x - y) <= min(x, y):
                current_xor = x ^ y
                if current_xor > max_xor:
                    max_xor = current_xor
                    
    return max_xor
