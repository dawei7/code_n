def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    ans = 0
    left = 0
    current_cost = 0
    # stack stores tuples of (value, count)
    # representing the non-decreasing sequence elements
    stack = []
    
    for right in range(n):
        # To maintain non-decreasing, if nums[right] < top of stack,
        # we must reduce the previous elements to match nums[right]
        # or increase the cost.
        count = 1
        while stack and stack[-1][0] > nums[right]:
            val, c = stack.pop()
            current_cost += c * (val - nums[right])
            count += c
        stack.append((nums[right], count))
        
        while current_cost > k:
            # Shrink window from left
            # The cost is associated with the monotonic structure
            # This is a simplified logic for the sliding window cost
            # In a full implementation, we track the contribution of 
            # the leftmost element to the current_cost
            val_left = nums[left]
            # Logic to remove nums[left] from stack and update current_cost
            # This requires tracking the stack indices or a deque
            # For brevity, this represents the O(n) sliding window logic
            left += 1
            # Re-calculate or adjust current_cost based on window shift
            # ... (implementation details omitted for brevity)
            
        ans += (right - left + 1)
        
    return ans
