from collections import deque, defaultdict

def solve(grid, start, target):
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = start
    target_r, target_c = target
    
    if grid[start_r][start_c] == -1 or grid[target_r][target_c] == -1:
        return -1
    
    # Map portal IDs to list of coordinates
    portals = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                portals[grid[r][c]].append((r, c))
                
    queue = deque([(start_r, start_c, 0)])
    visited = {(start_r, start_c)}
    visited_portals = set()
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == (target_r, target_c):
            return dist
        
        # Standard movement
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
        
        # Portal movement
        portal_id = grid[r][c]
        if portal_id > 0 and portal_id not in visited_portals:
            visited_portals.add(portal_id)
            for pr, pc in portals[portal_id]:
                if (pr, pc) not in visited:
                    visited.add((pr, pc))
                    queue.append((pr, pc, dist + 1))
                    
    return -1
