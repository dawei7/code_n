# Uncrossed Lines

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1035 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [uncrossed-lines](https://leetcode.com/problems/uncrossed-lines/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/uncrossed-lines/).

### Goal
Given two integer arrays, draw as many noncrossing equal-value connections as possible between the arrays. Return the maximum number of connections.

### Function Contract
**Inputs**

- `nums1`: List[int]
- `nums2`: List[int]

**Return value**

int - maximum number of noncrossing matching pairs

### Examples
**Example 1**

- Input: `nums1 = [1, 4, 2], nums2 = [1, 2, 4]`
- Output: `2`

**Example 2**

- Input: `nums1 = [2, 5, 1, 2, 5], nums2 = [10, 5, 2, 1, 5, 2]`
- Output: `3`

**Example 3**

- Input: `nums1 = [1, 3, 7, 1, 7, 5], nums2 = [1, 9, 2, 5, 1]`
- Output: `2`

---

## Solution
### Approach
Longest common subsequence dynamic programming.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1035: Uncrossed Lines."""


def solve(nums1: list[int], nums2: list[int]) -> int:
    previous = [0] * (len(nums2) + 1)
    for value1 in nums1:
        current = [0] * (len(nums2) + 1)
        for j, value2 in enumerate(nums2, start=1):
            if value1 == value2:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        previous = current
    return previous[-1]
```
</details>
