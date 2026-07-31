# Shortest Distance After Road Addition Queries II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3244 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Graph Theory, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/) |

## Problem Description

### Goal

There are $n$ cities numbered from $0$ through $n-1$. Initially, one-way roads connect each city $i$ to city $i+1$, forming a directed chain from the first city to the last.

Each query `[u, v]` permanently adds a new one-way road from `u` to `v`. After every addition, report the minimum number of roads required to travel from city $0$ to city $n-1$.

Every new road points forward, skips at least one city, and is distinct. The query intervals also never cross: for two different additions `[a, b]` and `[c, d]`, the endpoint order $a<c<b<d$ cannot occur. Intervals may instead be disjoint, nested, or share an endpoint. Return the shortest distance after each cumulative query.

### Function Contract

**Inputs**

- `n`: The number of cities, where $3 \le n \le 10^5$.
- `queries`: Between 1 and $10^5$ distinct roads `[u, v]` satisfying $0 \le u < v < n$, $v-u>1$, and the noncrossing guarantee.

**Return value**

- An array whose entry at index $i$ is the shortest distance from city $0$ to city $n-1$ after processing queries $0$ through $i$.

### Examples

**Example 1**

- Input: `n = 5, queries = [[2,4],[0,2],[0,4]]`
- Output: `[3,2,1]`

**Example 2**

- Input: `n = 4, queries = [[0,3],[0,2]]`
- Output: `[1,1]`

**Example 3**

- Input: `n = 7, queries = [[2,4],[1,5],[0,6]]`
- Output: `[5,3,1]`
