# Tree Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 608 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-node/) |

## Problem Description
### Goal
Given a `Tree` table in which each row contains a unique node `id` and its parent `p_id`, classify every node in the valid tree as one of three types. A node with a null parent is `Root`; a non-root node that is the parent of at least one other row is `Inner`; and every remaining node is `Leaf`.

Return each node's `id` and its classification in a column named `type`, in any order. The classification depends on both the node's own parent field and whether its identifier appears as another node's parent; a one-node tree is a root rather than a leaf.

### Function Contract
**Inputs**

- `Tree(id, p_id)`: node identifiers and their optional parent identifiers

**Return value**

- Columns `id` and `type`
- `Root` when `p_id` is null
- `Inner` when the node is not a root and appears as another row's parent
- `Leaf` otherwise

### Examples
**Example 1**

- Input: node 1 has no parent, node 2 is its child, and node 3 is a child of node 2
- Output: node 1 is `Root`, node 2 is `Inner`, and node 3 is `Leaf`

**Example 2**

- Input: a tree containing one node
- Output: that node is `Root`

**Example 3**

- Input: a root with two children and no grandchildren
- Output: the root is `Root` and both children are `Leaf`
