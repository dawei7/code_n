# Select Cells in Grid With Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3276 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [select-cells-in-grid-with-maximum-score](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/).

### Goal
Given a 2D grid of integers, select a set of cells such that no two cells share the same row. Each selected cell must contain a unique value. The objective is to maximize the sum of the values of the selected cells.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.

**Return value**

- An integer representing the maximum possible sum of selected cells.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `18`

**Example 2**

- Input: `grid = [[8,7,6],[8,3,1]]`
- Output: `15`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6]]`
- Output: `9`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with Bitmasking. Since we need to select cells with unique values across different rows, we first group the row indices for each unique value present in the grid. We then iterate through the sorted unique values and maintain a bitmask representing the set of rows already occupied. The state `dp[mask]` stores the maximum sum achievable using a subset of rows represented by the bitmask.

### Complexity Analysis
- **Time Complexity**: `O(V * 2^R)`, where `V` is the number of unique values in the grid and `R` is the number of rows. In the worst case, this is efficient enough given the constraints on grid dimensions.
- **Space Complexity**: `O(2^R)` to store the DP table for all possible row combinations.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    # Map each value to the list of rows it appears in
    val_to_rows = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            val_to_rows[grid[r][c]].append(r)

    # Sort unique values to process them in order
    unique_vals = sorted(val_to_rows.keys(), reverse=True)

    # dp[mask] = max sum using rows represented by mask
    # mask is a bitmask of length 'rows'
    dp = {0: 0}

    for val in unique_vals:
        new_dp = dp.copy()
        possible_rows = set(val_to_rows[val])

        for mask, current_sum in dp.items():
            for r in possible_rows:
                # If row r is not yet used in the mask
                if not (mask & (1 << r)):
                    new_mask = mask | (1 << r)
                    new_dp[new_mask] = max(new_dp.get(new_mask, 0), current_sum + val)
        dp = new_dp

    return max(dp.values())
```
</details>
