def solve(nums: list[int], x: int) -> int:
    # Initialize DP states with a very small number to represent unreachable states.
    # even_max: max score ending in an even number
    # odd_max: max score ending in an odd number
    even_max = float('-inf')
    odd_max = float('-inf')
    
    # Base case: the first element
    if nums[0] % 2 == 0:
        even_max = nums[0]
    else:
        odd_max = nums[0]
        
    for i in range(1, len(nums)):
        val = nums[i]
        if val % 2 == 0:
            # Current is even:
            # 1. Stay even: even_max + val
            # 2. Switch from odd: odd_max + val - x
            even_max = max(even_max + val, odd_max + val - x)
        else:
            # Current is odd:
            # 1. Stay odd: odd_max + val
            # 2. Switch from even: even_max + val - x
            odd_max = max(odd_max + val, even_max + val - x)
            
    return max(even_max, odd_max)
