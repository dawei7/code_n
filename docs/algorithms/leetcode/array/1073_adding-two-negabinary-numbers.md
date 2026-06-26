# Adding Two Negabinary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1073 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [adding-two-negabinary-numbers](https://leetcode.com/problems/adding-two-negabinary-numbers/) |

## Problem Description & Examples
### Goal
Given two arrays of bits that encode non-negative integers in base `-2`, return the bit array for their sum in the same base. The answer must not contain leading zeroes unless the value itself is zero.

### Function Contract
**Inputs**

- `arr1`: most-significant-bit-first representation of a value in base `-2`.
- `arr2`: most-significant-bit-first representation of another value in base `-2`.

**Return value**

A most-significant-bit-first base `-2` representation of the sum.

### Examples
**Example 1**

- Input: `arr1 = [1,1,1,1,1]`, `arr2 = [1,0,1]`
- Output: `[1,0,0,0,0]`

**Example 2**

- Input: `arr1 = [0]`, `arr2 = [0]`
- Output: `[0]`

**Example 3**

- Input: `arr1 = [1]`, `arr2 = [1]`
- Output: `[1,1,0]`

---

## Underlying Base Algorithm(s)
Base conversion, digit-by-digit addition, carry normalization.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)` for the output digits.
