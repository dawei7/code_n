# Find the Longest Valid Obstacle Course at Each Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1964 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Binary Indexed Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) |

## Problem Description
### Goal
The array `obstacles` lists obstacle heights in their original order. For
every index `i`, choose a subsequence from indices zero through `i` that must
include the obstacle at `i`.

The chosen indices must retain their array order, and their heights must be
non-decreasing: every height is at least the one immediately before it. Return
an array whose value at `i` is the greatest possible length of such an
obstacle course ending exactly at `i`.

### Function Contract
**Inputs**

- `obstacles`: a list of $N$ positive heights, where $1\le N\le10^5$ and each
  height is at most $10^7$.

**Return value**

- A length-$N$ list where position `i` contains the longest non-decreasing
  subsequence length that ends at `obstacles[i]`.

### Examples
**Example 1**

- Input: `obstacles = [1, 2, 3, 2]`
- Output: `[1, 2, 3, 3]`

**Example 2**

- Input: `obstacles = [2, 2, 1]`
- Output: `[1, 2, 1]`

**Example 3**

- Input: `obstacles = [3, 1, 5, 6, 4, 2]`
- Output: `[1, 1, 2, 3, 2, 2]`
