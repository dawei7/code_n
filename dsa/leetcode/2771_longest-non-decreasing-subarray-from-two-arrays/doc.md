# Longest Non-decreasing Subarray From Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2771 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-non-decreasing-subarray-from-two-arrays](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/).

### Goal
Given two arrays of equal length, construct a new sequence by picking exactly one element from either array at each index. The objective is to find the length of the longest contiguous subarray within this constructed sequence that is non-decreasing.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- An integer representing the maximum length of a non-decreasing subarray formed by choosing elements from `nums1` or `nums2` at each position.

### Examples
**Example 1**

- Input: `nums1 = [2,3,1], nums2 = [1,2,1]`
- Output: `2`

**Example 2**

- Input: `nums1 = [1,3,2,1], nums2 = [2,2,3,4]`
- Output: `4`

**Example 3**

- Input: `nums1 = [1,1], nums2 = [2,2]`
- Output: `2`

---

## Solution
### Approach
Dynamic Programming. We maintain two states at each index `i`: the length of the longest non-decreasing subarray ending at `i` using `nums1[i]` and the length of the longest non-decreasing subarray ending at `i` using `nums2[i]`. Transitions involve checking if the current element is greater than or equal to the previous elements chosen from either array.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input arrays, as we iterate through the arrays exactly once.
- **Space Complexity**: `O(1)`, as we only need to store the DP states for the previous index to calculate the current index.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    if n == 0:
        return 0

    # dp1: length of non-decreasing subarray ending at index i using nums1[i]
    # dp2: length of non-decreasing subarray ending at index i using nums2[i]
    dp1 = 1
    dp2 = 1
    max_len = 1

    for i in range(1, n):
        # Calculate potential new lengths for index i
        # We can extend from either nums1[i-1] or nums2[i-1]
        new_dp1 = 1
        new_dp2 = 1

        if nums1[i] >= nums1[i-1]:
            new_dp1 = max(new_dp1, dp1 + 1)
        if nums1[i] >= nums2[i-1]:
            new_dp1 = max(new_dp1, dp2 + 1)

        if nums2[i] >= nums1[i-1]:
            new_dp2 = max(new_dp2, dp1 + 1)
        if nums2[i] >= nums2[i-1]:
            new_dp2 = max(new_dp2, dp2 + 1)

        dp1, dp2 = new_dp1, new_dp2
        max_len = max(max_len, dp1, dp2)

    return max_len
```
</details>
