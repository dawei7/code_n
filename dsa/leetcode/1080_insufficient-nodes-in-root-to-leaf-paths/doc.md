# Insufficient Nodes in Root to Leaf Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1080 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/) |

## Problem Description

### Goal

Given the `root` of a binary tree and an integer `limit`, delete all insufficient nodes simultaneously and return the root of the resulting tree. A leaf is a node with no children in the original tree.

A node is insufficient when every root-to-leaf path intersecting that node has a sum strictly less than `limit`. Thus, a node survives exactly when it belongs to at least one original root-to-leaf path whose complete sum is at least `limit`; if no such path exists through the root, the entire tree is removed.

### Function Contract

**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, represented in local cases as a level-order list; $1 \le n \le 5000$.
- `limit`: the minimum sufficient root-to-leaf path sum.

Node values range from $-10^5$ through $10^5$, and `limit` ranges from $-10^9$ through $10^9$.

**Return value**

- The root of the resulting binary tree after every node absent from all qualifying original root-to-leaf paths has been removed, or `null` if no node survives.

### Examples

**Example 1**

- Input: `root = [1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]`, `limit = 1`
- Output: `[1, 2, 3, 4, null, null, 7, 8, 9, null, 14]`

**Example 2**

- Input: `root = [5, 4, 8, 11, null, 17, 4, 7, 1, null, null, 5, 3]`, `limit = 22`
- Output: `[5, 4, 8, 11, null, 17, 4, 7, null, null, null, 5]`

**Example 3**

- Input: `root = [1, 2, -3, -5, null, 4, null]`, `limit = -1`
- Output: `[1, null, -3, 4]`
