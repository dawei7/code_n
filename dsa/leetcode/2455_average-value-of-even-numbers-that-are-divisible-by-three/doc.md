# Average Value of Even Numbers That Are Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2455 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) |

## Problem Description

### Goal

You are given an integer array `nums` containing positive values. Select every element that is both even and divisible by $3$, then return the average of the selected elements.

The average is their sum divided by their count, rounded down to the nearest integer. If no array element satisfies both divisibility conditions, return `0`.

Every qualifying occurrence contributes separately, including repeated values at different indices.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

The array length is between $1$ and $1000$, inclusive, and every element is between $1$ and $1000$, inclusive.

**Return value**

- The floor of the average of all elements divisible by both $2$ and $3$, or `0` when there are none.

### Examples

**Example 1**

- Input: `nums = [1, 3, 6, 10, 12, 15]`
- Output: `9`
- Explanation: The qualifying values are `6` and `12`, whose average is $(6+12)/2=9$.

**Example 2**

- Input: `nums = [1, 2, 4, 7, 10]`
- Output: `0`
- Explanation: No element is both even and divisible by $3$.
