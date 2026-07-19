# Missing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 268 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/missing-number/) |

## Problem Description
### Goal
Given an array `nums` of length `n`, its entries are unique values selected from the complete integer range `0` through `n`. Exactly one value from that range is absent, and the input order is arbitrary.

Return the missing value. It may be either endpoint `0` or `n`, not only a gap between two present values. Preserve the input and meet the intended linear-time, constant-extra-space requirement rather than constructing a full set proportional to the range. The function returns the omitted integer itself, not an index at which it should be inserted.

### Function Contract
**Inputs**

- `nums`: distinct values drawn from `[0,n]`, with one omitted

**Return value**

The omitted value.

### Examples
**Example 1**

- Input: `nums = [3,0,1]`
- Output: `2`

**Example 2**

- Input: `nums = [0,1]`
- Output: `2`

**Example 3**

- Input: `nums = [9,6,4,2,3,5,7,0,1]`
- Output: `8`
