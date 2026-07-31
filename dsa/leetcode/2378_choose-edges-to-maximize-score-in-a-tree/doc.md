# Choose Edges to Maximize Score in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2378 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/) |

## Problem Description

### Goal

A weighted tree has nodes numbered from $0$ through $n-1$ and is rooted at node `0`. For every non-root node `i`, `edges[i] = [parent, weight]` describes the edge joining `i` to its parent and that edge's possibly negative weight; `edges[0]` is the sentinel `[-1,-1]`.

Choose a set of edges whose total weight is as large as possible, subject to no two chosen edges sharing a node. Choosing no edges is allowed and has score zero. Return the maximum attainable sum of chosen edge weights.

### Function Contract

**Inputs**

- `edges`: A length-$n$ list of `[parent, weight]` pairs with $1 \le n \le 10^5$.

**Input guarantees**

- `edges[0] = [-1,-1]`.
- For every node `i` from `1` onward, its parent is a different valid node index and its edge weight lies from $-10^6$ through $10^6$.
- The described edges form a valid tree rooted at node `0`.

**Return value**

- Return the maximum sum of a set of pairwise non-adjacent tree edges.

**Adjacency semantics**

- Two edges are adjacent exactly when they share either endpoint.
- A node can therefore be incident to at most one chosen edge.

### Examples

**Example 1**

- Input: `edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]`
- Output: `11`
- Explanation: Choosing the weight-`5` edge from node `0` to node `1` and the weight-`6` edge from node `2` to node `3` gives the optimal score.

**Example 2**

- Input: `edges = [[-1,-1],[0,5],[0,-6],[0,7]]`
- Output: `7`
- Explanation: All three edges share the root, so at most one can be chosen; the weight-`7` edge is best.
