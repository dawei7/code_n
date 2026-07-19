# Duplicate Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1089 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/duplicate-zeros/) |

## Problem Description

### Goal

Given a fixed-length integer array `arr`, duplicate every occurrence of zero and shift the remaining elements to the right. The array length must not change, so values shifted beyond its original final index are discarded and never written.

Perform the modification directly in `arr` and return nothing. Nonzero values retain their relative order, each zero consumes two positions when both fit, and a duplicate that would lie just beyond the fixed boundary is truncated.

### Function Contract

**Inputs**

- `arr`: a mutable array of $n$ integers, where $1 \le n \le 10^4$ and every value is from 0 through 9.

**Return value**

- Returns `None`; after mutation, `arr` equals the first $n$ values of the sequence obtained by replacing every original zero with two zeros.

### Examples

**Example 1**

- Input: `arr = [1, 0, 2, 3, 0, 4, 5, 0]`
- Output: `[1, 0, 0, 2, 3, 0, 0, 4]`

**Example 2**

- Input: `arr = [1, 2, 3]`
- Output: `[1, 2, 3]`
