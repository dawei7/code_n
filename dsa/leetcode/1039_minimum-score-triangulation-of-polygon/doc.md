# Minimum Score Triangulation of Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1039 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-score-triangulation-of-polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/).

### Goal
Given values on the vertices of a convex polygon in order, split the polygon into triangles. The score of a triangle is the product of its three vertex values. Return the minimum total triangulation score.

### Function Contract
**Inputs**

- `values`: List[int] polygon vertex values in circular order

**Return value**

int - minimum possible triangulation score

### Examples
**Example 1**

- Input: `values = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `values = [3, 7, 4, 5]`
- Output: `144`

**Example 3**

- Input: `values = [1, 3, 1, 4, 1, 5]`
- Output: `13`

---

## Solution
### Approach
Interval dynamic programming.

### Complexity Analysis
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1039: Minimum Score Triangulation of Polygon."""


def solve(values: list[int]) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    for length in range(3, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            dp[left][right] = min(
                dp[left][mid]
                + dp[mid][right]
                + values[left] * values[mid] * values[right]
                for mid in range(left + 1, right)
            )
    return dp[0][n - 1]
```
</details>
