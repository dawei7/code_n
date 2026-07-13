# Pizza With 3n Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1388 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [pizza-with-3n-slices](https://leetcode.com/problems/pizza-with-3n-slices/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/pizza-with-3n-slices/).

### Goal
A circular pizza is split into `3n` slices. Repeatedly choose one slice for yourself while the adjacent slices are taken by others, so you end up with `n` non-adjacent slices. Maximize the total size you take.

### Function Contract
**Inputs**

- `slices`: a circular list of slice sizes with length divisible by `3`.

**Return value**

The maximum total size obtainable by choosing exactly `len(slices) / 3` non-adjacent slices.

### Examples
**Example 1**

- Input: `slices = [1,2,3,4,5,6]`
- Output: `10`

**Example 2**

- Input: `slices = [8,9,8,6,1,1]`
- Output: `16`

**Example 3**

- Input: `slices = [4,1,2,5,8,3]`
- Output: `12`

---

## Solution
### Approach
Circular non-adjacent selection DP. Break the circle into two linear cases: exclude the first slice or exclude the last slice. For each case, use dynamic programming over index and count chosen.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` for `3n` slices and choosing `n` of them.
- **Space Complexity**: `O(n^2)`, reducible with rolling rows.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1388: Pizza With 3n Slices."""


def solve(slices: list[int]) -> int:
    choose = len(slices) // 3

    def best_linear(values: list[int]) -> int:
        dp = [[0] * (choose + 1) for _ in range(len(values) + 2)]
        for i, value in enumerate(values, start=2):
            for count in range(1, choose + 1):
                dp[i][count] = max(dp[i - 1][count], dp[i - 2][count - 1] + value)
        return dp[-1][choose]

    return max(best_linear(slices[:-1]), best_linear(slices[1:]))
```
</details>
