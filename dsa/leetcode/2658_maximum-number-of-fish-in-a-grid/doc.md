# Maximum Number of Fish in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2658 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-fish-in-a-grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/).

### Goal
Given a 2D grid representing a map, where each cell `grid[r][c]` contains an integer. A value of `0` indicates a land cell, while any positive integer `x` indicates a water cell containing `x` fish. Fish can only be caught from water cells. Two water cells are considered connected if they are horizontally or vertically adjacent. The objective is to find the maximum total number of fish that can be collected from any single connected component of water cells. If no fish are present in the grid, the result should be 0.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` - A 2D list of integers representing the map. `grid[r][c]` is the number of fish in cell `(r, c)`, or 0 if it's land.
  - `1 <= grid.length, grid[i].length <= 100`
  - `0 <= grid[i][j] <= 100`

**Return value**

- `int` - The maximum total number of fish found in any single connected component of water cells.

### Examples
**Example 1**

- Input: `[[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]`
- Output: `7`
  - Explanation: There are several connected components of fish.
    - (0,1)=2, (0,2)=1 -> Sum = 3
    - (1,0)=4 -> Sum = 4
    - (1,3)=3, (2,3)=4 -> Sum = 7 (This is the maximum)
    - (2,0)=1 -> Sum = 1
    - (3,1)=3, (3,2)=2 -> Sum = 5

**Example 2**

- Input: `[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]`
- Output: `16`
  - Explanation: All cells are water cells with 1 fish, forming one large connected component. The total fish is 4 * 4 * 1 = 16.

**Example 3**

- Input: `[[0,0,0],[0,0,0],[0,0,0]]`
- Output: `0`
  - Explanation: The grid contains only land cells (0 fish), so no fish can be caught.

---

## Solution
### Approach
The problem can be solved using graph traversal algorithms to identify and sum values within connected components.
1.  **Depth-First Search (DFS):** Iterate through each cell of the grid. If a cell contains fish and has not been visited, initiate a DFS traversal from that cell. The DFS will explore all connected water cells, summing their fish counts, and marking them as visited. The sum for each component is then compared to a running maximum.
2.  **Breadth-First Search (BFS):** Similar to DFS, iterate through the grid. When an unvisited water cell is found, start a BFS. The BFS will use a queue to explore all connected water cells level by level, summing their fish counts, and marking them as visited. The sum for each component is then compared to a running maximum.

Both DFS and BFS are suitable for this problem. DFS is often simpler to implement recursively, while BFS is iterative and can be preferred to avoid deep recursion limits.

### Complexity Analysis
- **Time Complexity**: `O(M * N)`
  - Where `M` is the number of rows and `N` is the number of columns in the grid.
  - Each cell in the grid is visited at most a constant number of times (once by the outer loop, and once by the DFS/BFS traversal). Marking cells as visited prevents redundant processing.
- **Space Complexity**: `O(M * N)`
  - This is primarily due to the `visited` set (or 2D array) which stores the state for each cell.
  - In the case of DFS, the recursion stack can go up to `O(M * N)` in the worst-case scenario (e.g., a grid entirely filled with water, forming a single long path).
  - In the case of BFS, the queue can hold up to `O(M * N)` elements in the worst-case (e.g., a grid entirely filled with water, where all cells are added to the queue before being processed).

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
