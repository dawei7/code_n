# Longest Arithmetic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1027 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-arithmetic-subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-arithmetic-subsequence/).

### Goal
Given an integer array, return the length of the longest subsequence whose adjacent differences are all the same.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum arithmetic subsequence length

### Examples
**Example 1**

- Input: `nums = [3, 6, 9, 12]`
- Output: `4`

**Example 2**

- Input: `nums = [9, 4, 7, 2, 10]`
- Output: `3`

**Example 3**

- Input: `nums = [20, 1, 15, 3, 10, 5, 8]`
- Output: `4`

---

## Solution
### Approach
Dynamic programming by ending index and difference.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1027: Longest Arithmetic Subsequence."""


def solve(nums: list[int]) -> int:
    dp: list[dict[int, int]] = [{} for _ in nums]
    best = 0
    for i, value in enumerate(nums):
        for j in range(i):
            diff = value - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            best = max(best, dp[i][diff])
    return best
```
</details>
