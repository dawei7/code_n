# Row With Maximum Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2643 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [row-with-maximum-ones](https://leetcode.com/problems/row-with-maximum-ones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/row-with-maximum-ones/).

### Goal
Given a binary matrix (a 2D grid containing only 0s and 1s), identify the row index that contains the highest count of 1s. If multiple rows share the same maximum count, return the index of the row that appears first.

### Function Contract
**Inputs**

- `mat`: A list of lists of integers (`List[List[int]]`) representing an $m \times n$ binary matrix.

**Return value**

- A list of two integers: `[index, count]`, where `index` is the row number with the most 1s, and `count` is the total number of 1s found in that row.

### Examples
**Example 1**

- Input: `mat = [[0,1],[1,0]]`
- Output: `[0, 1]`

**Example 2**

- Input: `mat = [[0,0,0],[0,1,1]]`
- Output: `[1, 2]`

**Example 3**

- Input: `mat = [[0,0],[1,1],[0,0]]`
- Output: `[1, 2]`

---

## Solution
### Approach
The problem is solved using a linear scan (traversal) of the matrix. We iterate through each row, calculate the sum of its elements (which effectively counts the 1s since the matrix is binary), and maintain a running maximum to track the best row found so far.

### Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we must inspect every element in the matrix at least once.
- **Space Complexity**: $O(1)$, as we only store a few integer variables to track the current maximum index and count, regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(mat: List[List[int]]) -> List[int]:
    max_row_index = 0
    max_ones_count = -1

    for i, row in enumerate(mat):
        # Since the matrix contains only 0s and 1s,
        # the sum of the row equals the count of 1s.
        current_ones_count = sum(row)

        if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
            max_row_index = i

    return [max_row_index, max_ones_count]
```
</details>
