# Matrix Block Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1314 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [matrix-block-sum](https://leetcode.com/problems/matrix-block-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/matrix-block-sum/).

### Goal
For every cell, compute the sum of all matrix values within `k` rows and `k` columns of that cell, clipped to the matrix boundaries.

### Function Contract
**Inputs**

- `mat`: integer matrix.
- `k`: block radius.

**Return value**

A matrix of block sums with the same shape as `mat`.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[12,21,16],[27,45,33],[24,39,28]]`

**Example 2**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 2`
- Output: `[[45,45,45],[45,45,45],[45,45,45]]`

**Example 3**

- Input: `mat = [[5]]`, `k = 3`
- Output: `[[5]]`

---

## Solution
### Approach
2D prefix sums.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(mat, k):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]

    answer = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        r1 = max(0, r - k)
        r2 = min(rows, r + k + 1)
        for c in range(cols):
            c1 = max(0, c - k)
            c2 = min(cols, c + k + 1)
            answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
    return answer
```
</details>
