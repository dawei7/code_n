def solve(m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
    # Sort cuts in descending order to apply the greedy strategy
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)
    
    h_idx = 0
    v_idx = 0
    
    # Number of segments currently created
    h_segments = 1
    v_segments = 1
    
    total_cost = 0
    
    # Process cuts until all are used
    while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
        # If the current horizontal cut is more expensive, perform it
        if horizontalCut[h_idx] >= verticalCut[v_idx]:
            total_cost += horizontalCut[h_idx] * v_segments
            h_segments += 1
            h_idx += 1
        else:
            # Otherwise, perform the vertical cut
            total_cost += verticalCut[v_idx] * h_segments
            v_segments += 1
            v_idx += 1
            
    # Add remaining horizontal cuts
    while h_idx < len(horizontalCut):
        total_cost += horizontalCut[h_idx] * v_segments
        h_idx += 1
        
    # Add remaining vertical cuts
    while v_idx < len(verticalCut):
        total_cost += verticalCut[v_idx] * h_segments
        v_idx += 1
        
    return total_cost
