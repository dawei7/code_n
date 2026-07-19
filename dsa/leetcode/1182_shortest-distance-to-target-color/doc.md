# Shortest Distance to Target Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1182 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-to-target-color/) |

## Problem Description

### Goal

An array `colors` describes a row of items, and every item has one of the three colors `1`, `2`, or `3`. You must answer a collection of independent queries about this fixed row without modifying it.

Each query is `[i, c]`: begin at index `i` and find the shortest distance to any array index whose value is the target color `c`. The distance between indices $i$ and $j$ is $\lvert i-j\rvert$, so the answer is zero when `colors[i] == c`. Return one answer per query in the original order, using `-1` if the requested color does not occur anywhere in `colors`.

### Function Contract

**Inputs**

- `colors`: A list of length $n$, where $1\le n\le 5\cdot 10^4$ and every value is `1`, `2`, or `3`.
- `queries`: A list of $q$ pairs `[i, c]`, where $1\le q\le 5\cdot 10^4$, $0\le i<n$, and `c` is `1`, `2`, or `3`.

**Return value**

- A list of $q$ integers. Entry $k$ is the minimum $\lvert i-j\rvert$ for query `queries[k] = [i, c]` over indices satisfying `colors[j] == c`, or `-1` when no such index exists.

### Examples

**Example 1**

- Input: `colors = [1,1,2,1,3,2,2,3,3]`, `queries = [[1,3],[2,2],[6,1]]`
- Output: `[3,0,3]`

For the first query, the nearest `3` to index `1` is at index `4`. The second query already points to color `2`, and the nearest `1` to index `6` is at index `3`.

**Example 2**

- Input: `colors = [1,2]`, `queries = [[0,3]]`
- Output: `[-1]`

Color `3` does not appear in the array.
