# Maximum Sum Obtained of Any Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1589 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Official Link | [maximum-sum-obtained-of-any-permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) |

## Problem Description & Examples
### Goal
Permute `nums` so the sum of all requested range sums is as large as possible.

### Function Contract
**Inputs**

- `nums`: the values that may be permuted.
- `requests`: inclusive index ranges.

**Return value**

The maximum possible total modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], requests = [[1, 3], [0, 1]]`
- Output: `19`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 6], requests = [[0, 1]]`
- Output: `11`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 10], requests = [[0, 2], [1, 3], [1, 1]]`
- Output: `47`

---

## Underlying Base Algorithm(s)
Use a difference array to count how many requests cover each index. Sort the
coverage counts and `nums`, then pair the largest values with the largest
coverage counts to maximize the dot product.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + r)`, where `r` is the number of requests.
- **Space Complexity**: `O(n)`.
