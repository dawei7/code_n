# Minimum Time to Make Rope Colorful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1578 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) |

## Problem Description
### Goal

A rope holds $N$ balloons in a row. The character `colors[i]` gives the color of balloon `i`, and `neededTime[i]` gives the number of seconds required to remove that same balloon from the rope.

The rope is colorful when no two balloons that remain adjacent have the same color. Removing a balloon closes the gap, so balloons that were separated by removed positions may become neighbors afterward.

Choose any balloons to remove and return the minimum total removal time that makes the rope colorful. Removal times are paid only for deleted balloons; every retained balloon costs nothing.

### Function Contract
**Inputs**

- `colors`: A lowercase English string of length $N$, where $1 \le N \le 10^5$.
- `needed_time`: An integer array of the same length, where $1 \le \texttt{needed_time[i]} \le 10^4$.

**Return value**

Return the minimum total time required to leave no equal adjacent balloon colors.

### Examples
**Example 1**

- Input: `colors = "abaac", needed_time = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `colors = "abc", needed_time = [1, 2, 3]`
- Output: `0`

**Example 3**

- Input: `colors = "aabaa", needed_time = [1, 2, 3, 4, 1]`
- Output: `2`
