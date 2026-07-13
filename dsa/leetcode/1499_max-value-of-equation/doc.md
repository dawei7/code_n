# Max Value of Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1499 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [max-value-of-equation](https://leetcode.com/problems/max-value-of-equation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/max-value-of-equation/).

### Goal
Given points sorted by increasing `x`, choose two points `i < j` with
`xj - xi <= k` and maximize `yi + yj + |xi - xj|`.

### Function Contract
**Inputs**

- `points`: a list of `[x, y]` coordinates sorted by `x`.
- `k`: the maximum allowed horizontal distance.

**Return value**

The largest equation value among valid pairs.

### Examples
**Example 1**

- Input: `points = [[1, 3], [2, 0], [5, 10], [6, -10]], k = 1`
- Output: `4`

**Example 2**

- Input: `points = [[0, 0], [3, 0], [9, 2]], k = 3`
- Output: `3`

**Example 3**

- Input: `points = [[1, 1], [2, 2], [3, 3]], k = 2`
- Output: `6`

---

## Solution
### Approach
Because `xj >= xi`, the expression becomes `yj + xj + (yi - xi)`. Sweep points
from left to right and keep a monotonic deque of previous candidates ordered by
their `yi - xi` value. Remove candidates that are more than `k` away, use the
front as the best partner for the current point, then insert the current point
while preserving decreasing candidate value.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(points, k):
    normalized = []
    for index, point in enumerate(points):
        if isinstance(point, list) and len(point) >= 2:
            normalized.append((point[0], point[1]))
        else:
            normalized.append((index, point))
    normalized.sort()
    queue = deque()
    best = -10**18
    for x, y in normalized:
        while queue and x - queue[0][1] > k:
            queue.popleft()
        if queue:
            best = max(best, x + y + queue[0][0])
        value = y - x
        while queue and queue[-1][0] <= value:
            queue.pop()
        queue.append((value, x))
    return 0 if best == -10**18 else best
```
</details>
