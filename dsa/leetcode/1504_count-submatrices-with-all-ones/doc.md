# Count Submatrices With All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1504 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Matrix, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-submatrices-with-all-ones](https://leetcode.com/problems/count-submatrices-with-all-ones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-submatrices-with-all-ones/).

### Goal
Count every rectangular submatrix that contains only `1` values.

### Function Contract
**Inputs**

- `mat`: a binary matrix.

**Return value**

The total number of all-one submatrices.

### Examples
**Example 1**

- Input: `mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]`
- Output: `13`

**Example 2**

- Input: `mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]`
- Output: `24`

**Example 3**

- Input: `mat = [[1, 1], [1, 1]]`
- Output: `9`

---

## Solution
### Approach
Treat each row as the base of a histogram of consecutive ones above it. For each
row, use a monotonic stack to count how many all-one rectangles end at each
column, then add those row contributions to the answer.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(mat):
    if not mat:
        return 0
    grid = []
    width = 0
    for row in mat:
        values = list(row) if isinstance(row, (list, str)) else [row]
        width = max(width, len(values))
        grid.append(values)
    heights = [0] * width
    answer = 0
    for row in grid:
        row = row + [0] * (width - len(row))
        stack = []
        row_sum = 0
        for col, value in enumerate(row):
            heights[col] = heights[col] + 1 if value in (1, "1", "A", True) else 0
            count = 1
            while stack and stack[-1][0] >= heights[col]:
                height, previous_count = stack.pop()
                row_sum -= height * previous_count
                count += previous_count
            stack.append((heights[col], count))
            row_sum += heights[col] * count
            answer += row_sum
    return answer
```
</details>
