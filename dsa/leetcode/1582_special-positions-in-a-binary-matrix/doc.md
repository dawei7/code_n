# Special Positions in a Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1582 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [special-positions-in-a-binary-matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/special-positions-in-a-binary-matrix/).

### Goal
Count cells containing `1` whose row and column each contain no other `1`.

### Function Contract
**Inputs**

- `mat`: a binary matrix.

**Return value**

The number of special positions.

### Examples
**Example 1**

- Input: `mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]`
- Output: `1`

**Example 2**

- Input: `mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`
- Output: `3`

**Example 3**

- Input: `mat = [[0, 0], [0, 0]]`
- Output: `0`

---

## Solution
### Approach
Precompute the number of ones in each row and each column. Then scan every cell;
cell `(r, c)` is special exactly when `mat[r][c] == 1`, `row_count[r] == 1`,
and `col_count[c] == 1`.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(m + n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(mat):
    if not mat:
        return 0
    rows = len(mat)
    cols = max((len(row) for row in mat), default=0)
    row_count = [0] * rows
    col_count = [0] * cols
    for r, row in enumerate(mat):
        for c, value in enumerate(row):
            if value == 1:
                row_count[r] += 1
                col_count[c] += 1
    total = 0
    for r, row in enumerate(mat):
        for c, value in enumerate(row):
            if value == 1 and row_count[r] == 1 and col_count[c] == 1:
                total += 1
    return total
```
</details>
