# Merge BSTs to Create Single BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1932 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-bsts-to-create-single-bst/) |

## Problem Description
### Goal
You are given $K$ separate binary search trees in `trees`. Every input tree
contains between one and three nodes, no node has grandchildren, and the root
values are pairwise distinct. Each input tree already satisfies the strict BST
ordering rule.

One merge chooses a leaf of one tree whose value equals the root value of a
different tree, replaces that leaf with the entire matching tree, and removes
the matching tree from the collection. Perform exactly $K-1$ such operations
to combine every input tree. Return the resulting root if the single combined
tree is a valid BST; otherwise return `null`.

In a valid BST, every value in a node's left subtree is strictly smaller than
that node's value, and every value in its right subtree is strictly larger.
A leaf has no children.

### Function Contract
**Inputs**

- `trees`: a list of $K$ valid `TreeNode` BST roots with distinct root values, where
  $1 \le K \le 5\cdot10^4$. Each tree has at most three nodes and no
  grandchildren; every node value is between $1$ and $5\cdot10^4$.

Let $T$ be the total number of nodes supplied across all input trees and let
$H$ be the height of the final tree, if one can be formed.

**Return value**

- A `TreeNode` root of the one valid BST obtainable by consuming all input
  trees, or `null` when no valid complete merge exists.

### Examples
**Example 1**

- Input: `trees = [[2, 1], [3, 2, 5], [5, 4]]`
- Output: `[3, 2, 5, 1, null, 4]`

**Example 2**

- Input: `trees = [[5, 3, 8], [3, 2, 6]]`
- Output: `null`

The only possible graft places `6` in the left subtree of `5`, violating the
strict BST bounds.

**Example 3**

- Input: `trees = [[5, 4], [3]]`
- Output: `null`
