def solve(distance: list[int]) -> bool:
    n = len(distance)
    if n <= 3:
        return False
    
    for i in range(3, n):
        # Case 1: Fourth line crosses first line (Spiral Inward)
        if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
            return True
        
        # Case 2: Fifth line meets first line (Bounded Spiral)
        if i >= 4:
            if distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
        
        # Case 3: Sixth line crosses first line (Spiral Outward to Inward)
        if i >= 5:
            if (distance[i - 1] <= distance[i - 3] and 
                distance[i - 1] + distance[i - 5] >= distance[i - 3] and
                distance[i - 2] > distance[i - 4] and
                distance[i] + distance[i - 4] >= distance[i - 2]):
                return True
                
    return False
