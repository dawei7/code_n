# Shortest Distance After Road Addition Queries I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3243 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/) |

## Problem Description

### Goal

There are $n$ cities numbered from $0$ through $n-1$. Initially, a one-way road leads from every city $i$ to city $i+1$, so the cities form a directed chain.

Each entry `[u, v]` in `queries` adds a new one-way road from `u` to `v`. Roads remain available after later queries. Immediately after every addition, determine the minimum number of roads needed to travel from city $0$ to city $n-1$.

Return these shortest distances in query order. Every added road skips at least one intermediate city, points toward a larger-numbered city, and is not repeated.

### Function Contract

**Inputs**

- `n`: The number of cities, where $3 \le n \le 500$.
- `queries`: Between 1 and 500 distinct forward road additions `[u, v]` satisfying $0 \le u < v < n$ and $v-u>1$.

**Return value**

- An array whose entry at index $i$ is the shortest distance from city $0$ to city $n-1$ after applying queries $0$ through $i$.

### Examples

**Example 1**

- Input: `n = 5, queries = [[2,4],[0,2],[0,4]]`
- Output: `[3,2,1]`

**Example 2**

- Input: `n = 4, queries = [[0,3],[0,2]]`
- Output: `[1,1]`

**Example 3**

- Input: `n = 7, queries = [[0,2],[2,6],[1,5],[0,4]]`
- Output: `[5,2,2,2]`
