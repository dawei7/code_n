# Grid Illumination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1001 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [grid-illumination](https://leetcode.com/problems/grid-illumination/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/grid-illumination/).

### Goal
On an `n x n` grid, lamps illuminate their row, column, and both diagonals. For each query cell, report whether it is illuminated, then switch off any lamps in that cell or its eight neighboring cells.

### Function Contract
**Inputs**

- `n`: int grid size
- `lamps`: List[List[int]] lamp coordinates
- `queries`: List[List[int]] queried coordinates

**Return value**

List[int] - `1` for illuminated query cells, otherwise `0`

### Examples
**Example 1**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 0]]`
- Output: `[1, 0]`

**Example 2**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 1]]`
- Output: `[1, 1]`

**Example 3**

- Input: `n = 3, lamps = [[0, 0], [1, 1]], queries = [[1, 1], [2, 2]]`
- Output: `[1, 0]`

---

## Solution
### Approach
Hash maps for row, column, and diagonal illumination counts.

### Complexity Analysis
- **Time Complexity**: `O(l + q)` for `l` lamps and `q` queries
- **Space Complexity**: `O(l)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1001: Grid Illumination."""

from collections import Counter


def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    active = set()
    rows: Counter[int] = Counter()
    cols: Counter[int] = Counter()
    diag: Counter[int] = Counter()
    anti: Counter[int] = Counter()

    for r, c in lamps:
        if (r, c) in active:
            continue
        active.add((r, c))
        rows[r] += 1
        cols[c] += 1
        diag[r - c] += 1
        anti[r + c] += 1

    answer: list[int] = []
    for r, c in queries:
        answer.append(1 if rows[r] or cols[c] or diag[r - c] or anti[r + c] else 0)
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) not in active:
                    continue
                active.remove((nr, nc))
                rows[nr] -= 1
                cols[nc] -= 1
                diag[nr - nc] -= 1
                anti[nr + nc] -= 1
    return answer
```
</details>
