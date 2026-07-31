# Beautiful Towers I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2865 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Beautiful Towers I](https://leetcode.com/problems/beautiful-towers-i/) |

## Problem Description

### Goal

You are given an integer array `heights`, where `heights[i]` is the number of bricks initially present in the $i$-th tower of a row of $n$ consecutive towers. You may remove bricks from any towers, but you cannot add bricks or reorder the towers.

The remaining tower heights must form a mountain-shaped arrangement. Moving from left to right, the heights are non-decreasing until they reach their maximum value. That peak may occupy one tower or several consecutive towers. After the peak, the heights are non-increasing.

Among every mountain-shaped arrangement obtainable under the original per-position limits, return the maximum possible sum of its tower heights.

### Function Contract

**Inputs**

- `heights`: A list of $n$ positive integers giving the original number of bricks in each tower.

The input satisfies $1 \le n \le 10^3$ and $1 \le \texttt{heights[i]} \le 10^9$.

**Return value**

- The maximum total height of any mountain-shaped arrangement obtainable by removing bricks.

### Examples

**Example 1**

- Input: `heights = [5,3,4,1,1]`
- Output: `13`
- Explanation: `[5,3,3,1,1]` is a valid maximum-sum arrangement with its peak at index `0`.

**Example 2**

- Input: `heights = [6,5,3,9,2,7]`
- Output: `22`
- Explanation: One optimal arrangement is `[3,3,3,9,2,2]`, whose peak is at index `3`.

**Example 3**

- Input: `heights = [3,2,5,5,2,3]`
- Output: `18`
- Explanation: `[2,2,5,5,2,2]` is optimal and has a two-tower peak.
