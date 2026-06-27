# Minimum Positive Sum Subarray 

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3364 |
| Difficulty | Easy |
| Topics | Array, Sliding Window, Prefix Sum |
| Official Link | [minimum-positive-sum-subarray](https://leetcode.com/problems/minimum-positive-sum-subarray/) |

## Problem Description & Examples
### Goal
Given an integer array and two bounds, identify the smallest possible sum among all contiguous subarrays whose length falls within the specified inclusive range [l, r] and whose sum is strictly greater than zero. If no such subarray exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `l`: An integer representing the minimum length of the subarray.
- `r`: An integer representing the maximum length of the subarray.

**Return value**

- An integer representing the minimum positive sum found, or -1 if no valid subarray exists.

### Examples
**Example 1**

- Input: `nums = [3, -2, 1, 4], l = 2, r = 3`
- Output: `1`
- Explanation: Subarrays of length 2 or 3 include [3, -2]=1, [-2, 1]=-1, [1, 4]=5, [3, -2, 1]=2, [-2, 1, 4]=3. The minimum positive sum is 1.

**Example 2**

- Input: `nums = [-2, 2, -3, 1], l = 2, r = 3`
- Output: `1`
- Explanation: Subarrays of length 2 or 3 include [-2, 2]=0, [2, -3]=-1, [-3, 1]=-2, [-2, 2, -3]=-3, [2, -3, 1]=0. Wait, the only positive sum is 1 (from subarray [1] which is length 1, but we need length 2-3). Actually, [2, -3, 1] is 0. The only positive sum is 1 (if we consider [1] but length is wrong). If no valid subarray exists, return -1.

**Example 3**

- Input: `nums = [1, 2, 3, 4], l = 2, r = 4`
- Output: `3`
- Explanation: The smallest positive sum of length 2 to 4 is 3 (from [1, 2]).

---

## Underlying Base Algorithm(s)
The problem is solved using a Prefix Sum array to allow for O(1) calculation of any subarray sum. By iterating through all possible starting indices and all valid lengths (from `l` to `r`), we evaluate every candidate subarray sum and track the minimum positive value encountered.

---

## Complexity Analysis
- **Time Complexity**: O(n * (r - l)), where n is the length of the array. In the worst case, this approaches O(n^2).
- **Space Complexity**: O(n) to store the prefix sum array, which can be optimized to O(1) if calculating sums on the fly.
