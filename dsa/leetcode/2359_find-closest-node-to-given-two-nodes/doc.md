# Find Closest Node to Given Two Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2359 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Graph |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) |

## Problem Description

### Goal

A directed graph contains $n$ nodes numbered from 0 through $n-1$, and every
node has at most one outgoing edge. The array `edges` represents that edge:
`edges[i]` is the destination from node $i$, while `-1` means that $i$ has no
outgoing edge. The graph may contain directed cycles.

Given starting nodes `node1` and `node2`, find a node reachable from both that
minimizes the larger of its two directed-path distances from the starts. If
several common reachable nodes have the same minimum maximum distance, return
the smallest node index. Return `-1` when the two reachable sets do not
intersect.

### Function Contract

**Inputs**

- `edges`: A list of $n$ integers encoding at most one outgoing edge per node.
- `node1`: The first starting node.
- `node2`: The second starting node.

The constraints are $2 \le n \le 10^5$,
$-1 \le \texttt{edges[i]} < n$, `edges[i] != i`, and
$0 \le \texttt{node1},\texttt{node2} < n$.

**Return value**

Return the smallest-index common reachable node minimizing the maximum of its
two directed distances, or `-1` if no node is reachable from both starts.

### Examples

#### Example 1

- **Input:** `edges = [2,2,3,-1], node1 = 0, node2 = 1`
- **Output:** `2`

Both starts reach node 2 in one step.

#### Example 2

- **Input:** `edges = [1,2,-1], node1 = 0, node2 = 2`
- **Output:** `2`

Node 2 is two steps from node 0 and zero steps from itself.
