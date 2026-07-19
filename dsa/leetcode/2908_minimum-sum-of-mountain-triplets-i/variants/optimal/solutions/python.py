def solve(nums: list[int]) -> int:
    n = len(nums)
    min_sum = float('inf')
    found = False
    
    # Iterate through all possible triplets (i, j, k)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check the mountain condition: nums[i] < nums[j] and nums[k] < nums[j]
                if nums[i] < nums[j] and nums[k] < nums[j]:
                    current_sum = nums[i] + nums[j] + nums[k]
                    if current_sum < min_sum:
                        min_sum = current_sum
                        found = True
                        
    return int(min_sum) if found else -1
