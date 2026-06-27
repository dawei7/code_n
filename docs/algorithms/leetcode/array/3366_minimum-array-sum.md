# Minimum Array Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3366 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-array-sum](https://leetcode.com/problems/minimum-array-sum/) |

## Problem Description & Examples
### Goal
Given an array of integers, you are allowed to perform two types of operations a limited number of times: divide an element by 2 (rounding up) or subtract a fixed value `k` from an element (if the element is at least `k`). The objective is to minimize the total sum of the array after performing at most `op1` division operations and `op2` subtraction operations. Each element can be modified at most once by each type of operation.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the subtraction constant.
- `op1`: An integer representing the maximum number of division operations allowed.
- `op2`: An integer representing the maximum number of subtraction operations allowed.

**Return value**

- An integer representing the minimum possible sum of the array after applying the operations.

### Examples
**Example 1**

- Input: `nums = [2, 8, 3, 19, 3, -7, 37, 1, 9, 5], k = 1, op1 = 1, op2 = 1`
- Output: `81`

**Example 2**

- Input: `nums = [2, 4, 3], k = 3, op1 = 2, op2 = 1`
- Output: `3`

**Example 3**

- Input: `nums = [10], k = 5, op1 = 0, op2 = 1`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved using **Dynamic Programming with Memoization**. We define a state `dp(index, rem_op1, rem_op2)` which returns the minimum sum of the suffix of the array starting at `index` given the remaining operation counts. For each element, we explore four possibilities: doing nothing, performing only division, performing only subtraction, or performing both (in either order).

---

## Complexity Analysis
- **Time Complexity**: `O(n * op1 * op2)`, where `n` is the length of the array. We visit each state exactly once.
- **Space Complexity**: `O(n * op1 * op2)` to store the memoization table.
