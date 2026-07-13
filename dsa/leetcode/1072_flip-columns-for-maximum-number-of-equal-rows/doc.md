# Flip Columns For Maximum Number of Equal Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1072 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [flip-columns-for-maximum-number-of-equal-rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/).

### Goal
Given a binary matrix, you may flip any set of columns. Return the maximum number of rows that can become all equal values within each row.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

int - maximum number of rows that can be made uniform

### Examples
**Example 1**

- Input: `matrix = [[0, 1], [1, 1]]`
- Output: `1`

**Example 2**

- Input: `matrix = [[0, 1], [1, 0]]`
- Output: `2`

**Example 3**

- Input: `matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `2`

---

## Solution
### Approach
Pattern normalization and hash counting.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for stored row patterns

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1072: Flip Columns For Maximum Number of Equal Rows."""

from collections import Counter


def solve(matrix: list[list[int]]) -> int:
    patterns: Counter[tuple[int, ...]] = Counter()
    for row in matrix:
        first = row[0]
        pattern = tuple(value ^ first for value in row)
        patterns[pattern] += 1
    return max(patterns.values())
```
</details>
