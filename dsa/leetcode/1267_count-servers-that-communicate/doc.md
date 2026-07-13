# Count Servers that Communicate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1267 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-servers-that-communicate](https://leetcode.com/problems/count-servers-that-communicate/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-servers-that-communicate/).

### Goal
Count servers that can communicate with at least one other server in the same row or column.

### Function Contract
**Inputs**

- `grid`: binary matrix where `1` is a server and `0` is empty.

**Return value**

The number of communicating servers.

### Examples
**Example 1**

- Input: `grid = [[1,0],[0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,0],[1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`
- Output: `4`

---

## Solution
### Approach
Row and column counting.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m + n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    row_counts = [sum(row) for row in grid]
    col_counts = [sum(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
    answer = 0
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value and (row_counts[r] > 1 or col_counts[c] > 1):
                answer += 1
    return answer
```
</details>
