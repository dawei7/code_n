def solve(nums: list[int]) -> int:
    """
    Greedily removes adjacent pairs that violate the non-decreasing order.
    """
    if not nums:
        return 0
    
    removals = 0
    i = 0
    # We use a list to simulate the array after removals
    stack = []
    
    for x in nums:
        stack.append(x)
        # Check if the last two elements violate the non-decreasing order
        if len(stack) >= 2 and stack[-2] > stack[-1]:
            # Remove the pair
            stack.pop()
            stack.pop()
            removals += 1
            
    return removals
