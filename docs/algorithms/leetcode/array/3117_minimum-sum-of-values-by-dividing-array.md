# Minimum Sum of Values by Dividing Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3117 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Bit Manipulation, Segment Tree, Queue |
| Official Link | [minimum-sum-of-values-by-dividing-array](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/) |

## Problem Description & Examples
### Goal
Partition an array `nums` into `m` contiguous subarrays such that the bitwise AND of each subarray matches the corresponding element in the array `andValues`. The objective is to minimize the sum of the last elements of these `m` subarrays. If no such partition exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the source array.
- `andValues`: A list of integers representing the required bitwise AND results for each partition.

**Return value**

- An integer representing the minimum possible sum of the last elements of the partitions, or -1 if the task is impossible.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 3, 2], andValues = [0, 3, 3, 2]`
- Output: `12`

**Example 2**

- Input: `nums = [2, 3, 5, 7, 7, 7, 5], andValues = [0, 7, 5]`
- Output: `17`

**Example 3**

- Input: `nums = [1, 2, 3, 4], andValues = [2]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with memoization. We define a state `(i, j, current_and)` where `i` is the current index in `nums`, `j` is the index in `andValues`, and `current_and` is the running bitwise AND of the current subarray. To optimize, we observe that `current_and` can only take values present in the prefix ANDs of `nums`. We use a dictionary to cache results and prune branches where the `current_and` cannot possibly match the target `andValues[j]`.

---

## Complexity Analysis
- **Time Complexity**: `O(n * m * log(max(nums)))`, where `n` is the length of `nums` and `m` is the length of `andValues`. The number of reachable states is limited by the bitwise properties.
- **Space Complexity**: `O(n * m)`, required for the memoization table.
