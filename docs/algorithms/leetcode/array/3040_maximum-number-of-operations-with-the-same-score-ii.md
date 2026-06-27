# Maximum Number of Operations With the Same Score II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3040 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [maximum-number-of-operations-with-the-same-score-ii](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, perform a series of operations where each operation involves removing two elements from either the beginning, the end, or one from each end. The constraint is that every operation must result in the same sum as the first operation. The objective is to maximize the total number of operations performed.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be processed.

**Return value**

- An integer representing the maximum number of operations possible under the constraint that all operations must yield the same sum as the initial operation.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 2, 3, 4]`
- Output: `3`
- Explanation: The first operation can remove the first two elements (3+2=5). Subsequent operations must also sum to 5.

**Example 2**

- Input: `nums = [3, 2, 6, 1, 4]`
- Output: `2`
- Explanation: The first operation can remove the first and last elements (3+4=7). Subsequent operations must also sum to 7.

**Example 3**

- Input: `nums = [2, 2, 2, 2]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with Memoization. Since we need to explore different ways to remove elements (front-front, back-back, or front-back) while maintaining a fixed target sum, we define a recursive function `dp(i, j, target)` that returns the maximum operations possible for the subarray `nums[i...j]` given a required `target` sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the array. There are `O(n^2)` possible states for the subarray boundaries `(i, j)`, and each state takes constant time to compute.
- **Space Complexity**: `O(n^2)` to store the memoization table for the states.
