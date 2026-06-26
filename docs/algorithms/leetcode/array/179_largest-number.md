# Largest Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 179 |
| Difficulty | Medium |
| Topics | Array, String, Greedy, Sorting |
| Official Link | [largest-number](https://leetcode.com/problems/largest-number/) |

## Problem Description & Examples
### Goal
Arrange non-negative integers so that their decimal strings concatenate into the largest possible number.

### Function Contract
**Inputs**

- `nums`: a list of non-negative integers.

**Return value**

Return the largest concatenated number as a string.

### Examples
**Example 1**

- Input: `nums = [10,2]`
- Output: `"210"`

**Example 2**

- Input: `nums = [3,30,34,5,9]`
- Output: `"9534330"`

**Example 3**

- Input: `nums = [0,0]`
- Output: `"0"`

---

## Underlying Base Algorithm(s)
Sort the numbers as strings with a custom comparison: `a` should come before `b` when `a + b` is lexicographically larger than `b + a`. Concatenate the sorted strings and collapse the all-zero case to `"0"`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n * L)`, where `L` is the maximum digit length
- **Space Complexity**: `O(n * L)`
