# Reorder Routes to Make All Paths Lead to the City Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1466 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) |

## Problem Description
### Goal

There are `n` cities numbered from `0` through `n - 1` and exactly `n - 1` roads. Ignoring road directions, there is exactly one route between every pair of cities, so the road network forms a tree. Each narrow road has been assigned one direction: `connections[i] = [a, b]` describes a road that currently allows travel from city `a` to city `b`.

City `0` is the capital. Reverse the direction of as few roads as possible so that every city has a directed route to city `0`. The tree structure guarantees that such an orientation can be obtained. Return the minimum number of roads whose directions must change.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 5 \cdot 10^4$.
- `connections`: exactly $n-1$ directed pairs `[a, b]`. Each endpoint lies in $[0,n-1]$, the endpoints of a road are different, and the undirected versions of the roads form one tree.

**Return value**

Return the minimum number of directed roads that must be reversed so every city can travel along road directions to city `0`.

### Examples
**Example 1**

- Input: `n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]`
- Output: `3`
- Explanation: The roads `0 -> 1`, `1 -> 3`, and `4 -> 5` point away from the capital along their unique tree paths and must be reversed.

**Example 2**

- Input: `n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]`
- Output: `2`

**Example 3**

- Input: `n = 3, connections = [[1,0],[2,0]]`
- Output: `0`
- Explanation: Both non-capital cities already have a direct road to city `0`.
