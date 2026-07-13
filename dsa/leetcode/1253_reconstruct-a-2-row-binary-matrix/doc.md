# Reconstruct a 2-Row Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1253 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reconstruct-a-2-row-binary-matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/).

### Goal
Build a two-row binary matrix whose row sums are `upper` and `lower`, and whose column sums match the given `colsum` array.

### Function Contract
**Inputs**

- `upper`: required sum of the first row.
- `lower`: required sum of the second row.
- `colsum`: required sum for each column, each value being `0`, `1`, or `2`.

**Return value**

A valid two-row binary matrix, or an empty list if impossible.

### Examples
**Example 1**

- Input: `upper = 2`, `lower = 1`, `colsum = [1,1,1]`
- Output: `[[1,1,0],[0,0,1]]`

**Example 2**

- Input: `upper = 2`, `lower = 3`, `colsum = [2,2,1,1]`
- Output: `[]`

**Example 3**

- Input: `upper = 5`, `lower = 5`, `colsum = [2,1,2,0,1,0,1,2,0,1]`
- Output: `[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]`

---

## Solution
### Approach
Greedy construction.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(upper, lower, colsum):
    top = [0] * len(colsum)
    bottom = [0] * len(colsum)
    for i, value in enumerate(colsum):
        if value == 2:
            top[i] = bottom[i] = 1
            upper -= 1
            lower -= 1
    if upper < 0 or lower < 0:
        return []
    for i, value in enumerate(colsum):
        if value == 1:
            if upper > lower:
                top[i] = 1
                upper -= 1
            else:
                bottom[i] = 1
                lower -= 1
    return [top, bottom] if upper == 0 and lower == 0 else []
```
</details>
