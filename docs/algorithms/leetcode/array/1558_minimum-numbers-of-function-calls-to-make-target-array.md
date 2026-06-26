# Minimum Numbers of Function Calls to Make Target Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1558 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation |
| Official Link | [minimum-numbers-of-function-calls-to-make-target-array](https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/) |

## Problem Description & Examples
### Goal
Starting from an all-zero array, form `nums` using operations that either add
`1` to one element or double every element. Minimize the number of operations.

### Function Contract
**Inputs**

- `nums`: the target array.

**Return value**

The fewest operations needed to construct `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 5]`
- Output: `5`

**Example 2**

- Input: `nums = [2, 2]`
- Output: `3`

**Example 3**

- Input: `nums = [4, 2, 5]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Work backward from `nums` to zero. Each odd bit in any number corresponds to one
single-element increment, so add the population counts of all numbers. The number
of whole-array double operations is the maximum bit length minus one among the
targets.

---

## Complexity Analysis
- **Time Complexity**: `O(n log M)`, where `M` is the maximum value.
- **Space Complexity**: `O(1)`.
