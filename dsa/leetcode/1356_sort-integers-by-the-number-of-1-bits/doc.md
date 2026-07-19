# Sort Integers by The Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1356 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) |

## Problem Description

### Goal

You are given an array `arr` of nonnegative integers. Sort its values in ascending order according to the number of `1` bits in each value's binary representation.

When two values contain the same number of `1` bits, place the numerically smaller value first. Preserve duplicate occurrences and return the fully ordered array. Thus the primary key is population count and the secondary key is the integer itself.

### Function Contract

**Inputs**

- `arr`: a nonempty array of nonnegative integers.
- Let $n$ be its length.

**Return value**

- Return all input values sorted by ascending bit count, breaking ties by ascending numeric value.

### Examples

**Example 1**

- Input: `arr = [0,1,2,3,4,5,6,7,8]`
- Output: `[0,1,2,4,8,3,5,6,7]`

**Example 2**

- Input: `arr = [1024,512,256,128,64,32,16,8,4,2,1]`
- Output: `[1,2,4,8,16,32,64,128,256,512,1024]`

**Example 3**

- Input: `arr = [2,2,1]`
- Output: `[1,2,2]`
