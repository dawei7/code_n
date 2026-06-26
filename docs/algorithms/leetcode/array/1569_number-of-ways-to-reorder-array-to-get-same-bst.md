# Number of Ways to Reorder Array to Get Same BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1569 |
| Difficulty | Hard |
| Topics | Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree |
| Official Link | [number-of-ways-to-reorder-array-to-get-same-bst](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) |

## Problem Description & Examples
### Goal
Count how many reorderings of `nums` produce the same binary search tree as the
original insertion order, excluding the original ordering itself.

### Function Contract
**Inputs**

- `nums`: a permutation of distinct integers.

**Return value**

The number of alternative reorderings modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `1`

**Example 2**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `5`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The first value is the root. Split the remaining values into those smaller and
larger than the root, recursively count valid reorderings for each side, and
multiply by the binomial coefficient that interleaves the left and right
subsequences while preserving each side's relative BST-building order.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` with precomputed combinations and recursive partitioning.
- **Space Complexity**: `O(n^2)` for the combination table.
