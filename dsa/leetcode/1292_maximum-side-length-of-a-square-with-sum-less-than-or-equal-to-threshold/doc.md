# Maximum Side Length of a Square with Sum Less than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1292 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/).

### Goal
Find the largest side length of a square submatrix whose sum is at most `threshold`.

### Function Contract
**Inputs**

- `mat`: integer matrix.
- `threshold`: maximum allowed square sum.

**Return value**

The maximum valid square side length.

### Examples
**Example 1**

- Input: `mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]`, `threshold = 4`
- Output: `2`

**Example 2**

- Input: `mat = [[2,2],[2,2]]`, `threshold = 1`
- Output: `0`

**Example 3**

- Input: `mat = [[1,0,1],[0,1,0],[1,0,1]]`, `threshold = 2`
- Output: `2`

---

## Solution
### Approach
2D prefix sums and incremental side-length testing.

### Complexity Analysis
- **Time Complexity**: `O(m * n * min(m, n))` in the straightforward scan.
- **Space Complexity**: `O(m * n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(mat, threshold):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]

    def square_sum(r, c, side):
        return prefix[r + side][c + side] - prefix[r][c + side] - prefix[r + side][c] + prefix[r][c]

    best = 0
    for r in range(rows):
        for c in range(cols):
            while r + best < rows and c + best < cols and square_sum(r, c, best + 1) <= threshold:
                best += 1
    return best
```
</details>
