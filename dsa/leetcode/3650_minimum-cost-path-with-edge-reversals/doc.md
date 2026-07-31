# Minimum Cost Path with Edge Reversals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3650 |
| Difficulty | Medium |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/) |

## Problem Description
### Goal

You are given a directed weighted graph on nodes `0` through `n - 1`. Each row `[u, v, w]` in `edges` is an ordinary directed edge from `u` to `v` with traversal cost `w`.

Every node has a switch usable at most once. After arriving at node `u`, you may use that node's unused switch on one incoming edge `v -> u`, temporarily reverse it to `u -> v`, and immediately traverse it for cost `2 * w`. The reversal applies only to that move; it does not permanently change the graph.

Find the minimum total cost of traveling from node `0` to node `n - 1`. Return `-1` when no valid route exists.

### Function Contract
**Inputs**

- `n`: The number of nodes, with $2\le n\le5\cdot10^4$.
- `edges`: Between 1 and $10^5$ rows `[u, v, w]`, where `u` and `v` are valid node labels and $1\le w\le1000$.

**Return value**

Return the minimum route cost from node `0` to node `n - 1`, including doubled costs for reversed traversals, or `-1` if the destination is unreachable.

### Examples
**Example 1**

- Input: `n = 4`, `edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]`
- Output: `5`
- Explanation: Traverse `0 -> 1` for 3, then reverse `3 -> 1` at node 1 and immediately traverse to node 3 for 2.

**Example 2**

- Input: `n = 4`, `edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]`
- Output: `3`
- Explanation: The ordinary route `0 -> 2 -> 1 -> 3` costs 3 and needs no switch.
