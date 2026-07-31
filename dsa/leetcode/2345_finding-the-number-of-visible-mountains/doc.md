# Finding the Number of Visible Mountains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2345 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/finding-the-number-of-visible-mountains/) |

## Problem Description

### Goal

Each pair `peaks[i] = [x_i, y_i]` describes a right-angled isosceles mountain whose peak is $(x_i,y_i)$, whose base lies on the $x$-axis, and whose ascending and descending slopes are $1$ and $-1$. Thus its base endpoints are $x_i-y_i$ and $x_i+y_i$.

A mountain is visible only when its peak lies neither inside nor on the border of any other mountain. Completely overlapping mountains hide one another, so duplicate peaks are all invisible. Return the number of mountains whose peaks remain visible under these rules.

### Function Contract

**Inputs**

- `peaks`: A list of $n$ coordinate pairs `[x_i, y_i]`.

The number of peaks and every coordinate are between $1$ and $10^5$.

**Return value**

Return the number of peaks that are not contained in or on any other mountain.

### Examples

**Example 1**

- Input: `peaks = [[2,2],[6,3],[5,4]]`
- Output: `2`

The peak at `(6,3)` lies on the side of the mountain centered at `(5,4)`, while the other two peaks are visible.

**Example 2**

- Input: `peaks = [[1,3],[1,3]]`
- Output: `0`

The two mountains completely overlap, so each peak lies within the other mountain.
