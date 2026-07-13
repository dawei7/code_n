from typing import List

def solve(nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
    # Use a set to track positions containing marbles.
    # Since we only care if a position is occupied, a set is sufficient.
    positions = set(nums)
    
    # Process each move operation
    for start, end in zip(moveFrom, moveTo):
        # If the source position has marbles, move them to the target.
        # Note: The problem implies all marbles at 'start' move to 'end'.
        if start in positions:
            positions.remove(start)
            positions.add(end)
            
    # Return the final positions sorted in ascending order
    return sorted(list(positions))
