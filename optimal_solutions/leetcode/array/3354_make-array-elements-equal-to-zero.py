def solve(nums: list[int]) -> int:
    total_sum = sum(nums)
    current_prefix_sum = 0
    valid_starts = 0
    
    for i, val in enumerate(nums):
        if val == 0:
            # If current element is 0, we can potentially start here.
            # The condition for success is that the sum of elements to the left
            # must equal the sum of elements to the right.
            left_sum = current_prefix_sum
            right_sum = total_sum - current_prefix_sum
            if left_sum == right_sum:
                valid_starts += 1
        else:
            # If current element is non-zero, we can potentially start here.
            # The condition is that the sums must differ by exactly 1.
            left_sum = current_prefix_sum
            right_sum = total_sum - current_prefix_sum - val
            if abs(left_sum - right_sum) == 1:
                valid_starts += 1
        
        current_prefix_sum += val
        
    return valid_starts
