# Relocate Marbles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2766 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Relocate Marbles](https://leetcode.com/problems/relocate-marbles/) |

## Problem Description

### Goal

A 0-indexed integer array `nums` gives the initial positions of a collection of marbles. Several marbles may occupy the same integer position. Two equal-length 0-indexed arrays, `moveFrom` and `moveTo`, describe a sequence of relocation steps.

At step $i$, move every marble currently at `moveFrom[i]` to `moveTo[i]`. The source is guaranteed to contain at least one marble when that step occurs, and the source and destination may be equal. After performing every step in order, return all positions occupied by at least one marble, sorted in ascending order.

### Function Contract

**Inputs**

- `nums`: An array of $n$ initial marble positions, where $1 \leq n \leq 10^5$.
- `moveFrom`: An array of $m$ source positions, where $1 \leq m \leq 10^5$.
- `moveTo`: An array of $m$ destination positions.

Every coordinate in the three arrays is between $1$ and $10^9$, inclusive. Each `moveFrom[i]` is occupied immediately before operation $i$.

**Return value**

Return the distinct occupied positions after all moves, sorted in ascending order.

### Examples

**Example 1**

- Input: `nums = [1,6,7,8]`, `moveFrom = [1,7,2]`, `moveTo = [2,9,5]`
- Output: `[5,6,8,9]`
- Explanation: The occupied-position set changes from `{1,6,7,8}` to `{2,6,7,8}`, then `{2,6,8,9}`, and finally `{5,6,8,9}`.

**Example 2**

- Input: `nums = [1,1,3,3]`, `moveFrom = [1,3]`, `moveTo = [2,2]`
- Output: `[2]`
- Explanation: Both groups of marbles move to position `2`, leaving a single occupied position.
