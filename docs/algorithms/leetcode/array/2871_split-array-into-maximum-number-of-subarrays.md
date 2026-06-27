# Split Array Into Maximum Number of Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2871 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation |
| Official Link | [split-array-into-maximum-number-of-subarrays](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, partition the array into the maximum number of contiguous subarrays such that the bitwise AND of each subarray is equal to the minimum possible total bitwise AND of the entire array.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers (`List[int]`).

**Return value**

- An integer representing the maximum number of subarrays the array can be split into.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2, 0, 1, 2]`
- Output: `3`

**Example 2**

- Input: `nums = [5, 7, 1, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem relies on the property of the bitwise AND operation: the AND sum of a range is non-increasing as you include more elements. The minimum possible AND sum of the entire array is achieved by taking the AND of all elements in the array. If the total AND sum is greater than 0, the only possible split is the array itself (count = 1). If the total AND sum is 0, we can greedily partition the array whenever the running AND sum of a subarray reaches 0.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass to calculate the total AND and another pass to count the partitions.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the running AND sum and the partition count.
