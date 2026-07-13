# Modify the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3033 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [modify-the-matrix](https://leetcode.com/problems/modify-the-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/modify-the-matrix/).

### Goal
Given a 2D integer matrix, replace every occurrence of -1 with the maximum value found in its respective column. The transformation should be performed in-place or returned as a new matrix, ensuring that the original -1 values are updated based on the column-wise maximums calculated from the original matrix state.

### Function Contract
**Inputs**

- `matrix`: A list of lists of integers (`List[List[int]]`) representing the grid.

**Return value**

- A list of lists of integers (`List[List[int]]`) where all -1s have been replaced by the maximum value of their column.

### Examples
**Example 1**

- Input: `matrix = [[1,2,-1],[4,-1,6],[7,8,9]]`
- Output: `[[1,2,9],[4,8,6],[7,8,9]]`

**Example 2**

- Input: `matrix = [[3,-1],[5,2]]`
- Output: `[[3,2],[5,2]]`

**Example 3**

- Input: `matrix = [[-1]]`
- Output: `[[0]]` (Note: If the max is -1, it remains -1 unless specified otherwise; however, per problem constraints, -1 is replaced by the max of the column).

---

## Solution
### Approach
The algorithm utilizes a two-pass approach:
1. **Column Maximum Calculation**: Iterate through each column to determine the maximum value present in that column.
2. **Matrix Transformation**: Iterate through the matrix again, replacing any -1 with the pre-calculated maximum for that specific column.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we traverse the matrix twice.
- **Space Complexity**: `O(n)` to store the maximum values for each of the `n` columns.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0])

    # Precompute the maximum value for each column
    col_maxes = []
    for c in range(cols):
        current_max = -1
        for r in range(rows):
            if matrix[r][c] > current_max:
                current_max = matrix[r][c]
        col_maxes.append(current_max)

    # Create a result matrix or modify in place
    # Here we modify in place for efficiency
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == -1:
                matrix[r][c] = col_maxes[c]

    return matrix
```
</details>
