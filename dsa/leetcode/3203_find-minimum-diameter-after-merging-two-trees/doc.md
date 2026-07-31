# Find Minimum Diameter After Merging Two Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3203 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/) |

## Problem Description

### Goal

Two undirected trees are given separately. The first tree has nodes numbered from $0$ through $n-1$ and edges listed in `edges1`; the second has nodes numbered from $0$ through $m-1$ and edges listed in `edges2`. Each edge joins its two listed endpoints, and either tree may consist of one node with no edges.

Add exactly one edge between any chosen node of the first tree and any chosen node of the second tree. The result is again a tree. Its diameter is the number of edges on the longest simple path between any two nodes.

Return the minimum diameter achievable by choosing the two endpoints of the new edge optimally.

### Function Contract

**Inputs**

- `edges1`: The $n-1$ undirected edges of a valid tree on nodes $0$ through $n-1$.
- `edges2`: The $m-1$ undirected edges of a valid tree on nodes $0$ through $m-1$.

Both $n$ and $m$ lie in $[1,10^5]$. Every edge contains two valid node identifiers.

**Return value**

- The smallest possible diameter after adding one cross-tree edge.

Let $N=n+m$ be the total number of nodes.

### Examples

**Example 1**

- Input: `edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]`
- Output: `3`
- Explanation: Connect node `0` of the first tree to either node of the second tree.

**Example 2**

- Input: `edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]`
- Output: `5`
- Explanation: Connecting a center of each tree, such as node `0` to node `0`, minimizes the longest new cross-tree path.
