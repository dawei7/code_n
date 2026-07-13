# Escape a Large Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1036 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [escape-a-large-maze](https://leetcode.com/problems/escape-a-large-maze/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/escape-a-large-maze/).

### Goal
On a very large square grid, some cells are blocked. Determine whether it is possible to move from `source` to `target` using four-directional moves without stepping on a blocked cell.

### Function Contract
**Inputs**

- `blocked`: List[List[int]] blocked coordinates
- `source`: List[int] starting coordinate
- `target`: List[int] destination coordinate

**Return value**

bool - whether the target can be reached

### Examples
**Example 1**

- Input: `blocked = [[0, 1], [1, 0]], source = [0, 0], target = [0, 2]`
- Output: `False`

**Example 2**

- Input: `blocked = [], source = [0, 0], target = [999999, 999999]`
- Output: `True`

**Example 3**

- Input: `blocked = [[10, 10], [10, 11]], source = [0, 0], target = [20, 20]`
- Output: `True`

---

## Solution
### Approach
Bounded breadth-first search with enclosure detection.

### Complexity Analysis
- **Time Complexity**: `O(b^2)` where `b` is the number of blocked cells
- **Space Complexity**: `O(b^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1036: Escape a Large Maze."""

from collections import deque


def solve(blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
    blocked_set = {tuple(cell) for cell in blocked}
    limit = len(blocked) * (len(blocked) - 1) // 2
    size = 1_000_000

    def can_escape(start: tuple[int, int], finish: tuple[int, int]) -> bool:
        queue: deque[tuple[int, int]] = deque([start])
        seen = {start}
        while queue and len(seen) <= limit:
            r, c = queue.popleft()
            if (r, c) == finish:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                nxt = (nr, nc)
                if 0 <= nr < size and 0 <= nc < size and nxt not in blocked_set and nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return len(seen) > limit

    src = (source[0], source[1])
    dst = (target[0], target[1])
    return can_escape(src, dst) and can_escape(dst, src)
```
</details>
