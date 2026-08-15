# Alternating Groups II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alternating-groups-ii/) |

## Problem Description

### Goal

`colors` describes a circular sequence of red and blue tiles, where `0` is red and `1` is blue. The first and last array positions are adjacent.

For every possible circular block of exactly `k` consecutive tiles, determine whether adjacent tiles alternate throughout the block. Equivalently, every tile except the two endpoints must differ from both of its neighbors inside the block.

Return the number of alternating length-`k` blocks. Blocks with different circular starting positions are counted separately.

### Function Contract

**Inputs**

- `colors`: A binary color array with $3 \le \lvert\texttt{colors}\rvert \le 10^5$.
- `k`: The required group length, with $3 \le k \le \lvert\texttt{colors}\rvert$.

Let $n=\lvert\texttt{colors}\rvert$.

**Return value**

- The number of the $n$ circular length-`k` blocks whose adjacent colors all differ.

### Examples

#### Example 1

- **Input:** `colors = [0,1,0,1,0], k = 3`
- **Output:** `3`

#### Example 2

- **Input:** `colors = [0,1,0,0,1,0,1], k = 6`
- **Output:** `2`

#### Example 3

- **Input:** `colors = [1,1,0,1], k = 4`
- **Output:** `0`
