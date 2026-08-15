# Maximize the Number of Target Nodes After Connecting Trees I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3372 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) |

## Problem Description

### Goal

Two undirected trees contain $n$ and $m$ distinctly labelled nodes, numbered from $0$ in each tree. A node is a target of another node when their unique path uses at most $k$ edges; every node is therefore its own target. For each node `i` in the first tree, one temporary edge must connect some first-tree node to some second-tree node.

Choose that edge independently for every `i` to maximize how many nodes across the resulting connected tree are targets of `i`. Record this maximum for every first-tree node. Remove the temporary edge before considering the next node, so one query's choice never changes another query's tree.

### Function Contract

**Inputs**

- `edges1`: The $n-1$ undirected edges of the first tree on labels $0$ through $n-1$.
- `edges2`: The $m-1$ undirected edges of the second tree on labels $0$ through $m-1$.
- `k`: The inclusive target-distance limit, satisfying $0\leq k\leq1000$.

Both $n$ and $m$ are between $2$ and $1000$, and both edge lists describe valid trees.

**Return value**

- A length-$n$ list whose entry `answer[i]` is the greatest target count obtainable for node `i` by adding one temporary cross-tree edge.

### Examples

#### Example 1

- **Input:** `edges1 = [[0,1],[0,2],[2,3],[2,4]]`, `edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]`, `k = 2`
- **Output:** `[9,7,9,8,8]`

#### Example 2

- **Input:** `edges1 = [[0,1],[0,2],[0,3],[0,4]]`, `edges2 = [[0,1],[1,2],[2,3]]`, `k = 1`
- **Output:** `[6,3,3,3,3]`

#### Example 3

- **Input:** `edges1 = [[0,1]]`, `edges2 = [[0,1]]`, `k = 0`
- **Output:** `[1,1]`
- **Explanation:** No node across the added edge can be within zero edges.
