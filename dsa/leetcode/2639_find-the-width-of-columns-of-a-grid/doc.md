# Find the Width of Columns of a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2639 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-width-of-columns-of-a-grid](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/).

### Goal
Given a 2D integer matrix, determine the maximum character width of each column. The width of a column is defined as the number of digits in the longest integer within that column, accounting for the negative sign if the integer is negative.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (`List[List[int]]`) representing the matrix.

**Return value**

- A list of integers (`List[int]`) where the $i$-th element represents the maximum width found in the $i$-th column of the grid.

### Examples
**Example 1**

- Input: `grid = [[1],[22],[333]]`
- Output: `[3]`

**Example 2**

- Input: `grid = [[-15,1,3],[15,7,12]]`
- Output: `[3,1,2]`

**Example 3**

- Input: `grid = [[0]]`
- Output: `[1]`

---

## Solution
### Approach
The problem is solved using a linear scan approach. We iterate through each column index, and for every column, we iterate through all rows to find the string representation length of each integer. We maintain a running maximum for each column index.

### Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we must visit every element in the grid exactly once.
- **Space Complexity**: $O(n)$ to store the result list containing the maximum width for each of the $n$ columns.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> List[int]:
    """
    Calculates the maximum width of each column in a 2D grid.
    The width is defined by the number of characters in the string representation
    of the integer, including the negative sign.
    """
    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])
    result = []

    for c in range(cols):
        max_width = 0
        for r in range(rows):
            # Convert integer to string to easily count digits and sign
            width = len(str(grid[r][c]))
            if width > max_width:
                max_width = width
        result.append(max_width)

    return result
```
</details>
