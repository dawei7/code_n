# Correct a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1660 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/correct-a-binary-tree/) |

## Problem Description
### Goal
A binary tree contains exactly one invalid node. Instead of a normal right child, that node's `right` pointer incorrectly references another node at the same depth that lies to its right. Remove the invalid node and its entire genuine descendant subtree while preserving the node reached by the erroneous pointer and every other valid part of the tree.

For serialized custom tests, `root.values` describes the tree before corruption. The fixture's `root.corrupt_right` descriptor identifies the source and target by their unique values; the cOde(n) harness installs that invalid pointer while constructing the `TreeNode` graph, before it calls `solve(root)`.

### Function Contract
**Inputs**

- `root`: the actual `TreeNode` root passed to the solution. It contains between 3 and $10^4$ uniquely valued nodes, with each value in $[-10^9,10^9]$.

In JSON cases, `root` has a level-order `values` array and a `corrupt_right` object with `from_value` and `to_value`. The harness reconstructs the graph and redirects the source node's originally null `right` pointer to the same-depth target on its right. These serialization fields are fixture metadata, not extra solution parameters. Let $N$ be the number of tree nodes.

**Return value**

Return the corrected tree root after removing the invalid node and all of its genuine descendants. The incorrectly referenced `toNode` subtree remains in its original location.

### Examples
**Example 1**

- Input: `root = {"values":[1,2,3],"corrupt_right":{"from_value":2,"to_value":3}}`
- Output: `[1, null, 3]`

Node 2 is invalid, so its parent link is cleared.

**Example 2**

- Input: `root = {"values":[8,3,1,7,null,9,4,2,null,null,null,5,6],"corrupt_right":{"from_value":7,"to_value":4}}`
- Output: `[8, 3, 1, null, null, 9, 4, null, null, 5, 6]`

Removing invalid node 7 also removes its genuine descendant 2, while node 4 remains attached beneath node 1.
