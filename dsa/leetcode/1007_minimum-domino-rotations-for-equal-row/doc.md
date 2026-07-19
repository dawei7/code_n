# Minimum Domino Rotations For Equal Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1007 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) |

## Problem Description

### Goal

A row contains $N$ dominoes. For domino `i`, `tops[i]` is the number on its top half and `bottoms[i]` is the number on its bottom half; every number is from `1` through `6`.

You may rotate any domino, swapping its top and bottom values. Return the minimum number of rotations required to make every value in `tops` the same or every value in `bottoms` the same. If neither row can be made uniform, return `-1`.

### Function Contract

**Inputs**

- `tops`: an array of $N$ top-half values, where $2\le N\le2\cdot10^4$ and every value is from `1` through `6`.
- `bottoms`: an array of $N$ bottom-half values with `bottoms.length == tops.length` and the same value range.

**Return value**

- The minimum number of domino rotations that makes either entire row equal, or `-1` when no such arrangement exists.

### Examples

**Example 1**

- Input: `tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2]`
- Output: `2`
- Explanation: Rotating the second and fourth dominoes makes every top value equal to `2`.

**Example 2**

- Input: `tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4]`
- Output: `-1`
- Explanation: No number occurs on at least one half of every domino, so neither row can become uniform.

**Example 3**

- Input: `tops = [1, 1, 1], bottoms = [2, 3, 4]`
- Output: `0`
- Explanation: The top row is already uniform.
