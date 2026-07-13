def solve(colors: list[int]) -> int:
    n = len(colors)
    if n < 3:
        return 0
    
    count = 0
    # Iterate through each index, treating it as the center of a triplet.
    # Due to circularity, the neighbors of index i are (i-1)%n and (i+1)%n.
    for i in range(n):
        left = colors[(i - 1) % n]
        mid = colors[i]
        right = colors[(i + 1) % n]
        
        # Check if the middle element is different from both neighbors
        if mid != left and mid != right:
            count += 1
            
    return count
