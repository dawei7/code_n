# Count the Number of Incremovable Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2972 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-incremovable-subarrays-ii](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/).

### Goal
Given an array of integers, determine the total number of subarrays that, when removed, leave the remaining elements in a strictly increasing order. A subarray is defined as a contiguous sequence of elements within the array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of "incremovable" subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`

**Example 2**

- Input: `nums = [6, 5, 7, 8]`
- Output: `7`

**Example 3**

- Input: `nums = [8, 7, 6, 6]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a **Two Pointers** approach. We first identify the longest strictly increasing prefix and the longest strictly increasing suffix. By removing a subarray between these two segments, we can form a valid sequence if the last element of the prefix is smaller than the first element of the suffix. We iterate through all possible valid prefixes and use binary search (or a second pointer) to count how many valid suffixes can be paired with each prefix.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array to find the prefix and suffix boundaries and then perform a linear scan to count the valid combinations.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track indices and the count.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)

    # Find the longest strictly increasing prefix
    left = 0
    while left + 1 < n and nums[left] < nums[left + 1]:
        left += 1

    # If the whole array is strictly increasing
    if left == n - 1:
        return n * (n + 1) // 2

    # Find the longest strictly increasing suffix
    right = n - 1
    while right - 1 >= 0 and nums[right - 1] < nums[right]:
        right -= 1

    count = 0
    j = right
    # i == -1 means the whole kept part, if any, comes from the suffix.
    for i in range(-1, left + 1):
        while i >= 0 and j < n and nums[j] <= nums[i]:
            j += 1
        count += (n - j + 1)

    return count
```
</details>
