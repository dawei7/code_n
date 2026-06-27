def solve(nums: list[int], k: int, dist: int) -> int:
    from sortedcontainers import SortedList
    # We need to pick k-1 elements from nums[1 : dist + 1]
    # The first element nums[0] is always picked.
    # We maintain the smallest k-1 elements in a SortedList.
    
    n = len(nums)
    # Smallest k-1 elements
    left = SortedList()
    # Remaining elements in the current window
    right = SortedList()
    
    left_sum = 0
    
    def add(val):
        nonlocal left_sum
        left.add(val)
        left_sum += val
        if len(left) > k - 1:
            move = left.pop(-1)
            left_sum -= move
            right.add(move)
            
    def remove(val):
        nonlocal left_sum
        if val in left:
            left.remove(val)
            left_sum -= val
            if right:
                move = right.pop(0)
                left.add(move)
                left_sum += move
        else:
            right.remove(val)
            
    # Initialize window [1, dist + 1]
    for i in range(1, dist + 2):
        add(nums[i])
        
    ans = nums[0] + left_sum
    
    # Slide the window
    for i in range(dist + 2, n):
        # Remove element that falls out of window
        remove(nums[i - dist - 1])
        # Add new element
        add(nums[i])
        ans = min(ans, nums[0] + left_sum)
        
    return ans
