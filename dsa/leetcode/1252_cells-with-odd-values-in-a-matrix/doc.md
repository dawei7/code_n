# Cells with Odd Values in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1252 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [cells-with-odd-values-in-a-matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/).

### Goal
Start with an `m x n` zero matrix. For each index pair, increment every cell in that row and every cell in that column. Count cells with odd final values.

### Function Contract
**Inputs**

- `m`: number of rows.
- `n`: number of columns.
- `indices`: list of `[row, col]` operations.

**Return value**

The number of cells whose final value is odd.

### Examples
**Example 1**

- Input: `m = 2`, `n = 3`, `indices = [[0,1],[1,1]]`
- Output: `6`

**Example 2**

- Input: `m = 2`, `n = 2`, `indices = [[1,1],[0,0]]`
- Output: `0`

**Example 3**

- Input: `m = 1`, `n = 1`, `indices = [[0,0]]`
- Output: `0`

---

## Solution
### Approach
Parity counting.

### Complexity Analysis
- **Time Complexity**: `O(m + n + len(indices))`
- **Space Complexity**: `O(m + n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(m, n, indices):
    rows = [0] * m
    cols = [0] * n
    for r, c in indices:
        rows[r] ^= 1
        cols[c] ^= 1
    odd_rows = sum(rows)
    odd_cols = sum(cols)
    return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
```
</details>
