# As Far from Land as Possible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [as-far-from-land-as-possible](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/as-far-from-land-as-possible/).

### Goal
In a square grid of water (`0`) and land (`1`), find the water cell whose Manhattan distance to the nearest land cell is as large as possible.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix of `0` and `1`.

**Return value**

The maximum distance from a water cell to its nearest land cell, or `-1` if the grid has no water or no land.

### Examples
**Example 1**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `-1`

---

## Solution
### Approach
Multi-source breadth-first search.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)` for the queue in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(grid):
    n = len(grid)
    queue = deque()
    seen = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                queue.append((r, c, 0))
                seen[r][c] = True

    if not queue or len(queue) == n * n:
        return -1

    answer = 0
    while queue:
        r, c, distance = queue.popleft()
        answer = max(answer, distance)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                seen[nr][nc] = True
                queue.append((nr, nc, distance + 1))
    return answer
```
</details>
