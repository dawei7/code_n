def solve(nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
    # We need to find i, j such that abs(i - j) >= indexDifference
    # and abs(nums[i] - nums[j]) >= valueDifference.
    # This is equivalent to finding i such that i <= j - indexDifference
    # and (nums[j] - nums[i] >= valueDifference OR nums[i] - nums[j] >= valueDifference).
    
    # Track the index of the minimum and maximum values seen so far
    # that satisfy the indexDifference constraint.
    min_idx = 0
    max_idx = 0
    
    for j in range(indexDifference, len(nums)):
        i = j - indexDifference
        
        # Update the min/max index based on the new valid i
        if nums[i] < nums[min_idx]:
            min_idx = i
        if nums[i] > nums[max_idx]:
            max_idx = i
            
        # Check if the current nums[j] satisfies the condition with the best i found so far
        if abs(nums[j] - nums[min_idx]) >= valueDifference:
            return [min_idx, j]
        if abs(nums[j] - nums[max_idx]) >= valueDifference:
            return [max_idx, j]
            
    return [-1, -1]
