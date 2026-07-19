# Minimum Difference Between Largest and Smallest Value in Three Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1509 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) |

## Problem Description
### Goal

You are given an integer array `nums`. In one move, choose one element and replace it with any integer value. You may perform at most three such moves.

Minimize the difference between the largest and smallest array values after those changes, and return that minimum difference. A move may place a changed element anywhere inside the final surviving value range, so only values that remain as unavoidable extremes determine the answer.

### Function Contract
**Inputs**

Let $n$ be the length of `nums`.

- `nums`: An integer array of length $n$, where $1 \leq n \leq 10^5$ and each value lies between $-10^9$ and $10^9$, inclusive.
- Each of at most three moves may replace one chosen occurrence with any integer; equal values at different indices remain separate elements.

**Return value**

Return the minimum possible value of $\max(\texttt{nums})-\min(\texttt{nums})$ after at most three moves.

### Examples
**Example 1**

- Input: `nums = [5, 3, 2, 4]`
- Output: `0`
- Explanation: All but one of the four values can be changed to match the remaining value.

**Example 2**

- Input: `nums = [1, 5, 0, 10, 14]`
- Output: `1`
- Explanation: Three extreme values can be moved inside the interval from 0 to 1.

**Example 3**

- Input: `nums = [3, 100, 20]`
- Output: `0`
