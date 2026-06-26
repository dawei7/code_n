def solve(words: list[str], target: str, startIndex: int) -> int:
    n = len(words)
    min_dist = float('inf')
    found = False
    
    for i in range(n):
        if words[i] == target:
            found = True
            # Calculate distance in both directions
            dist = abs(i - startIndex)
            circular_dist = n - dist
            
            # Update min_dist with the smaller of the two paths
            min_dist = min(min_dist, dist, circular_dist)
            
    return int(min_dist) if found else -1
