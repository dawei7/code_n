# Minimum Number of Groups to Create a Valid Assignment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2910 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) |

## Problem Description

### Goal

A collection of numbered balls is given by the array `balls`. Place every ball into exactly one box. Each box must be homogeneous: all balls inside it have the same value. Balls carrying the same value may be split among several boxes.

The distribution must also be nearly balanced across the entire collection of boxes. The largest box may contain at most one ball more than the smallest box, regardless of which values their balls carry. Return the minimum number of boxes needed to satisfy both rules.

### Function Contract

**Inputs**

- `balls`: An integer array of length $n$, where $1\le n\le 10^5$ and $1\le\texttt{balls}[i]\le 10^9$.

Let $u$ be the number of distinct values in `balls`.

**Return value**

Return the fewest boxes in a valid assignment of every ball.

### Examples

#### Example 1

- **Input:** `balls = [3, 2, 3, 2, 3]`
- **Output:** `2`
- **Explanation:** Use boxes `[3, 3, 3]` and `[2, 2]`. Their sizes differ by one.

#### Example 2

- **Input:** `balls = [10, 10, 10, 3, 1, 1]`
- **Output:** `4`
- **Explanation:** Boxes `[10]`, `[10, 10]`, `[3]`, and `[1, 1]` have sizes one or two. Three boxes cannot satisfy both homogeneity and global balance.
