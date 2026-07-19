# Minimum Swaps to Group All 1's Together

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1151 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) |

## Problem Description

### Goal

Given a binary array `data`, group every `1` present in the array into one contiguous block located anywhere in the array. A swap may exchange the values at any two positions; the positions do not need to be adjacent.

Return the minimum number of swaps required. The relative order of equal values is irrelevant, and the array may already satisfy the condition. In particular, zero or one occurrence of `1` is already grouped and requires no swap.

### Function Contract

**Inputs**

- `data`: a binary array of length $n$, where $1 \le n \le 10^5$ and every element is `0` or `1`.
- Let $k$ be the total number of `1` values in `data`.

**Return value**

The fewest arbitrary-position swaps needed to place all $k$ ones in one contiguous block.

### Examples

**Example 1**

- Input: `data = [1,0,1,0,1]`
- Output: `1`

**Example 2**

- Input: `data = [0,0,0,1,0]`
- Output: `0`

**Example 3**

- Input: `data = [1,0,1,0,1,0,0,1,1,0,1]`
- Output: `3`
