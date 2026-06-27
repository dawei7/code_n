def solve(X: int, Y: int, circles: list[list[int]]) -> bool:
    n = len(circles)
    parent = list(range(n + 2))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # n: left/top boundary (x=0 or y=Y)
    # n+1: right/bottom boundary (x=X or y=0)
    for i in range(n):
        x, y, r = circles[i]
        
        # Check intersection with left (x=0) or top (y=Y)
        if x <= r or abs(y - Y) <= r:
            union(i, n)
        
        # Check intersection with right (x=X) or bottom (y=0)
        if abs(x - X) <= r or y <= r:
            union(i, n + 1)
            
        # Check intersection between circles
        for j in range(i + 1, n):
            x2, y2, r2 = circles[j]
            dist_sq = (x - x2)**2 + (y - y2)**2
            if dist_sq <= (r + r2)**2:
                union(i, j)
                
    # If the two boundaries are connected, the path is blocked
    if find(n) == find(n + 1):
        return False
        
    # Check if the start or end points are inside any circle
    for x, y, r in circles:
        if x**2 + y**2 <= r**2:
            return False
        if (x - X)**2 + (y - Y)**2 <= r**2:
            return False
            
    return True
