# Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1284 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/).

### Goal
Each move chooses one cell and toggles that cell plus its four orthogonal neighbors if present. Find the fewest moves needed to turn the whole binary matrix into zeroes.

### Function Contract
**Inputs**

- `mat`: an `m x n` binary matrix.

**Return value**

The minimum number of flips required, or `-1` if the zero matrix is unreachable.

### Examples
**Example 1**

- Input: `mat = [[0,0],[0,1]]`
- Output: `3`

**Example 2**

- Input: `mat = [[0]]`
- Output: `0`

**Example 3**

- Input: `mat = [[1,1,1],[1,0,1],[0,0,0]]`
- Output: `6`

---

## Solution
### Approach
Bitmask state encoding and breadth-first search.

### Complexity Analysis
- **Time Complexity**: `O(m * n * 2^(m*n))`
- **Space Complexity**: `O(2^(m*n))`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(mat):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    start = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c]:
                start |= 1 << (r * cols + c)
    if start == 0:
        return 0

    flips = []
    for r in range(rows):
        for c in range(cols):
            mask = 0
            for dr, dc in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    mask ^= 1 << (nr * cols + nc)
            flips.append(mask)

    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        mask, steps = queue.popleft()
        for flip in flips:
            nxt = mask ^ flip
            if nxt == 0:
                return steps + 1
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))
    return -1
```
</details>
