# Partition Array for Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1043 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [partition-array-for-maximum-sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/partition-array-for-maximum-sum/).

### Goal
Partition an array into contiguous groups of length at most `k`. Each group contributes its maximum value repeated for the group length. Return the largest possible total.

### Function Contract
**Inputs**

- `arr`: List[int]
- `k`: int maximum partition length

**Return value**

int - maximum transformed sum

### Examples
**Example 1**

- Input: `arr = [1, 15, 7, 9, 2, 5, 10], k = 3`
- Output: `84`

**Example 2**

- Input: `arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k = 4`
- Output: `83`

**Example 3**

- Input: `arr = [1], k = 1`
- Output: `1`

---

## Solution
### Approach
One-dimensional dynamic programming.

### Complexity Analysis
- **Time Complexity**: `O(n * k)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1043: Partition Array for Maximum Sum."""


def solve(arr: list[int], k: int) -> int:
    dp = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        best = 0
        current_max = 0
        for length in range(1, min(k, i) + 1):
            current_max = max(current_max, arr[i - length])
            best = max(best, dp[i - length] + current_max * length)
        dp[i] = best
    return dp[-1]
```
</details>
