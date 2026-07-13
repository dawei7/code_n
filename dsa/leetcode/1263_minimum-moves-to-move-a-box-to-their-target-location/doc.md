# Minimum Moves to Move a Box to Their Target Location

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1263 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-moves-to-move-a-box-to-their-target-location](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/).

### Goal
In a grid with walls, one player, one box, and one target, find the minimum number of box pushes needed to move the box onto the target.

### Function Contract
**Inputs**

- `grid`: matrix containing walls `#`, empty cells `.`, player `S`, box `B`, and target `T`.

**Return value**

The fewest pushes required, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `3`

**Example 2**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#","#","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `-1`

**Example 3**

- Input: `grid = [["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `5`

---

## Solution
### Approach
Breadth-first search over box/player states with reachability checks.

### Complexity Analysis
- **Time Complexity**: `O((m * n)^2)` in the straightforward BFS with player reachability searches.
- **Space Complexity**: `O((m * n)^2)` for visited box/player states.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    box = player = target = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "B":
                box = (r, c)
            elif grid[r][c] == "S":
                player = (r, c)
            elif grid[r][c] == "T":
                target = (r, c)

    def free(cell, blocked_box):
        r, c = cell
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and cell != blocked_box

    def can_reach(start, goal, blocked_box):
        queue = deque([start])
        seen = {start}
        while queue:
            cell = queue.popleft()
            if cell == goal:
                return True
            r, c = cell
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt = (r + dr, c + dc)
                if nxt not in seen and free(nxt, blocked_box):
                    seen.add(nxt)
                    queue.append(nxt)
        return False

    queue = deque([(box, player, 0)])
    seen = {(box, player)}
    while queue:
        current_box, current_player, pushes = queue.popleft()
        if current_box == target:
            return pushes
        br, bc = current_box
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            stand = (br - dr, bc - dc)
            next_box = (br + dr, bc + dc)
            if not free(next_box, current_box) or not free(stand, current_box):
                continue
            if not can_reach(current_player, stand, current_box):
                continue
            state = (next_box, current_box)
            if state not in seen:
                seen.add(state)
                queue.append((next_box, current_box, pushes + 1))
    return -1
```
</details>
