# Power of Two

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `bit_02` |
| Frontend ID | 231 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation, Recursion |
| Official Link | [power-of-two](https://leetcode.com/problems/power-of-two/) |

## Problem Description & Examples
### Goal
Return True iff the input n is a power of two.
A single bitwise trick covers the whole problem:
n is a power of two iff n > 0 and (n & (n - 1)) == 0.
Why? Powers of two have exactly one bit set, so
n - 1 clears that bit and only that bit, and the
AND with n is 0. O(1).
Source: https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/

### Function Contract
**Inputs**

- `n`: non-negative integer.

**Return value**

True iff n is a power of two (1, 2, 4, 8, ...).

### Examples
**Example 1**

- Input: `n = 1`
- Output: `True`

**Example 2**

- Input: `n = 16`
- Output: `True`

**Example 3**

- Input: `n = 6`
- Output: `False`

---

## Underlying Base Algorithm(s)
bit_manipulation

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `TODO`
