def solve(points: list[list[int]]) -> int:
    # Transform coordinates: u = x + y, v = x - y
    # Manhattan distance = max(|u1 - u2|, |v1 - v2|)
    transformed = []
    for x, y in points:
        transformed.append((x + y, x - y))
    
    def get_max_dist(indices_to_skip):
        min_u, max_u = float('inf'), float('-inf')
        min_v, max_v = float('inf'), float('-inf')
        
        for i in range(len(transformed)):
            if i in indices_to_skip:
                continue
            u, v = transformed[i]
            min_u, max_u = min(min_u, u), max(max_u, u)
            min_v, max_v = min(min_v, v), max(max_v, v)
            
        return max(max_u - min_u, max_v - min_v)

    # The maximum distance is determined by the points with min/max u or v.
    # We only need to check removing these specific points.
    candidates = set()
    for i in range(len(transformed)):
        u, v = transformed[i]
        # Check if this point is an extreme
        # We collect indices of points that define the current max distance
        pass

    # Find indices of points that result in min_u, max_u, min_v, max_v
    u_vals = [t[0] for t in transformed]
    v_vals = [t[1] for t in transformed]
    
    idx_min_u = u_vals.index(min(u_vals))
    idx_max_u = u_vals.index(max(u_vals))
    idx_min_v = v_vals.index(min(v_vals))
    idx_max_v = v_vals.index(max(v_vals))
    
    to_check = {idx_min_u, idx_max_u, idx_min_v, idx_max_v}
    
    ans = float('inf')
    for i in to_check:
        ans = min(ans, get_max_dist({i}))
        
    return ans
