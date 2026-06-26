# Largest Multiple of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1363 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Greedy, Sorting |
| Official Link | [largest-multiple-of-three](https://leetcode.com/problems/largest-multiple-of-three/) |

## Problem Description & Examples
### Goal
Given digits, choose some or all of them and arrange the chosen digits to form the largest possible integer that is divisible by `3`. Return the number as a string, or an empty string if no such positive-length number exists.

### Function Contract
**Inputs**

- `digits`: a list of digits from `0` to `9`.

**Return value**

The largest divisible-by-three number that can be formed, with no leading zeroes unless the answer is exactly `"0"`.

### Examples
**Example 1**

- Input: `digits = [8,1,9]`
- Output: `"981"`

**Example 2**

- Input: `digits = [8,6,7,1,0]`
- Output: `"8760"`

**Example 3**

- Input: `digits = [1]`
- Output: `""`

---

## Underlying Base Algorithm(s)
Digit counting and divisibility by remainder. Count digits, compute the total modulo `3`, remove the smallest possible digit set that fixes the remainder, then emit remaining digits from `9` down to `0`.

---

## Complexity Analysis
- **Time Complexity**: `O(n + 10)`
- **Space Complexity**: `O(10)` besides the output string.
