# Number of Ways to Arrive at Destination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1976 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Graph Theory, Topological Sort, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) |

## Problem Description
### Goal
A connected city graph has `n` intersections labeled from `0` through
`n - 1`. Each entry `[u, v, time]` in `roads` represents one bidirectional
road whose positive travel time is the same in both directions. No unordered
pair of intersections has more than one road.

Count the distinct routes from intersection `0` to intersection `n - 1` whose
total travel time is as small as possible. Return that count modulo
$10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of intersections $V$, where $1 \le V \le 200$.
- `roads`: $E$ unique undirected weighted edges, where
  $V-1 \le E \le V(V-1)/2$.
- Every travel time is an integer from `1` through $10^9$, and the graph is
  connected.

**Return value**

- The number of shortest routes from vertex `0` to vertex `V - 1`, reduced
  modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 7, roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]`
- Output: `4`

**Example 2**

- Input: `n = 2, roads = [[1, 0, 10]]`
- Output: `1`

**Example 3**

- Input: `n = 3, roads = [[0, 1, 1], [1, 2, 1], [0, 2, 2]]`
- Output: `2`
