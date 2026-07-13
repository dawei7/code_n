# Difference of Number of Distinct Values on Diagonals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2711 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [difference-of-number-of-distinct-values-on-diagonals](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/).

### Goal
Given a 0-indexed `m x n` integer matrix `grid`, the task is to construct and return a new matrix `diff` of the same dimensions. For each cell `(r, c)` in the original `grid`, the corresponding cell `diff[r][c]` should store the absolute difference between two counts:
1. The number of distinct values found on the top-left diagonal segment that includes `(r, c)` and extends upwards and leftwards.
2. The number of distinct values found on the bottom-right diagonal segment that includes `(r, c)` and extends downwards and rightwards.

The top-left diagonal segment for `(r, c)` includes all cells `(x, y)` such that `x <= r`, `y <= c`, and `x - y == r - c`.
The bottom-right diagonal segment for `(r, c)` includes all cells `(x, y)` such that `x >= r`, `y >= c`, and `x + y == r + c`.

### Function Contract
**Inputs**

- `grid`: A `List[List[int]]` representing the `m x n` integer matrix. `m` is the number of rows and `n` is the number of columns.
  - `1 <= m, n <= 100`
  - `1 <= grid[i][j] <= 100`

**Return value**

- A `List[List[int]]` representing the `m x n` `diff` matrix, where `diff[r][c]` is calculated as described above.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[0,0,0],[0,1,1],[0,1,2]]`
- Explanation:
  - For `diff[0][0]`: TL-diag: `{1}` (count=1), BR-diag: `{1}` (count=1). `|1-1|=0`.
  - For `diff[1][1]`: TL-diag: `{1,5}` (count=2), BR-diag: `{5}` (count=1). `|2-1|=1`.
  - For `diff[0][2]`: TL-diag: `{3}` (count=1), BR-diag: `{3,5,7}` (count=3). `|1-3|=2`.

**Example 2**

- Input: `grid = [[1]]`
- Output: `[[0]]`
- Explanation:
  - For `diff[0][0]`: TL-diag: `{1}` (count=1), BR-diag: `{1}` (count=1). `|1-1|=0`.

**Example 3**

- Input: `grid = [[3,2,1],[1,7,6],[2,7,7]]`
- Output: `[[0,1,1],[1,1,0],[1,0,0]]`
- Explanation:
  - For `diff[0][0]`: TL-diag: `{3}` (count=1), BR-diag: `{3}` (count=1). `|1-1|=0`.
  - For `diff[0][1]`: TL-diag: `{2}` (count=1), BR-diag: `{2,7}` (count=2). `|1-2|=1`.
  - For `diff[1][1]`: TL-diag: `{3,7}` (count=2), BR-diag: `{7}` (count=1). `|2-1|=1`.

---

## Solution
### Approach
The core algorithm involves iterating through each cell `(r, c)` of the input `grid` and, for each cell, performing two separate traversals to identify and count distinct elements on its specific diagonal segments.

1.  **Matrix Traversal:** A nested loop iterates through every cell `(r, c)` from `(0, 0)` to `(m-1, n-1)`.
2.  **Diagonal Segment Traversal:**
    *   **Top-Left Diagonal:** For a given cell `(r, c)`, we start at `(r, c)` and move diagonally upwards and leftwards. This means decrementing both the row and column indices (`curr_r -= 1`, `curr_c -= 1`) in each step. We continue this traversal as long as `curr_r >= 0` and `curr_c >= 0`. During this traversal, all encountered values are added to a `set` to keep track of distinct elements.
    *   **Bottom-Right Diagonal:** Similarly, for the same cell `(r, c)`, we start at `(r, c)` and move diagonally downwards and rightwards. This involves incrementing both the row and column indices (`curr_r += 1`, `curr_c += 1`) in each step. This traversal continues as long as `curr_r < m` and `curr_c < n`. Values are added to a separate `set` for distinct counting.
3.  **Difference Calculation:** After both diagonal segments are traversed and their distinct counts obtained (by taking the `len()` of the respective sets), the absolute difference between these two counts is calculated and stored in `diff[r][c]`.

This process is repeated for all cells in the `grid` to populate the entire `diff` matrix.

### Complexity Analysis
Let `m` be the number of rows and `n` be the number of columns in the `grid`.

- **Time Complexity**: `O(m * n * min(m, n))`
    - The algorithm iterates through each of the `m * n` cells in the input `grid`.
    - For each cell `(r, c)`:
        - Traversing the top-left diagonal segment: In the worst case (e.g., for `grid[m-1][n-1]`), this segment can have up to `min(r + 1, c + 1)` elements. This is bounded by `min(m, n)` elements.
        - Traversing the bottom-right diagonal segment: In the worst case (e.g., for `grid[0][0]`), this segment can have up to `min(m - r, n - c)` elements. This is also bounded by `min(m, n)` elements.
        - Adding elements to a `set` and checking its length takes `O(1)` on average for each element.
    - Therefore, for each of the `m * n` cells, we perform `O(min(m, n))` operations.
    - The total time complexity is `O(m * n * min(m, n))`. Given `m, n <= 100`, this is at most `100 * 100 * 100 = 10^6` operations, which is efficient enough.

- **Space Complexity**: `O(m * n)`
    - An output matrix `diff` of size `m x n` is created to store the results, contributing `O(m * n)` to the space complexity.
    - During the calculation for each cell `(r, c)`, two `set` objects are used to store distinct values for the top-left and bottom-right diagonals. In the worst case, each set can store up to `min(m, n)` distinct elements. This auxiliary space is `O(min(m, n))` at any given point in time.
    - Since `O(m * n)` (for the output matrix) dominates `O(min(m, n))` (for the temporary sets), the overall space complexity is `O(m * n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])

    # Initialize the diff matrix with zeros
    diff_matrix = [[0] * n for _ in range(m)]

    # Iterate through each cell (r, c) in the grid
    for r in range(m):
        for c in range(n):
            # Calculate distinct values on the top-left diagonal segment
            tl_distinct = set()
            curr_r, curr_c = r - 1, c - 1
            while curr_r >= 0 and curr_c >= 0:
                tl_distinct.add(grid[curr_r][curr_c])
                curr_r -= 1
                curr_c -= 1

            # Calculate distinct values on the bottom-right diagonal segment
            br_distinct = set()
            curr_r, curr_c = r + 1, c + 1
            while curr_r < m and curr_c < n:
                br_distinct.add(grid[curr_r][curr_c])
                curr_r += 1
                curr_c += 1

            # Store the absolute difference of distinct counts in the diff_matrix
            diff_matrix[r][c] = abs(len(tl_distinct) - len(br_distinct))

    return diff_matrix
```
</details>
