# Length of the Longest Increasing Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3288 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-the-longest-increasing-path/) |

## Problem Description

### Goal

You are given an array `coordinates` of distinct points in a two-dimensional plane and an index `k`. A path is increasing when both coordinates strictly increase between every consecutive pair: from $(x_i, y_i)$ to $(x_{i+1}, y_{i+1})$, it must satisfy $x_i < x_{i+1}$ and $y_i < y_{i+1}$.

Find the maximum number of points in an increasing path that contains the distinguished point `coordinates[k]`. The points may be chosen from anywhere in the input; their original array order does not restrict the path.

### Function Contract

**Inputs**

- `coordinates`: A list of $n$ distinct pairs `[x, y]` representing plane coordinates.
- `k`: The zero-based index of the point that every eligible path must contain.

The constraints guarantee $1 \le n \le 10^5$, $0 \le x, y \le 10^9$, and $0 \le k < n$.

**Return value**

- The length of the longest path containing `coordinates[k]` whose $x$- and $y$-coordinates are both strictly increasing.

### Examples

**Example 1**

- Input: `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]]`, `k = 1`
- Output: `3`
- Explanation: The path `[0,0] -> [2,2] -> [5,3]` is increasing in both coordinates and contains `coordinates[1]`.

**Example 2**

- Input: `coordinates = [[2,1],[7,0],[5,6]]`, `k = 2`
- Output: `2`
- Explanation: The path `[2,1] -> [5,6]` contains `coordinates[2]` and has the maximum possible length.
