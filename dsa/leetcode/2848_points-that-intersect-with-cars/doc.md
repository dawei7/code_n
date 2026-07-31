# Points That Intersect With Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2848 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## Problem Description

### Goal

A 0-indexed array `nums` describes cars parked along a number line. Each entry `nums[i] = [start_i, end_i]` gives the starting and ending coordinates occupied by one car.

Both endpoints belong to the car's occupied range, so every integer coordinate from `start_i` through `end_i` is covered. Return the number of distinct integer points covered by at least one part of any car. A point shared by several cars is counted only once.

### Function Contract

**Inputs**

- `nums`: A list of inclusive integer intervals `[start, end]`, one per car.

The constraints are $1\le\lvert\texttt{nums}\rvert\le100$ and $1\le\texttt{start}_i\le\texttt{end}_i\le100$.

**Return value**

- The number of distinct integer coordinates contained in at least one interval.

### Examples

**Example 1**

- Input: `nums = [[3,6],[1,5],[4,7]]`
- Output: `7`
- Explanation: Every integer point from `1` through `7` is covered.

**Example 2**

- Input: `nums = [[1,3],[5,8]]`
- Output: `7`
- Explanation: The covered points are `1`, `2`, `3`, `5`, `6`, `7`, and `8`.
