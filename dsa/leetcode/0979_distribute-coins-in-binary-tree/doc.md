# Distribute Coins in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 979 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/distribute-coins-in-binary-tree/) |

## Problem Description

### Goal

A binary tree has $N$ nodes, and each node's value states how many coins it currently holds. Across the whole tree there are exactly $N$ coins.

In one move, choose two adjacent nodes and transfer one coin across their connecting edge. The transfer may go from a parent to its child or from a child to its parent. Find the minimum number of moves needed to leave every node with exactly one coin. A coin crossing two edges counts as two moves, even if both transfers are part of the same route.

### Function Contract

**Inputs**

- `root`: the root of a non-empty binary tree containing $N$ nodes, where $1 \le N \le 100$.
- Every node value is between $0$ and $N$, and the sum of all node values is $N$.

Let $H$ denote the tree height. For a subtree rooted at node $u$, define its coin balance as

$$
B_u = \bigl(\text{coins in the subtree of }u\bigr)-\bigl(\text{nodes in that subtree}\bigr).
$$

**Return value**

- The minimum number of single-coin, single-edge moves required to give every node exactly one coin.

### Examples

**Example 1**

- Input: `root = [3, 0, 0]`
- Output: `2`
- Explanation: the root sends one coin to each child.

**Example 2**

- Input: `root = [0, 3, 0]`
- Output: `3`
- Explanation: the left child sends two coins to the root, after which the root sends one coin to the right child.
