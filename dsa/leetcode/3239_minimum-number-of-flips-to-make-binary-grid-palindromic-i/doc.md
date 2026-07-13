# Minimum Number of Flips to Make Binary Grid Palindromic I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3239 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-flips-to-make-binary-grid-palindromic-i](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/).

### Goal
Given a binary matrix, determine the minimum number of bit flips (changing 0 to 1 or vice versa) required to make either all rows palindromic or all columns palindromic. A row or column is palindromic if it reads the same forwards and backwards.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (a 2D binary matrix).

**Return value**

- An integer representing the minimum flips needed to satisfy the condition for either all rows or all columns.

### Examples
**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,1],[0,1],[0,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1],[0]]`
- Output: `0`

---

## Solution
### Approach
The problem relies on the **Two Pointers** technique. For each row (or column), we compare elements at index `i` and `n - 1 - i` moving towards the center. Each mismatch requires exactly one flip to make that specific row (or column) a palindrome. We calculate the total flips required for all rows and all columns independently, then return the minimum of the two sums.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. We iterate through every element in the grid exactly twice (once for row checks, once for column checks).
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the flip counts, regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    # Calculate flips needed to make all rows palindromic
    row_flips = 0
    for r in range(rows):
        left, right = 0, cols - 1
        while left < right:
            if grid[r][left] != grid[r][right]:
                row_flips += 1
            left += 1
            right -= 1

    # Calculate flips needed to make all columns palindromic
    col_flips = 0
    for c in range(cols):
        top, bottom = 0, rows - 1
        while top < bottom:
            if grid[top][c] != grid[bottom][c]:
                col_flips += 1
            top += 1
            bottom -= 1

    return min(row_flips, col_flips)
```
</details>
