# Number of Submatrices That Sum to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1074 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-submatrices-that-sum-to-target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/).

### Goal
Count how many non-empty rectangular submatrices have values whose total equals `target`.

### Function Contract
**Inputs**

- `matrix`: an `m x n` integer grid.
- `target`: the required submatrix sum.

**Return value**

The number of rectangular submatrices with sum exactly `target`.

### Examples
**Example 1**

- Input: `matrix = [[0,1,0],[1,1,1],[0,1,0]]`, `target = 0`
- Output: `4`

**Example 2**

- Input: `matrix = [[1,-1],[-1,1]]`, `target = 0`
- Output: `5`

**Example 3**

- Input: `matrix = [[904]]`, `target = 0`
- Output: `0`

---

## Solution
### Approach
2D prefix sums reduced to repeated 1D subarray-sum counting.

### Complexity Analysis
- **Time Complexity**: `O(min(m, n)^2 * max(m, n))`
- **Space Complexity**: `O(max(m, n))`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1074: Number of Submatrices That Sum to Target."""

from collections import Counter


def solve(matrix: list[list[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    answer = 0
    for top in range(rows):
        col_sums = [0] * cols
        for bottom in range(top, rows):
            for c in range(cols):
                col_sums[c] += matrix[bottom][c]
            counts = Counter({0: 1})
            running = 0
            for value in col_sums:
                running += value
                answer += counts[running - target]
                counts[running] += 1
    return answer
```
</details>
