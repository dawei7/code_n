# Lucky Numbers in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1380 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [lucky-numbers-in-a-matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/lucky-numbers-in-a-matrix/).

### Goal
Find every matrix value that is the smallest number in its row and also the largest number in its column.

### Function Contract
**Inputs**

- `matrix`: a rectangular matrix of integers.

**Return value**

A list of all lucky numbers.

### Examples
**Example 1**

- Input: `matrix = [[3,7,8],[9,11,13],[15,16,17]]`
- Output: `[15]`

**Example 2**

- Input: `matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]`
- Output: `[12]`

**Example 3**

- Input: `matrix = [[7,8],[1,2]]`
- Output: `[7]`

---

## Solution
### Approach
Row and column extrema. Compute each row minimum and each column maximum, then select values that belong to both sets.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(m + n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1380: Lucky Numbers in a Matrix."""


def solve(matrix: list[list[int]]) -> list[int]:
    row_mins = {min(row) for row in matrix}
    col_maxes = {max(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))}
    return list(row_mins & col_maxes)
```
</details>
