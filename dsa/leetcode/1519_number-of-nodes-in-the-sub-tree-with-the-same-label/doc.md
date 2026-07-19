# Number of Nodes in the Sub-Tree With the Same Label

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1519 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/) |

## Problem Description
### Goal

An undirected tree has `n` nodes numbered from 0 through `n - 1`, exactly `n - 1` edges, and root node 0. The character `labels[i]` is the lowercase English label assigned to node `i`.

For every node `i`, consider the rooted subtree containing `i` and all descendants reached away from node 0. Count how many nodes in that subtree have the same label as `i`, including `i` itself, and return the $n$ counts in node-number order.

### Function Contract
**Inputs**

- `n`: The node count, where $1 \leq n \leq 10^5$.
- `edges`: Exactly $n-1$ pairs `[a, b]` describing a connected, acyclic, undirected graph over nodes 0 through `n - 1`.
- `labels`: A length-$n$ string of lowercase English letters; position `i` labels node `i`.
- Node 0 defines the root and therefore every parent-descendant relationship.

**Return value**

Return an integer list `answer` of length $n$, where `answer[i]` is the number of nodes labeled `labels[i]` in the rooted subtree of node `i`.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"`
- Output: `[2,1,1,1,1,1,1]`
- Explanation: Node 0 and descendant node 2 share label `a`; every other node is the only occurrence of its own label in its subtree.

**Example 2**

- Input: `n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"`
- Output: `[4,2,1,1]`
- Explanation: Every node has label `b`, so each answer is its subtree size.

**Example 3**

- Input: `n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"`
- Output: `[3,2,1,1,1]`
