def solve(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0
    
    target_sum = nums[0] + nums[1]
    count = 0
    
    for i in range(0, len(nums), 2):
        if i + 1 < len(nums) and (nums[i] + nums[i + 1] == target_sum):
            count += 1
        else:
            break
            
    return count
