# Amount of Time for Binary Tree to Be Infected

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2385 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) |

## Problem Description

### Goal

You are given the root of a nonempty binary tree whose node values are unique, together with a value `start` that occurs in the tree. At minute zero, the node carrying `start` is infected.

During every following minute, each currently uninfected node becomes infected when it is adjacent to an infected node. In a tree, adjacency includes the parent-child relationship in either direction, so infection can travel from a child to its parent as well as from a parent to either child. Return the number of minutes required until every node is infected.

### Function Contract

**Inputs**

- `root`: The root of a binary tree containing $n$ nodes, where $1 \le n \le 10^5$.
- `start`: The unique value of the node infected at minute zero.

Every node value is unique and lies between 1 and $10^5$, and `start` is guaranteed to occur in the tree.

**Return value**

- Return the number of one-minute infection steps needed to reach every node.

**Infection semantics**

- Infection spreads simultaneously across every edge leaving the currently infected region.
- A node's parent and children are all adjacent nodes.
- The starting node is already infected at minute zero.

### Examples

#### Example 1

- **Input:** `root = [1,5,3,null,4,10,6,9,2], start = 3`
- **Output:** `4`
- **Explanation:** The farthest nodes from value `3` are reached after four tree edges.

#### Example 2

- **Input:** `root = [1], start = 1`
- **Output:** `0`
- **Explanation:** The only node is infected at minute zero.
