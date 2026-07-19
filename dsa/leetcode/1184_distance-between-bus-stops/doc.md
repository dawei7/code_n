# Distance Between Bus Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1184 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distance-between-bus-stops/) |

## Problem Description

### Goal

A bus route has $n$ stops numbered from `0` through `n - 1` and arranged in a circle. For every index `i`, `distance[i]` gives the distance along the edge joining stop `i` to stop `(i + 1) % n`.

The bus can travel around the circle in either direction: clockwise or counterclockwise. Given the stops `start` and `destination`, return the shorter of the two route distances connecting them. The two directions may have equal length, and an edge is allowed to have distance zero.

### Function Contract

**Inputs**

- `distance`: A list of length $n$, where $1\le n\le10^4$ and $0\le\texttt{distance[i]}\le10^4$. Entry `distance[i]` is the distance between neighboring stops `i` and `(i + 1) % n`.
- `start`: An integer satisfying $0\le\texttt{start}<n$.
- `destination`: An integer satisfying $0\le\texttt{destination}<n$.

**Return value**

- The minimum travel distance from `start` to `destination` over the two directions around the circular route.

### Examples

**Example 1**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 1`
- Output: `1`

The direct edge has length `1`; the route around the other three edges has length `9`.

**Example 2**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 2`
- Output: `3`

The two direction lengths are `1 + 2 = 3` and `3 + 4 = 7`.

**Example 3**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 3`
- Output: `4`
