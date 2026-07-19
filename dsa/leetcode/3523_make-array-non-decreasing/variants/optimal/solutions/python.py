def solve(nums: list[int]) -> int:
    # The stack stores tuples of (value, rounds_to_be_removed)
    # rounds_to_be_removed is the number of rounds until this element is deleted.
    stack = []
    max_rounds = 0
    
    for x in nums:
        rounds = 0
        # While the current element is smaller than the top of the stack,
        # it will be removed by the element at the top of the stack.
        while stack and stack[-1][0] <= x:
            rounds = max(rounds, stack.pop()[1])
        
        if stack:
            # If the stack is not empty, the current element will be removed
            # in (rounds + 1) steps because it is smaller than the element
            # currently at the top of the stack.
            rounds += 1
        else:
            # If the stack is empty, this element will never be removed.
            rounds = 0
            
        max_rounds = max(max_rounds, rounds)
        stack.append((x, rounds))
        
    return max_rounds
