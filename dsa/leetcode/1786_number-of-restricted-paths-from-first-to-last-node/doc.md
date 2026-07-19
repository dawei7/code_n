# Number of Restricted Paths From First to Last Node

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) |
| Frontend ID | 1786 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected, weighted, connected graph has `n` nodes labeled from `1` through `n`. Each entry `[u, v, weight]` in `edges` represents one positive-weight edge between `u` and `v`, and no node pair has more than one edge.

For any node `x`, define its distance to the last node as the minimum total edge weight of a path from `x` to node `n`. A path `[z_0, z_1, ..., z_k]` from node `1` to node `n` is restricted when this shortest-distance value strictly decreases at every step:

$$
\operatorname{dist}(z_i,n) > \operatorname{dist}(z_{i+1},n).
$$

Count all restricted paths from node `1` to node `n`, and return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: the number of nodes, where $1 \le n \le 2\cdot 10^4$.
- `edges`: between $n-1$ and $4\cdot 10^4$ entries `[u, v, weight]`, where endpoints are distinct labels from `1` through `n` and $1 \le \texttt{weight} \le 10^5$.
- The graph is connected, undirected, and simple.

Let $E=\lvert\texttt{edges}\rvert$.

**Return value**

- Return the number of paths from node `1` to node `n` whose distance-to-`n` values strictly decrease along every edge, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]`
- Output: `3`

The restricted paths are `1 → 2 → 5`, `1 → 2 → 3 → 5`, and `1 → 3 → 5`.

**Example 2**

- Input: `n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]`
- Output: `1`

Only `1 → 3 → 7` strictly descends the shortest-distance values.

**Example 3**

- Input: `n = 3, edges = [[1,2,5],[2,3,5],[1,3,20]]`
- Output: `2`

Both `1 → 2 → 3` and the heavier direct path `1 → 3` are restricted. A restricted path need not itself be a shortest path.
