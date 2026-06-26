# Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1546 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Prefix Sum |
| Official Link | [maximum-number-of-non-overlapping-subarrays-with-sum-equals-target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) |

## Problem Description & Examples
### Goal
Find the maximum number of non-overlapping contiguous subarrays whose sum equals
`target`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `target`: the desired subarray sum.

**Return value**

The largest count of pairwise non-overlapping target-sum subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 2`
- Output: `2`

**Example 2**

- Input: `nums = [-1, 3, 5, 1, 4, 2, -9], target = 6`
- Output: `2`

**Example 3**

- Input: `nums = [3, 4, 7, 2, -3, 1, 4, 2], target = 7`
- Output: `3`

---

## Underlying Base Algorithm(s)
Scan with prefix sums and a set of prefix sums seen since the end of the last
chosen subarray. If `prefix - target` is present, a valid subarray ends here;
greedily take it, increment the answer, and reset the set so future subarrays do
not overlap.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.
