# Smallest Absent Positive Greater Than Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3678 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-absent-positive-greater-than-average/) |

## Problem Description
### Goal

Given an integer array `nums`, compute its arithmetic average as the sum of all elements divided by the array length. Find the smallest positive integer that is both strictly greater than this average and absent from `nums`.

The comparison uses the exact average rather than a rounded value. Array elements may be negative or repeated, while the returned value must always be positive.

### Function Contract

**Inputs**

- `nums`: a non-empty list of $n$ integers, where $1\le n\le100$ and $-100\le\texttt{nums[i]}\le100$.

**Return value**

Return the smallest positive integer not appearing in `nums` whose value is strictly greater than the array average.

### Examples

**Example 1**

- Input: `nums = [3, 5]`
- Output: `6`

The average is 4. Integer 5 is greater than the average but is present, so 6 is the first valid value.

**Example 2**

- Input: `nums = [-1, 1, 2]`
- Output: `3`

The average is $2/3$; positive integers 1 and 2 are present, making 3 the first absent choice.

**Example 3**

- Input: `nums = [4, -1]`
- Output: `2`

The average is $3/2$, and 2 is absent and strictly larger.
