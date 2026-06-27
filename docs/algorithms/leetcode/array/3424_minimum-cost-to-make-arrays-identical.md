# Minimum Cost to Make Arrays Identical

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3424 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-cost-to-make-arrays-identical](https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/) |

## Problem Description & Examples
### Goal
Given two integer arrays of equal length, calculate the minimum cost to transform the first array into the second. You have two operations: modifying an element at a cost of `k` per unit difference, or reordering the entire first array at a fixed cost `d`. The goal is to determine the cheaper of two strategies: transforming the array in its original order or sorting both arrays to minimize the element-wise differences before applying modifications.

### Function Contract
**Inputs**

- `arr`: A list of integers representing the initial array.
- `brr`: A list of integers representing the target array.
- `k`: An integer representing the cost to change an element by 1.
- `d`: An integer representing the fixed cost to reorder the array.

**Return value**

- An integer representing the minimum total cost to make `arr` identical to `brr`.

### Examples
**Example 1**

- Input: `arr = [1, 2, 3], brr = [3, 2, 1], k = 1, d = 5`
- Output: `5`

**Example 2**

- Input: `arr = [2, 1, 3], brr = [3, 2, 1], k = 2, d = 1`
- Output: `3`

**Example 3**

- Input: `arr = [1, 2], brr = [1, 2], k = 1, d = 10`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved by comparing two distinct strategies:
1. **Direct Transformation**: Calculate the sum of absolute differences between `arr[i]` and `brr[i]` for all `i`, multiplied by `k`.
2. **Sorted Transformation**: Sort both `arr` and `brr`. Calculate the sum of absolute differences between the sorted elements, multiplied by `k`, and add the fixed cost `d`.
The final answer is the minimum of these two values.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting requirement in the second strategy, where `N` is the length of the arrays.
- **Space Complexity**: `O(N)` to store the sorted versions of the input arrays.
