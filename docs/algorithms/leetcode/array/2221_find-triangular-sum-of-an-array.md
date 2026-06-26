# Find Triangular Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2221 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation, Combinatorics, Number Theory |
| Official Link | [find-triangular-sum-of-an-array](https://leetcode.com/problems/find-triangular-sum-of-an-array/) |

## Problem Description & Examples
### Goal
Repeatedly replace an array by the adjacent pair sums modulo `10` until one digit remains. Return that final triangular sum.

### Function Contract
**Inputs**

- `nums`: an array of decimal digits.

**Return value**

The single remaining digit.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `8`

**Example 2**

- Input: `nums = [5]`
- Output: `5`

**Example 3**

- Input: `nums = [9, 9]`
- Output: `8`

---

## Underlying Base Algorithm(s)
Simulate each shrinking row in place. For a current length `len`, set `nums[i] = (nums[i] + nums[i + 1]) mod 10` for `0 <= i < len - 1`, then reduce the active length. The first position contains the answer after `n - 1` rounds.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)` auxiliary space when modifying the input
