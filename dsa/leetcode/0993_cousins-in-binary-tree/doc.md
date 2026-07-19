# Cousins in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 993 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/cousins-in-binary-tree/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values are unique, together with the values `x` and `y` of two different nodes that both occur in the tree. Two nodes are cousins when they have the same depth but different parents.

The root has depth $0$, and every child of a node at depth $d$ has depth $d+1$. Return `true` when the nodes identified by `x` and `y` satisfy both cousin conditions, and return `false` otherwise.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes, where $2\le N\le100$; every node value is unique and lies from $1$ through $100$.
- `x` and `y`: different values of nodes present in the tree.

**Return value**

- `true` if the two selected nodes have the same depth and different parents; otherwise, `false`.

### Examples

**Example 1**

- Input: `root = [1, 2, 3, 4], x = 4, y = 3`
- Output: `false`
- Explanation: Node $4$ is deeper than node $3$.

**Example 2**

- Input: `root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4`
- Output: `true`
- Explanation: The selected nodes share a depth and have different parents.

**Example 3**

- Input: `root = [1, 2, 3, null, 4], x = 2, y = 3`
- Output: `false`
- Explanation: Nodes $2$ and $3$ are siblings, so their parent is the same.
