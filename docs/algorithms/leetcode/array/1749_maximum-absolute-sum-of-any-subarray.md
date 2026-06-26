# Maximum Absolute Sum of Any Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1749 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-absolute-sum-of-any-subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) |

## Problem Description & Examples
### Goal
Find the largest absolute value of the sum of any non-empty contiguous subarray.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the maximum absolute subarray sum.

### Examples
**Example 1**

- Input: `nums = [1,-3,2,3,-4]`
- Output: `5`

**Example 2**

- Input: `nums = [2,-5,1,-4,3,-2]`
- Output: `8`

**Example 3**

- Input: `nums = [-1,-2,-3]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Track prefix sums. The sum of any subarray is the difference between two prefix sums, so the maximum absolute subarray sum is `max_prefix - min_prefix`. Equivalently, run Kadane's algorithm for both maximum and minimum subarray sums and take the larger absolute value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
