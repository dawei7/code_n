# Valid Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 941 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-mountain-array/) |

## Problem Description

### Goal

Given an integer array `arr`, decide whether it is a valid mountain array. A mountain must contain at least three elements and have an interior peak: some index strictly between the first and last positions.

All values before that peak must be strictly increasing, and all values after it must be strictly decreasing. Thus both slopes must contain at least one step, equal adjacent values are forbidden, and neither endpoint can serve as the peak. Return whether the whole array satisfies this shape.

### Function Contract

Let $n$ be the length of `arr`, and let $a_i$ denote the value at index $i$.

**Inputs**

- `arr`: an integer array with $1 \le n \le 10^4$ and $0 \le a_i \le 10^4$ for every valid index $i$.

**Return value**

Return `true` exactly when there is an index $p$ with $0<p<n-1$ such that the values are strictly increasing through $p$ and strictly decreasing after $p$; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [2,1]`
- Output: `false`

**Example 2**

- Input: `arr = [3,5,5]`
- Output: `false`

**Example 3**

- Input: `arr = [0,3,2,1]`
- Output: `true`
