# Count Submatrices with Top-Left Element and Sum Less Than k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3070 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-submatrices-with-top-left-element-and-sum-less-than-k](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/).

### Goal
Given a 2D grid of non-negative integers and an integer `k`, determine the total number of submatrices that start at the top-left corner (0, 0) and have a total sum of elements strictly less than `k`.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the 2D matrix.
- `k`: An integer representing the threshold sum.

**Return value**

- An integer representing the count of submatrices starting at (0, 0) with a sum less than `k`.

### Examples
**Example 1**

- Input: `grid = [[7,6,3],[6,6,1]], k = 18`
- Output: `4`

**Example 2**

- Input: `grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20`
- Output: `6`

---

## Solution
### Approach
The problem is solved using 2D Prefix Sums. By precomputing a prefix sum matrix where each cell `(i, j)` stores the sum of the rectangle from `(0, 0)` to `(i, j)`, we can determine the sum of any submatrix starting at `(0, 0)` in constant time. The algorithm iterates through every cell in the grid, calculates the prefix sum, and increments a counter if the sum is less than `k`.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we traverse the grid once to compute prefix sums.
- **Space Complexity**: `O(m * n)` to store the prefix sum matrix (or `O(1)` if modifying the input grid in-place).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]], k: int) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Create a 2D prefix sum array
    # prefix_sum[i][j] will store the sum of the submatrix from (0,0) to (i,j)
    prefix_sum = [[0] * cols for _ in range(rows)]
    count = 0

    for r in range(rows):
        row_running_sum = 0
        for c in range(cols):
            row_running_sum += grid[r][c]

            # The sum of the submatrix (0,0) to (r,c) is:
            # current row's running sum + the prefix sum of the row above
            if r == 0:
                prefix_sum[r][c] = row_running_sum
            else:
                prefix_sum[r][c] = row_running_sum + prefix_sum[r-1][c]

            if prefix_sum[r][c] < k:
                count += 1
            else:
                # Since all elements are non-negative, if the sum at (r,c)
                # is >= k, any submatrix extending further will also be >= k.
                # However, we must continue to fill the prefix_sum table
                # for future calculations.
                pass

    return count
```
</details>
