# Matrix Diagonal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1572 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [matrix-diagonal-sum](https://leetcode.com/problems/matrix-diagonal-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/matrix-diagonal-sum/).

### Goal
Sum the values on both diagonals of a square matrix, counting the center only
once when the matrix size is odd.

### Function Contract
**Inputs**

- `mat`: an `n x n` integer matrix.

**Return value**

The sum of all primary and secondary diagonal cells.

### Examples
**Example 1**

- Input: `mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `25`

**Example 2**

- Input: `mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]`
- Output: `8`

**Example 3**

- Input: `mat = [[5]]`
- Output: `5`

---

## Solution
### Approach
For each row `i`, add `mat[i][i]` and `mat[i][n - 1 - i]`. If both indices are
the same center cell, add it only once.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(mat):
    n = min(len(mat), len(mat[0]) if mat else 0)
    total = 0
    for i in range(n):
        total += mat[i][i]
        j = n - 1 - i
        if j != i:
            total += mat[i][j]
    return total
```
</details>
