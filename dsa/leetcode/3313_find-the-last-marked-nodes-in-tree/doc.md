# Find the Last Marked Nodes in Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3313 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/) |

## Problem Description

### Goal

An undirected tree contains $n$ vertices numbered from $0$ through $n-1$. Initially every vertex is unmarked. After one vertex is marked at time $t=0$, each subsequent second marks every still-unmarked vertex that is adjacent to at least one already marked vertex. Thus marking spreads outward across one tree edge per second.

Consider starting this process separately from every vertex `i`. Return an array `nodes` where `nodes[i]` is a vertex marked during the final second when `i` is the initial vertex. Several vertices can be marked last at the same time; in that situation, any one of those tied vertices is a valid answer for `nodes[i]`.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of a valid tree, with `edges[j] = [u, v]` connecting vertices `u` and `v`. The constraints are $2\leq n\leq10^5$ and $0\leq u,v<n$.

**Return value**

Return an integer array of length $n$. For each starting vertex `i`, the value at index `i` must be any vertex whose distance from `i` is maximum.

### Examples

#### Example 1

- **Input:** `edges = [[0, 1], [0, 2]]`
- **Output:** `[2, 2, 1]`

Starting from 0, vertices 1 and 2 tie for last, so either is allowed. Starting from either leaf, the other leaf is marked last.

#### Example 2

- **Input:** `edges = [[0, 1]]`
- **Output:** `[1, 0]`

#### Example 3

- **Input:** `edges = [[0, 1], [0, 2], [2, 3], [2, 4]]`
- **Output:** `[3, 3, 1, 1, 1]`

For example, starting at vertex 2 leaves vertex 1 for the final second, while starting at vertex 0 may validly choose either vertex 3 or 4.
