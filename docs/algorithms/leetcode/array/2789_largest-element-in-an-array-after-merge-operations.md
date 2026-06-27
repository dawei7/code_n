# Largest Element in an Array after Merge Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2789 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [largest-element-in-an-array-after-merge-operations](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, you are permitted to perform a merge operation: if two adjacent elements `nums[i]` and `nums[i+1]` satisfy `nums[i] <= nums[i+1]`, you can replace them with a single element equal to their sum. This process can be repeated any number of times. The objective is to determine the maximum possible value that any single element in the array can attain after performing an arbitrary number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers (`List[int]`).

**Return value**

- An integer representing the maximum value achievable in the array after any number of valid merge operations.

### Examples
**Example 1**

- Input: `nums = [2, 3, 7, 9, 3]`
- Output: `24`
- Explanation: Merge 2 and 3 (5), then 5 and 7 (12), then 12 and 9 (21), then 21 and 3 (24).

**Example 2**

- Input: `nums = [5, 3, 3]`
- Output: `11`
- Explanation: Merge 3 and 3 (6), then 5 and 6 (11).

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach** traversing the array from right to left. By processing backwards, we can greedily accumulate the largest possible sum for the current suffix. If the element to the left is less than or equal to the current accumulated sum, we merge them; otherwise, we reset our current "running" maximum to the new element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the current sum and the global maximum.
