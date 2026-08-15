# Find the Closest Marked Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2737 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-closest-marked-node/) |

## Problem Description

### Goal

A directed, weighted graph has `n` nodes numbered from `0` to `n - 1`. Every entry `[u, v, w]` in `edges` represents a directed edge from node `u` to node `v` whose positive weight is `w`. Multiple directed edges may connect the same ordered pair of nodes.

Starting at node `s`, find the minimum total weight of a directed path that ends at any node listed in `marked`. The marked nodes are distinct, and `s` itself is not marked. Return `-1` if no marked node is reachable from the source.

### Function Contract

**Inputs**

- `n`: The number of graph nodes, where $2 \le n \le 500$.
- `edges`: Between $1$ and $10^4$ directed edges `[u, v, w]`, with $0 \le u,v < n$, $u \ne v$, and $1 \le w \le 10^6$.
- `s`: The source node, with $0 \le s < n$.
- `marked`: Between $1$ and $n-1$ distinct destination nodes; none equals `s`.

**Return value**

Return the shortest directed-path distance from `s` to any marked node, or `-1` when every marked node is unreachable.

### Examples

#### Example 1

- **Input:** `n = 4, edges = [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], s = 0, marked = [2,3]`
- **Output:** `4`
- **Explanation:** Node `2` is reached with cost `4`, while node `3` can also be reached directly with cost `4`.

#### Example 2

- **Input:** `n = 5, edges = [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]], s = 1, marked = [0,4]`
- **Output:** `3`
- **Explanation:** The path `1 -> 3 -> 4` reaches a marked node with total cost `3`; node `0` is unreachable from the source.

#### Example 3

- **Input:** `n = 4, edges = [[0,1,1],[1,2,3],[2,3,2]], s = 3, marked = [0,1]`
- **Output:** `-1`
- **Explanation:** No directed path from node `3` reaches either marked node.
