# Beautiful Towers II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2866 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Beautiful Towers II](https://leetcode.com/problems/beautiful-towers-ii/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `maxHeights` of length $n$. Build one tower at every coordinate from `0` through `n - 1`, choosing the height of tower `i` between $1$ and `maxHeights[i]`, inclusive.

The chosen sequence `heights` must be a mountain. There must be some peak index `i` such that the sequence is non-decreasing from coordinate `0` through `i` and non-increasing from `i` through `n - 1`. Equal neighboring heights are allowed, so a valid mountain may have a flat peak spanning several towers.

Return the maximum possible sum of the chosen tower heights among all configurations that satisfy both the per-coordinate limits and the mountain condition.

### Function Contract

**Inputs**

- `maxHeights`: A list of $n$ positive integers, where `maxHeights[i]` is the inclusive upper bound for tower `i`.

The input satisfies $1 \le n \le 10^5$ and $1 \le \texttt{maxHeights[i]} \le 10^9$.

**Return value**

- The maximum possible sum of all tower heights in a beautiful configuration.

### Examples

**Example 1**

- Input: `maxHeights = [5,3,4,1,1]`
- Output: `13`
- Explanation: `[5,3,3,1,1]` respects every limit and is a mountain with peak index `0`.

**Example 2**

- Input: `maxHeights = [6,5,3,9,2,7]`
- Output: `22`
- Explanation: `[3,3,3,9,2,2]` is an optimal configuration with peak index `3`.

**Example 3**

- Input: `maxHeights = [3,2,5,5,2,3]`
- Output: `18`
- Explanation: `[2,2,5,5,2,2]` is optimal; either index `2` or index `3` may be regarded as its peak.
