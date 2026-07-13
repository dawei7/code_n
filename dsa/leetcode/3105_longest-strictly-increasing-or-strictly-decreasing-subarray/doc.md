# Longest Strictly Increasing or Strictly Decreasing Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3105 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-strictly-increasing-or-strictly-decreasing-subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/).

### Goal
Given an array of integers, identify the length of the longest contiguous subarray that is either strictly increasing or strictly decreasing. A subarray is defined as a contiguous sequence of elements within the array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum length found among all strictly increasing or strictly decreasing contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 3, 2]`
- Output: `2`
- Explanation: The longest strictly increasing subarray is `[1, 4]` (length 2) and the longest strictly decreasing is `[4, 3]` or `[3, 2]` (length 2).

**Example 2**

- Input: `nums = [3, 3, 3, 3]`
- Output: `1`
- Explanation: Since the elements are identical, no strictly increasing or decreasing subarray can have a length greater than 1.

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `3`
- Explanation: The entire array is strictly decreasing, so the length is 3.

---

## Solution
### Approach
The problem can be solved using a single-pass linear scan (greedy approach). We maintain two counters: one for the current increasing sequence length and one for the current decreasing sequence length. As we iterate through the array, we compare adjacent elements to update these counters, resetting them to 1 whenever the strictly increasing or decreasing condition is violated.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for tracking the current and maximum lengths.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    if not nums:
        return 0

    max_len = 1
    inc_len = 1
    dec_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_len += 1
            dec_len = 1
        elif nums[i] < nums[i - 1]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = 1
            dec_len = 1

        max_len = max(max_len, inc_len, dec_len)

    return max_len
```
</details>
