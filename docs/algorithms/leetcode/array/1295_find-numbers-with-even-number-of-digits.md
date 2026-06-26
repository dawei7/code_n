# Find Numbers with Even Number of Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1295 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [find-numbers-with-even-number-of-digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) |

## Problem Description & Examples
### Goal
Count how many integers in the array have an even number of decimal digits.

### Function Contract
**Inputs**

- `nums`: array of positive integers.

**Return value**

The count of numbers whose decimal representation length is even.

### Examples
**Example 1**

- Input: `nums = [12,345,2,6,7896]`
- Output: `2`

**Example 2**

- Input: `nums = [555,901,482,1771]`
- Output: `1`

**Example 3**

- Input: `nums = [10,100,1000]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Digit counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n * d)` with string conversion, where `d` is max digit count.
- **Space Complexity**: `O(1)` aside from temporary digit strings.
