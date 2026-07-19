# Minimum Jumps to Reach Home

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1654 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-home/) |

## Problem Description
### Goal
A bug begins at position 0 on the nonnegative x-axis and wants to reach its home at position `x`. A forward jump always moves exactly `a` positions, while a backward jump always moves exactly `b` positions. The bug may pass beyond its home, but it may never land at a negative position or at any position listed in `forbidden`.

Two backward jumps may not occur consecutively; a forward jump resets that restriction. Return the fewest jumps that can land exactly on `x`, or `-1` when no legal route exists.

### Function Contract
**Inputs**

- `forbidden`: between 1 and 1000 distinct blocked positive positions, each at most 2000; `x` is not blocked.
- `a`: the forward jump length, where $1 \le a \le 2000$.
- `b`: the backward jump length, where $1 \le b \le 2000$.
- `x`: the target position, where $0 \le x \le 2000$.

Let $f=\lvert\texttt{forbidden}\rvert$, $M=\max(x,\max(\texttt{forbidden}))$, and $L=M+a+b$.

**Return value**

Return the minimum number of legal jumps from 0 to `x`, or `-1` if none exists.

### Examples
**Example 1**

- Input: `forbidden = [14, 4, 18, 1, 15], a = 3, b = 15, x = 9`
- Output: `3`

Three forward jumps follow `0 -> 3 -> 6 -> 9`.

**Example 2**

- Input: `forbidden = [8, 3, 16, 6, 12, 20], a = 15, b = 13, x = 11`
- Output: `-1`

**Example 3**

- Input: `forbidden = [1, 6, 2, 14, 5, 17, 4], a = 16, b = 9, x = 7`
- Output: `2`

One forward and one backward jump follow `0 -> 16 -> 7`.
