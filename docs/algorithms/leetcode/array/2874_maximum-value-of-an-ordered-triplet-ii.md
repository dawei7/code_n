# Maximum Value of an Ordered Triplet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2874 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [maximum-value-of-an-ordered-triplet-ii](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, find the maximum value of the expression `(nums[i] - nums[j]) * nums[k]` for all indices `i < j < k`. If the result of the expression is negative, return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers where `3 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^6`.

**Return value**

- An integer representing the maximum possible value of the triplet expression, or 0 if all possible results are negative.

### Examples
**Example 1**

- Input: `nums = [12,6,1,2,7]`
- Output: `77`
- Explanation: The triplet (i=0, j=1, j=2) gives (12 - 6) * 1 = 6. The triplet (i=0, j=1, j=4) gives (12 - 6) * 7 = 42. The triplet (i=0, j=2, j=4) gives (12 - 1) * 7 = 77.

**Example 2**

- Input: `nums = [1,10,3,4,19]`
- Output: `133`
- Explanation: The triplet (i=0, j=2, j=4) gives (1 - 3) * 19 = -38. The triplet (i=1, j=2, j=4) gives (10 - 3) * 19 = 133.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `0`
- Explanation: (1 - 2) * 3 = -3. Since the result is negative, return 0.

---

## Underlying Base Algorithm(s)
The problem is solved using a single-pass linear scan (prefix/suffix tracking). By maintaining the maximum value seen so far (`max_i`) and the maximum difference `(nums[i] - nums[j])` seen so far (`max_diff`), we can calculate the potential result for each index `k` in constant time.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.
