# Minimum Moves to Reach Target with Rotations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1210 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-moves-to-reach-target-with-rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/).

### Goal
Move a two-cell snake from the top-left horizontal position to the bottom-right horizontal target in a square grid with blocked cells. The snake may move right, move down, or rotate when the surrounding `2 x 2` area is clear.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix where `0` is empty and `1` is blocked.

**Return value**

The minimum number of moves required, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]`
- Output: `11`

**Example 2**

- Input: `grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]`
- Output: `9`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `1`

---

## Solution
### Approach
Breadth-first search over position-and-orientation states.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(grid):
    n = len(grid)
    start = (0, 0, 0)
    target = (n - 1, n - 2, 0)
    queue = deque([(0, 0, 0, 0)])
    seen = {start}

    while queue:
        r, c, orientation, steps = queue.popleft()
        if (r, c, orientation) == target:
            return steps

        if orientation == 0:
            if c + 2 < n and grid[r][c + 2] == 0:
                state = (r, c + 1, 0)
                if state not in seen:
                    seen.add(state)
                    queue.append((r, c + 1, 0, steps + 1))
            if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                for state in ((r + 1, c, 0), (r, c, 1)):
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, steps + 1))
        else:
            if r + 2 < n and grid[r + 2][c] == 0:
                state = (r + 1, c, 1)
                if state not in seen:
                    seen.add(state)
                    queue.append((r + 1, c, 1, steps + 1))
            if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                for state in ((r, c + 1, 1), (r, c, 0)):
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, steps + 1))

    return -1
```
</details>
