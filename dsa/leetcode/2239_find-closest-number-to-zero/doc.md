# Find Closest Number to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2239 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/find-closest-number-to-zero/) |

## Problem Description

### Goal

Given a nonempty integer array `nums`, choose an element whose numeric value is
closest to zero. The distance of a value $x$ from zero is its absolute value
$\lvert x\rvert$, so positive and negative values with the same magnitude are
equally close.

If exactly one array value has the smallest absolute value, return it. If
several values share that minimum distance, return the largest of those
values. In particular, when both $-x$ and $x$ are closest for positive $x$,
the required tie-break returns $x$.

### Function Contract

**Inputs**

- `nums`: A nonempty array of $n$ integers, where $1\le n\le 1000$.

Every element satisfies $-10^5\le\texttt{nums[i]}\le 10^5$.

**Return value**

Return an element of `nums` minimizing its absolute value; among equal-distance
elements, return the largest value.

### Examples

**Example 1**

- Input: `nums = [-4, -2, 1, 4, 8]`
- Output: `1`

**Example 2**

- Input: `nums = [2, -1, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [-5, -3, -9]`
- Output: `-3`
