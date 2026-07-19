# Interval List Intersections

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 986 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sweep Line |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/interval-list-intersections/) |

## Problem Description

### Goal

You are given two lists of closed intervals, `firstList` and `secondList`. Within each list, intervals are sorted by their positions and are pairwise disjoint.

A closed interval $[a,b]$ contains every real number $x$ satisfying $a\le x\le b$. The intersection of two closed intervals is empty when they do not overlap; otherwise it is the closed interval shared by both. Return the ordered list of every intersection between the two input lists. Because endpoints are included, intervals that meet at exactly one endpoint intersect in a one-point interval such as `[5, 5]`.

### Function Contract

**Inputs**

- `firstList`: $M$ sorted, pairwise-disjoint intervals `[start_i, end_i]`.
- `secondList`: $N$ sorted, pairwise-disjoint intervals `[start_j, end_j]`.
- Each list has at most $1000$ intervals, at least one interval exists across both lists, and every endpoint satisfies $0\le\texttt{start}<\texttt{end}\le10^9$.

Let $K$ be the number of intersections returned.

**Return value**

- All non-empty closed intersections, in increasing order.

### Examples

**Example 1**

- Input: `firstList = [[0, 2], [5, 10], [13, 23], [24, 25]], secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]`
- Output: `[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]`

**Example 2**

- Input: `firstList = [[1, 3], [5, 9]], secondList = []`
- Output: `[]`
