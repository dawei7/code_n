# Recover a Tree From Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1028 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) |

## Problem Description

### Goal

A preorder depth-first search is performed from the `root` of a binary tree. When a node is visited, its encoding first writes `D` dashes, where `D` is that node's depth, and then writes the node's decimal value. The root has depth $0$, and an immediate child of a depth-$D$ node has depth $D+1$.

The traversal visits each parent before its left and right subtrees. If a node has exactly one child, the input guarantees that child is the left child.

Given the resulting string `traversal`, recover the original binary tree and return its root.

### Function Contract

**Inputs**

- `traversal`: the preorder encoding of a binary tree containing $N$ nodes, where $1 \le N \le 1000$ and $1 \le \texttt{Node.val} \le 10^9$.
- Let $L$ be the number of characters in `traversal`, and let $H$ be the recovered tree's height.

**Return value**

- The root of the recovered tree, represented in cases as a level-order array using `null` for absent children.

### Examples

**Example 1**

- Input: `traversal = "1-2--3--4-5--6--7"`
- Output: `[1,2,5,3,4,6,7]`
- Explanation: The depth markers reconstruct a full three-level tree.

**Example 2**

- Input: `traversal = "1-2--3---4-5--6---7"`
- Output: `[1,2,5,3,null,6,null,4,null,7]`
- Explanation: The three-dash nodes are children of the preceding depth-two nodes.

**Example 3**

- Input: `traversal = "1-401--349---90--88"`
- Output: `[1,401,null,349,88,90]`
- Explanation: Multi-digit values continue until the next dash or the end of the string.
