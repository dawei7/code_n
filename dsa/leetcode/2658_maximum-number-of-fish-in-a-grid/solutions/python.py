from collections import deque
from typing import List

def solve(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    max_fish = 0

    # Define directions for neighbors (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(r_start, c_start):
        current_component_fish = 0
        q = deque([(r_start, c_start)])
        visited.add((r_start, c_start))

        while q:
            r, c = q.popleft()
            current_component_fish += grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Check if it's a water cell with fish and not visited
                    if grid[nr][nc] > 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        return current_component_fish

    for r in range(rows):
        for c in range(cols):
            # If it's a water cell with fish and hasn't been visited yet
            if grid[r][c] > 0 and (r, c) not in visited:
                fish_in_component = bfs(r, c)
                max_fish = max(max_fish, fish_in_component)

    return max_fish
