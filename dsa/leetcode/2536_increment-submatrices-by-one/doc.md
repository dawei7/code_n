# Increment Submatrices by One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2536 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [increment-submatrices-by-one](https://leetcode.com/problems/increment-submatrices-by-one/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/increment-submatrices-by-one/).

### Goal
Given an $n \times n$ grid initialized with zeros, process a series of queries. Each query specifies a submatrix defined by its top-left $(r1, c1)$ and bottom-right $(r2, c2)$ coordinates. For every query, increment all cells within the specified rectangular region by 1. Return the final state of the grid after all queries have been applied.

### Function Contract
**Inputs**

- `n`: An integer representing the dimensions of the $n \times n$ grid.
- `queries`: A list of lists, where each inner list contains four integers `[r1, c1, r2, c2]` representing the bounds of the submatrix to increment.

**Return value**

- A 2D list of integers (size $n \times n$) representing the grid after all increments.

### Examples
**Example 1**

- Input: `n = 3, queries = [[1,1,2,2],[0,0,1,1]]`
- Output: `[[1,1,0],[1,2,1],[0,1,1]]`

**Example 2**

- Input: `n = 2, queries = [[0,0,1,1]]`
- Output: `[[1,1],[1,1]]`

**Example 3**

- Input: `n = 1, queries = [[0,0,0,0]]`
- Output: `[[1]]`

---

## Solution
### Approach
The problem is solved using a **2D Difference Array** (a variation of the prefix sum technique). Instead of updating every cell in the submatrix (which would be $O(n^2)$ per query), we mark the boundaries of the increment. For a submatrix defined by $(r1, c1)$ to $(r2, c2)$, we increment `grid[r1][c1]`, decrement `grid[r1][c2+1]`, decrement `grid[r2+1][c1]`, and increment `grid[r2+1][c2+1]`. After processing all queries, we compute the 2D prefix sum to reconstruct the final grid values.

### Complexity Analysis
- **Time Complexity**: $O(q + n^2)$, where $q$ is the number of queries and $n$ is the grid dimension. We process each query in $O(1)$ and perform a prefix sum pass over the $n \times n$ grid.
- **Space Complexity**: $O(n^2)$ to store the grid.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, queries: list[list[int]]) -> list[list[int]]:
    # Initialize a difference array with size (n+1) x (n+1)
    # to handle boundary conditions easily.
    diff = [[0] * (n + 1) for _ in range(n + 1)]

    for r1, c1, r2, c2 in queries:
        diff[r1][c1] += 1
        if r2 + 1 < n:
            diff[r2 + 1][c1] -= 1
        if c2 + 1 < n:
            diff[r1][c2 + 1] -= 1
        if r2 + 1 < n and c2 + 1 < n:
            diff[r2 + 1][c2 + 1] += 1

    # Compute the 2D prefix sum to get the actual values
    res = [[0] * n for _ in range(n)]

    # First, compute prefix sums along rows
    for r in range(n):
        current_row_sum = 0
        for c in range(n):
            current_row_sum += diff[r][c]
            diff[r][c] = current_row_sum

    # Then, compute prefix sums along columns
    for c in range(n):
        current_col_sum = 0
        for r in range(n):
            current_col_sum += diff[r][c]
            res[r][c] = current_col_sum

    return res
```
</details>
