# Count Equal and Divisible Pairs in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2176 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [count-equal-and-divisible-pairs-in-an-array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/) |

## Problem Description & Examples
### Goal
Count index pairs `(i, j)` with `i < j` where the values are equal and the product of the two indices is divisible by `k`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: a positive divisor.

**Return value**

The number of pairs satisfying both conditions.

### Examples
**Example 1**

- Input: `nums = [3, 1, 2, 2, 2, 1, 3]`, `k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [5, 5, 5]`, `k = 2`
- Output: `3`

---

## Underlying Base Algorithm(s)
Check each pair of indices. Increment the count when the values match and `(i * j) mod k` is zero. The input limits make direct pair enumeration sufficient and least error-prone.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
