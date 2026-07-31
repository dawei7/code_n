# Maximize the Number of Target Nodes After Connecting Trees II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3373 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/) |

## Problem Description

### Goal

Two undirected trees contain $n$ and $m$ nodes, respectively, with the labels in each tree beginning at $0$. A node `u` is a target of `v` exactly when their unique path contains an even number of edges. Consequently, every node is a target of itself, while adjacent nodes are not targets of one another.

For each node `i` in the first tree, add one temporary edge between any first-tree node and any second-tree node. Choose its endpoints to maximize the total number of nodes that are targets of `i`, and record that maximum as `answer[i]`. The queries are independent: remove the added edge before processing the next first-tree node.

### Function Contract

**Inputs**

- `edges1`: The $n-1$ undirected edges of the first tree on labels $0$ through $n-1$.
- `edges2`: The $m-1$ undirected edges of the second tree on labels $0$ through $m-1$.

Both $n$ and $m$ are between $2$ and $10^5$, inclusive, and each edge list describes a valid tree.

**Return value**

- A length-$n$ list where `answer[i]` is the greatest even-distance target count obtainable for first-tree node `i` after adding one temporary cross-tree edge.

### Examples

**Example 1**

- Input: `edges1 = [[0,1],[0,2],[2,3],[2,4]]`, `edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]`
- Output: `[8,7,7,8,8]`

**Example 2**

- Input: `edges1 = [[0,1],[0,2],[0,3],[0,4]]`, `edges2 = [[0,1],[1,2],[2,3]]`
- Output: `[3,6,6,6,6]`

**Example 3**

- Input: `edges1 = [[0,1]]`, `edges2 = [[0,1]]`
- Output: `[2,2]`
- Explanation: Each tree has one node in each bipartition class, so every query can target one node from each tree.
