# Maximum Cost of Trip With K Highways

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2247 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Bit Manipulation, Graph Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/) |

## Problem Description

### Goal

There are `n` cities numbered from $0$ through $n-1$. Each entry
`[a, b, toll]` in `highways` describes one undirected highway between distinct
cities `a` and `b`; crossing it in either direction adds `toll` to the trip's
cost. No city pair has more than one highway.

Choose any starting city and make a trip that crosses exactly `k` highways.
Every city may be visited at most once, including the starting city, so the
trip must be a simple path of `k + 1` cities. Return the greatest total toll
among all such trips, or `-1` if no qualifying path exists.

### Function Contract

**Inputs**

- `n`: The number of cities, where $2\le n\le15$.
- `highways`: Between $1$ and $50$ distinct undirected entries `[a, b, toll]`, with valid distinct endpoints and $0\le\texttt{toll}\le100$.
- `k`: The exact number of highways the trip must cross, where $1\le k\le50$.

**Return value**

Return the maximum sum of tolls on a simple path containing exactly `k`
highways, or `-1` when no such path exists.

### Examples

**Example 1**

- Input: `n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], k = 3`
- Output: `17`

**Example 2**

- Input: `n = 4, highways = [[0,1,3],[2,3,2]], k = 2`
- Output: `-1`

**Example 3**

- Input: `n = 3, highways = [[0,1,0],[1,2,0]], k = 2`
- Output: `0`
