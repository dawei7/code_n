# Maximum Subtree of the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3004 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subtree-of-the-same-color/) |

## Problem Description
### Goal
You are given an undirected tree with nodes numbered from 0 through $N-1$ and
rooted at node 0. Each row `[u, v]` of `edges` connects two nodes, and
`colors[i]` gives the integer color assigned to node `i`.

A rooted subtree qualifies when every node in that subtree has the same color.
Return the greatest number of nodes in any qualifying subtree.

### Function Contract
**Inputs**

- `edges`: the $N-1$ undirected tree edges
- `colors`: the length-$N$ node-color array

The contract guarantees $N=\lvert\texttt{edges}\rvert+1$,
$1\le N\le5\cdot10^4$, valid node endpoints, color values from 1 through
$10^5$, and a connected acyclic graph.

**Return value**

Return the maximum size of a rooted subtree whose nodes all share one color.

### Examples
**Example 1**

- Input: `edges = [[0,1],[0,2],[0,3]], colors = [1,1,2,3]`
- Output: `1`

The root's subtree mixes colors, while every leaf is a valid size-one subtree.

**Example 2**

- Input: `edges = [[0,1],[0,2],[0,3]], colors = [1,1,1,1]`
- Output: `4`

The entire rooted tree is monochromatic.

**Example 3**

- Input: `edges = [[0,1],[0,2],[2,3],[2,4]], colors = [1,2,3,3,3]`
- Output: `3`

Node 2 roots a three-node subtree whose color is uniformly 3.
