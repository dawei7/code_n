def solve(m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
    MOD = 10**9 + 7
    
    # Include the boundaries of the field
    h_coords = sorted([1] + hFences + [m])
    v_coords = sorted([1] + vFences + [n])
    
    # Calculate all possible distances between any two horizontal fences
    h_distances = set()
    for i in range(len(h_coords)):
        for j in range(i + 1, len(h_coords)):
            h_distances.add(h_coords[j] - h_coords[i])
            
    # Calculate all possible distances between any two vertical fences
    # and check if they exist in the horizontal distances set
    max_side = -1
    for i in range(len(v_coords)):
        for j in range(i + 1, len(v_coords)):
            dist = v_coords[j] - v_coords[i]
            if dist in h_distances:
                if dist > max_side:
                    max_side = dist
                    
    if max_side == -1:
        return -1
    
    return (max_side * max_side) % MOD
