# Maximize Sum Of Array After K Negations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1005 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-sum-of-array-after-k-negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/).

### Goal
You may choose an array element and flip its sign exactly `k` times. Return the largest possible array sum after all flips are used.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int number of sign flips

**Return value**

int - maximum achievable sum

### Examples
**Example 1**

- Input: `nums = [4, 2, 3], k = 1`
- Output: `5`

**Example 2**

- Input: `nums = [3, -1, 0, 2], k = 3`
- Output: `6`

**Example 3**

- Input: `nums = [2, -3, -1, 5, -4], k = 2`
- Output: `13`

---

## Solution
### Approach
Greedy sign flipping after sorting by value.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1005: Maximize Sum Of Array After K Negations."""


def solve(nums: list[int], k: int) -> int:
    nums.sort()
    for i, value in enumerate(nums):
        if k == 0 or value >= 0:
            break
        nums[i] = -value
        k -= 1

    total = sum(nums)
    if k % 2 == 1:
        total -= 2 * min(nums)
    return total
```
</details>
