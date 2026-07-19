# Stepping Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stepping-numbers/) |

## Problem Description

### Goal

An integer is a **stepping number** when the absolute difference between every pair of adjacent decimal digits is exactly $1$. Every single-digit integer is therefore a stepping number because it has no adjacent digit pair to violate the condition.

Given two integers `low` and `high`, return every stepping number in the inclusive range `[low, high]`. The returned list must be sorted in increasing order.

### Function Contract

**Inputs**

- `low`: The inclusive lower bound, with $0\le\texttt{low}\le\texttt{high}$.
- `high`: The inclusive upper bound, with $\texttt{high}\le2\cdot10^9$.

Let $S$ be the number of stepping numbers from $0$ through `high`, inclusive.

**Return value**

- A list of all stepping numbers in `[low, high]`, sorted in increasing order.

### Examples

**Example 1**

- Input: `low = 0`, `high = 21`
- Output: `[0,1,2,3,4,5,6,7,8,9,10,12,21]`

The two-digit results qualify because their adjacent digits differ by exactly $1$; all one-digit values qualify automatically.

**Example 2**

- Input: `low = 10`, `high = 15`
- Output: `[10,12]`
