# Reachable Nodes With Restrictions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2368 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Union Find, Graph |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reachable-nodes-with-restrictions/) |

## Problem Description

### Goal

An undirected tree contains $n$ nodes numbered from 0 through $n-1$. Each pair
in `edges` connects two nodes, and the $n-1$ edges form one valid tree.
The distinct nodes listed in `restricted` may not be visited.

Starting at node 0, return the maximum number of nodes reachable without ever
passing through a restricted node. Node 0 is guaranteed not to be restricted;
blocking a node also makes every subtree accessible only through that node
unreachable.

### Function Contract

**Inputs**

- `n`: The number of tree nodes.
- `edges`: The $n-1$ undirected tree edges.
- `restricted`: Distinct forbidden node identifiers, excluding 0.

The constraints are $2\le n\le10^5$ and
$1\le\lvert\texttt{restricted}\rvert<n$.

**Return value**

Return the size of the unrestricted connected component containing node 0.

### Examples

#### Example 1

- **Input:** `n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]`
- **Output:** `4`

#### Example 2

- **Input:** `n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]`
- **Output:** `3`
