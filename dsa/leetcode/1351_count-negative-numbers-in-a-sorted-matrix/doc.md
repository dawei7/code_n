# Count Negative Numbers in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1351 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-negative-numbers-in-a-sorted-matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/).

### Goal
Count negative values in a matrix where every row and every column is sorted in non-increasing order.

### Function Contract
**Inputs**

- `grid`: sorted integer matrix.

**Return value**

The number of negative entries.

### Examples
**Example 1**

- Input: `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- Output: `8`

**Example 2**

- Input: `grid = [[3,2],[1,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,-1],[-1,-1]]`
- Output: `3`

---

## Solution
### Approach
Staircase scan on a sorted matrix.

### Complexity Analysis
- **Time Complexity**: `O(m + n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    r = rows - 1
    c = 0
    answer = 0
    while r >= 0 and c < cols:
        if grid[r][c] < 0:
            answer += cols - c
            r -= 1
        else:
            c += 1
    return answer
```
</details>
