from typing import List

def solve(m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    """
    Calculates the minimum cost to cut an m x n cake into 1x1 squares.
    Uses a greedy approach: always perform the most expensive cut available.
    """
    # Sort cuts in descending order to prioritize expensive cuts
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)
    
    h_idx = 0
    v_idx = 0
    
    # Number of pieces currently in each dimension
    h_pieces = 1
    v_pieces = 1
    
    total_cost = 0
    
    # Process all cuts
    while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
        if horizontalCut[h_idx] >= verticalCut[v_idx]:
            # Perform horizontal cut
            total_cost += horizontalCut[h_idx] * v_pieces
            h_pieces += 1
            h_idx += 1
        else:
            # Perform vertical cut
            total_cost += verticalCut[v_idx] * h_pieces
            v_pieces += 1
            v_idx += 1
            
    # Add remaining horizontal cuts
    while h_idx < len(horizontalCut):
        total_cost += horizontalCut[h_idx] * v_pieces
        h_idx += 1
        
    # Add remaining vertical cuts
    while v_idx < len(verticalCut):
        total_cost += verticalCut[v_idx] * h_pieces
        v_idx += 1
        
    return total_cost
