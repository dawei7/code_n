# Flower Planting With No Adjacent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1042 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/flower-planting-with-no-adjacent/) |

## Problem Description

### Goal

There are $N$ gardens labeled from $1$ through $N$. Each pair `paths[i] = [x_i, y_i]` describes a bidirectional path connecting gardens $x_i$ and $y_i$. Every garden has at most three paths entering or leaving it.

Plant exactly one of four flower types in each garden. Any two gardens joined directly by a path must receive different flower types.

Return any valid assignment as an array `answer` of length $N$, where `answer[i]` is the type planted in garden $i+1$. Flower types are represented by `1`, `2`, `3`, and `4`, and a valid assignment is guaranteed to exist.

### Function Contract

**Inputs**

- `n`: the number $N$ of gardens, where $1 \le N \le 10^4$.
- `paths`: the $P$ bidirectional paths, where $0 \le P \le 2\cdot10^4$; every entry contains two distinct labels in $[1,N]$, and each garden has degree at most three.

**Return value**

- Any length-$N$ array of flower types from `1` through `4` such that connected gardens have different types.

### Examples

**Example 1**

- Input: `n = 3, paths = [[1,2],[2,3],[3,1]]`
- Output: `[1,2,3]`
- Explanation: Each pair of gardens in the triangle receives different flower types. Other valid assignments are also accepted.

**Example 2**

- Input: `n = 4, paths = [[1,2],[3,4]]`
- Output: `[1,2,1,2]`

**Example 3**

- Input: `n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]`
- Output: `[1,2,3,4]`
