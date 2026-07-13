# Max Consecutive Ones III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1004 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [max-consecutive-ones-iii](https://leetcode.com/problems/max-consecutive-ones-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/max-consecutive-ones-iii/).

### Goal
Given a binary array and an allowance `k`, return the longest contiguous segment that can be made all `1`s by changing at most `k` zeroes.

### Function Contract
**Inputs**

- `nums`: List[int] containing only 0 and 1
- `k`: int maximum zeroes allowed in the window

**Return value**

int - maximum valid window length

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- Output: `6`

**Example 2**

- Input: `nums = [0, 0, 1, 1, 0, 1], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 1, 1], k = 0`
- Output: `3`

---

## Solution
### Approach
Sliding window with a zero counter.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1004: Max Consecutive Ones III."""


def solve(nums: list[int], k: int) -> int:
    left = 0
    zeroes = 0
    best = 0
    for right, value in enumerate(nums):
        if value == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```
</details>
