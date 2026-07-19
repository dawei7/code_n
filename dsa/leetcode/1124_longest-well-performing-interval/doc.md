# Longest Well-Performing Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1124 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-well-performing-interval/) |

## Problem Description

### Goal

The array `hours` records how many hours one employee worked on each consecutive day. A day is a tiring day if and only if the employee worked strictly more than `8` hours on that day; every other day, including a day of exactly `8` hours, is non-tiring.

A well-performing interval is a contiguous interval of days in which the number of tiring days is strictly larger than the number of non-tiring days. Among all intervals in `hours`, return the greatest possible length of a well-performing interval. Return `0` when no interval satisfies the strict majority condition.

### Function Contract

**Inputs**

- `hours`: an integer array of length $n$, where $1 \le n \le 10^4$ and $0 \le \texttt{hours[i]} \le 16$.

**Return value**

The length of the longest contiguous interval containing strictly more tiring days than non-tiring days.

### Examples

**Example 1**

- Input: `hours = [9,9,6,0,6,6,9]`
- Output: `3`
- Explanation: `[9,9,6]` is a well-performing interval of maximum length.

**Example 2**

- Input: `hours = [6,6,6]`
- Output: `0`
