# Remove Max Number of Edges to Keep Graph Fully Traversable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1579 |
| Difficulty | Hard |
| Topics | Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) |

## Problem Description
### Goal

An undirected graph has $N$ nodes numbered from $1$ through $N$. Each edge is represented as `[type, u, v]` and can be used by Alice, Bob, or both: type 1 is Alice-only, type 2 is Bob-only, and type 3 is shared by both users.

Alice and Bob traverse the same node set but may use only the edge types available to them. The graph is fully traversable for a user when that user can travel between every pair of nodes using allowed retained edges.

Remove as many edges as possible while leaving the graph fully traversable for both Alice and Bob. Return that maximum removable count, or `-1` if no retained subset can connect the graph for both users.

### Function Contract
**Inputs**

- `n`: The number of nodes, with nodes labeled $1$ through $N$.
- `edges`: A list of distinct undirected edges `[type, u, v]`, where `type` is $1$, $2$, or $3$ and $1 \le u < v \le N$.
- $1 \le N \le 10^5$, and the edge count is at most $10^5$.

**Return value**

Return the maximum number of removable edges that preserves full traversal for both users, or `-1` when this is impossible.

### Examples
**Example 1**

- Input: `n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]`
- Output: `2`

**Example 2**

- Input: `n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]`
- Output: `0`

**Example 3**

- Input: `n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]`
- Output: `-1`
