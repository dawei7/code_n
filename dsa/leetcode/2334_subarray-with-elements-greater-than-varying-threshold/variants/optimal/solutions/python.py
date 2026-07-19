def solve(nums: list[int], threshold: int) -> int:
    n = len(nums)
    
    # left_smaller[i] stores the index of the first element to the left of i
    # that is strictly smaller than nums[i]. If no such element, it's -1.
    left_smaller = [-1] * n
    stack = [] # Stores indices
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_smaller[i] = stack[-1]
        stack.append(i)
    
    # right_smaller[i] stores the index of the first element to the right of i
    # that is strictly smaller than nums[i]. If no such element, it's n.
    right_smaller = [n] * n
    stack = [] # Clear and reuse stack
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_smaller[i] = stack[-1]
        stack.append(i)
        
    # For each nums[i], consider it as the minimum element of a subarray.
    # The largest such subarray where nums[i] is the minimum spans from
    # (left_smaller[i] + 1) to (right_smaller[i] - 1).
    # The length of this subarray is (right_smaller[i] - 1) - (left_smaller[i] + 1) + 1
    # = right_smaller[i] - left_smaller[i] - 1.
    
    for i in range(n):
        length = right_smaller[i] - left_smaller[i] - 1
        
        # The problem condition is: min_element_in_subarray > threshold / length_of_subarray
        # If nums[i] is the minimum element in a subarray of 'length',
        # then the condition becomes nums[i] > threshold / length.
        # To avoid float division and potential precision issues, we rewrite it as:
        # nums[i] * length > threshold
        # Note: If length is 0, nums[i] * 0 = 0, and 0 > threshold is false (assuming threshold >= 0).
        # This correctly handles cases where a single element cannot form a valid subarray.
        if nums[i] * length > threshold:
            return length
            
    return -1
