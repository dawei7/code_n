# Minimum Falling Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1289 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-falling-path-sum-ii](https://leetcode.com/problems/minimum-falling-path-sum-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-falling-path-sum-ii/).

### Goal
Choose one cell from each row of a square grid so that no two adjacent rows choose the same column, minimizing the total sum.

### Function Contract
**Inputs**

- `grid`: an `n x n` integer matrix.

**Return value**

The minimum valid falling path sum.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `13`

**Example 2**

- Input: `grid = [[7]]`
- Output: `7`

**Example 3**

- Input: `grid = [[2,2,1],[1,2,2],[2,1,2]]`
- Output: `3`

---

## Solution
### Approach
Dynamic programming with minimum and second minimum tracking.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    n = len(grid)
    prev = grid[0][:]
    for r in range(1, n):
        first = second = float("inf")
        first_index = -1
        for c, value in enumerate(prev):
            if value < first:
                second = first
                first = value
                first_index = c
            elif value < second:
                second = value
        prev = [grid[r][c] + (second if c == first_index else first) for c in range(n)]
    return min(prev)
```
</details>
