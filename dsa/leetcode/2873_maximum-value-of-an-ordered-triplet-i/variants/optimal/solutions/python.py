def solve(nums: list[int]) -> int:
    n = len(nums)
    max_val = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_val = (nums[i] - nums[j]) * nums[k]
                if current_val > max_val:
                    max_val = current_val
                    
    return max_val
