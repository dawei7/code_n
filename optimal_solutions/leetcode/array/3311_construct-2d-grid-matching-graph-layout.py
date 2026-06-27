from collections import defaultdict, deque

def solve(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    degree = {i: len(adj[i]) for i in range(n)}
    
    # Find potential width by looking at a corner (degree 2)
    # A corner node has degree 2. Its neighbors have degrees 3 and 3 (or 2 and 3).
    # The distance to the next corner along the edge gives the width.
    nodes_by_degree = defaultdict(list)
    for i in range(n):
        nodes_by_degree[degree[i]].append(i)
        
    # Start from a corner
    start_node = nodes_by_degree[2][0]
    
    # Determine width: traverse from start_node along one of its neighbors
    # until we hit another node with degree < 4 (an edge or corner)
    curr = start_node
    width = 1
    next_node = adj[curr][0]
    while len(adj[next_node]) > 2:
        width += 1
        # Move to the next node in the row
        for neighbor in adj[next_node]:
            if neighbor != curr and len(adj[neighbor]) >= 2:
                # Pick the neighbor that isn't the one we came from
                # In a grid, we want to keep moving in the same direction
                if len(adj[neighbor]) < 4:
                    width += 1
                    curr, next_node = next_node, neighbor
                    break
                curr, next_node = next_node, neighbor
                break
    
    # If width is 1, it's a single column
    if width == 1:
        # Just sort by connectivity
        res = [[start_node]]
        visited = {start_node}
        while len(visited) < n:
            for neighbor in adj[res[-1][0]]:
                if neighbor not in visited:
                    res.append([neighbor])
                    visited.add(neighbor)
                    break
        return res

    # Build the grid row by row
    grid = [[0] * width for _ in range(n // width)]
    grid[0][0] = start_node
    visited = {start_node}
    
    # Fill first row
    for j in range(1, width):
        for neighbor in adj[grid[0][j-1]]:
            if neighbor not in visited:
                grid[0][j] = neighbor
                visited.add(neighbor)
                break
                
    # Fill remaining rows
    for i in range(1, n // width):
        for j in range(width):
            if j == 0:
                # Find node below grid[i-1][0]
                for neighbor in adj[grid[i-1][0]]:
                    if neighbor not in visited:
                        grid[i][0] = neighbor
                        visited.add(neighbor)
                        break
            else:
                # Find node below grid[i-1][j] OR right of grid[i][j-1]
                candidates = set(adj[grid[i-1][j]]) & set(adj[grid[i][j-1]])
                for cand in candidates:
                    if cand not in visited:
                        grid[i][j] = cand
                        visited.add(cand)
                        break
    return grid
