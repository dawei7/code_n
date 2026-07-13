# Count Square Submatrices with All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1277 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-square-submatrices-with-all-ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-square-submatrices-with-all-ones/).

### Goal
Count every square submatrix whose cells are all `1`.

### Function Contract
**Inputs**

- `matrix`: binary matrix.

**Return value**

The number of all-ones square submatrices.

### Examples
**Example 1**

- Input: `matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]`
- Output: `15`

**Example 2**

- Input: `matrix = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `7`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`

---

## Solution
### Approach
Dynamic programming on square side lengths.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(1)` extra if the input matrix may be updated in place.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    total = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] and r and c:
                matrix[r][c] = 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
            total += matrix[r][c]
    return total
```
</details>
