def solve(nums: list[int]) -> int:
    """
    Calculates the number of times an ant returns to the origin (0)
    given a sequence of moves.
    """
    current_position = 0
    return_count = 0
    
    for move in nums:
        current_position += move
        if current_position == 0:
            return_count += 1
            
    return return_count
