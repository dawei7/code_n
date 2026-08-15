# Minimize the Maximum Edge Weight of Graph

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/) |
| Frontend ID | 3419 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Binary Search, Depth-First Search, Breadth-First Search, Graph Theory, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A directed weighted graph contains `n` nodes numbered from `0` through `n - 1`. Each entry `[source, destination, weight]` in `edges` describes a directed edge, and several edges may connect the same ordered pair when their weights differ. You may remove any collection of edges, including none of them.

Choose the remaining edges so that every node can reach node `0` and every node has at most `threshold` outgoing edges. Among all choices satisfying both conditions, minimize the maximum weight of a retained edge. Return that minimum possible maximum, or `-1` when no valid choice exists.

### Function Contract

**Inputs**

- `n`: The number of graph nodes, where $2 \le n \le 10^5$.
- `edges`: Between $1$ and $\min(10^5, n(n-1)/2)$ directed edges `[source, destination, weight]`. Endpoints are distinct nodes, weights lie in $[1, 10^6]$, and parallel edges have distinct weights.
- `threshold`: The maximum permitted outgoing-edge count per node, where $1 \le \texttt{threshold} \le n-1$.

**Return value**

Return the smallest achievable maximum retained edge weight while all nodes can reach node `0` and the outgoing-degree bound holds. Return `-1` if those requirements cannot all be met.

### Examples

#### Example 1

- **Input:** `n = 5`, `edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]]`, `threshold = 2`
- **Output:** `1`
- **Explanation:** Removing edge `2 -> 0` leaves paths to node `0` whose heaviest retained edge has weight `1`.

#### Example 2

- **Input:** `n = 5`, `edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]]`, `threshold = 1`
- **Output:** `-1`
- **Explanation:** Node `2` cannot reach node `0`, regardless of which edges are removed.

#### Example 3

- **Input:** `n = 5`, `edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]]`, `threshold = 1`
- **Output:** `2`
- **Explanation:** Retaining the route `1 -> 2 -> 3 -> 4 -> 0` gives every node a path to `0` and uses no edge heavier than `2`.

#### Example 4

- **Input:** `n = 5`, `edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]]`, `threshold = 1`
- **Output:** `-1`
- **Explanation:** The available edges do not give node `3` a path to node `0`.
