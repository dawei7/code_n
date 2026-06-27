from typing import List

def solve(costs: List[int]) -> int:
    """
    Calculates the minimum cost to reach every position by summing all costs.
    
    Args:
        costs: A list of integers representing the cost at each position.
        
    Returns:
        The total sum of all costs in the array.
    """
    return sum(costs)
