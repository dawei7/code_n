# Maximum Possible Number by Binary Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3309 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/) |

## Problem Description

### Goal

Given an array `nums` containing exactly three positive integers, write each value in its ordinary binary representation. These representations contain no leading zeros. Choose an ordering of the three original elements and concatenate their complete bit strings in that order, without separators or discarded bits.

Interpret the resulting bit string as a binary integer. Return the largest decimal value attainable over every possible ordering. Equal values still occupy separate positions in the input, although swapping identical representations does not change the concatenation.

### Function Contract

**Inputs**

- `nums`: An array of exactly three integers, each in the inclusive range from 1 through 127.

**Return value**

Return the maximum integer represented by concatenating the three binary representations in some order.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `30`

Ordering the values as `[3, 1, 2]` produces the bit string `"11110"`, whose decimal value is 30.

**Example 2**

- Input: `nums = [2, 8, 16]`
- Output: `1296`

The order `[2, 8, 16]` produces `"10100010000"`, which represents 1296.
