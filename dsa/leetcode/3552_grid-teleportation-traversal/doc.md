# Grid Teleportation Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3552 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [grid-teleportation-traversal](https://leetcode.com/problems/grid-teleportation-traversal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/grid-teleportation-traversal/).

### Goal
Given a 2D grid where certain cells contain teleportation portals, determine the minimum number of steps required to travel from a starting coordinate to a target coordinate. A portal at `(r, c)` allows an instantaneous jump to any other cell `(r', c')` that shares the same portal ID. Standard movement is restricted to adjacent cells (up, down, left, right).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where `0` represents an empty path, `-1` represents an obstacle, and positive integers represent portal IDs.
- `start`: A tuple `(r, c)` representing the starting coordinates.
- `target`: A tuple `(r, c)` representing the destination coordinates.

**Return value**

- An integer representing the minimum steps to reach the target, or `-1` if the target is unreachable.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 0], [0, -1, 0], [0, 1, 0]], start = (0, 0), target = (2, 2)`
- Output: `3`

**Example 2**

- Input: `grid = [[0, 0, 0], [0, -1, 0], [0, 0, 0]], start = (0, 0), target = (2, 2)`
- Output: `4`

**Example 3**

- Input: `grid = [[0, 1, 2], [0, -1, 0], [2, 1, 0]], start = (0, 0), target = (2, 2)`
- Output: `2`

---

## Solution
### Approach
Breadth-First Search (BFS) is used to find the shortest path in an unweighted graph. The grid is treated as a graph where nodes are cells and edges exist between adjacent cells or between cells sharing the same portal ID. To optimize, we use a hash map to group portal coordinates by their ID, ensuring we only traverse each portal network once.

### Complexity Analysis
- **Time Complexity**: `O(R * C)`, where `R` is the number of rows and `C` is the number of columns. Each cell is visited at most once, and each portal network is processed once.
- **Space Complexity**: `O(R * C)` to store the visited set and the portal mapping dictionary.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
