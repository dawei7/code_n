from typing import List

def solve(reward1: List[int], reward2: List[int], k: int) -> int:
    """
    Calculates the maximum total points by greedily selecting the k pieces
    that provide the highest relative advantage for the first mouse.
    """
    n = len(reward1)
    
    # Calculate the net gain of choosing mouse 1 over mouse 2 for each piece
    gains = []
    for i in range(n):
        gains.append(reward1[i] - reward2[i])
    
    # Sort gains in descending order to pick the best k pieces for mouse 1
    gains.sort(reverse=True)
    
    # Start with the assumption that mouse 2 eats everything
    total_points = sum(reward2)
    
    # Add the top k gains to the base sum
    for i in range(k):
        total_points += gains[i]
        
    return total_points
