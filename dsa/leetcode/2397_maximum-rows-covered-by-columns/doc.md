# Maximum Rows Covered by Columns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2397 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-rows-covered-by-columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-rows-covered-by-columns/).

### Goal
Given a binary matrix and an integer `numSelect`, determine the maximum number of rows that can be fully "covered" by selecting exactly `numSelect` columns. A row is considered covered if all its cells containing a 1 are located within the chosen set of columns.

### Function Contract
**Inputs**

- `matrix`: A 2D list of integers (0 or 1) representing the grid.
- `numSelect`: An integer representing the number of columns to choose.

**Return value**

- An integer representing the maximum number of rows that can be covered.

### Examples
**Example 1**

- Input: `matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2`
- Output: `3`

**Example 2**

- Input: `matrix = [[1],[0]], numSelect = 1`
- Output: `2`

---

## Solution
### Approach
The problem is solved using **Combinatorial Enumeration** (specifically combinations) combined with **Bit Manipulation**. Since the number of columns is small (up to 12), we can represent each row as a bitmask. We iterate through all possible combinations of `numSelect` columns, represent the selection as a bitmask, and check if each row's bitmask is a subset of the selected columns' mask.

### Complexity Analysis
- **Time Complexity**: `O(C(n, k) * m)`, where `n` is the number of columns, `k` is `numSelect`, and `m` is the number of rows. We evaluate all combinations of columns and for each, iterate through all rows.
- **Space Complexity**: `O(m)` to store the bitmask representation of each row.

### Reference Implementations
<details>
<summary>python</summary>

```python
from itertools import combinations

def solve(matrix: list[list[int]], num_select: int) -> int:
    m = len(matrix)
    n = len(matrix[0])

    # Convert each row into a bitmask for efficient comparison
    row_masks = []
    for row in matrix:
        mask = 0
        for j in range(n):
            if row[j] == 1:
                mask |= (1 << j)
        row_masks.append(mask)

    max_covered = 0

    # Generate all combinations of column indices to select
    for cols in combinations(range(n), num_select):
        # Create a mask representing the selected columns
        selection_mask = 0
        for col in cols:
            selection_mask |= (1 << col)

        # Count rows covered by this selection
        # A row is covered if (row_mask & selection_mask) == row_mask
        # This is equivalent to (row_mask & ~selection_mask) == 0
        count = 0
        for r_mask in row_masks:
            if (r_mask & selection_mask) == r_mask:
                count += 1

        if count > max_covered:
            max_covered = count

    return max_covered
```
</details>
