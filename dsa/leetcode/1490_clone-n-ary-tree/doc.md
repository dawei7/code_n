# Clone N-ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1490 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/clone-n-ary-tree/) |

## Problem Description
### Goal

An N-ary tree node stores an integer value and an ordered list of zero or more child nodes. Given the tree's root, construct a deep copy of the entire tree.

The returned root must belong to a newly allocated tree. For every original node, its copy must hold the same value, and the copied node's children must be the copies of the original children in the same left-to-right order. No node object in the result may be one of the original node objects. Return null when the input tree is empty.

### Function Contract
**Inputs**

Let $N$ be the number of nodes and $H$ the tree height.

- Native `cloneTree(root)` receives the root of an N-ary tree whose nodes expose `val` and an ordered `children` list.
- The structure is a tree: every non-root node occurs in exactly one parent's child list.
- A node may be a leaf with an empty child list, and `root` may be null.
- The app-local `solve(root)` receives the same structure serialized recursively as `[value, children]`, where every element of `children` is another encoded node.

**Return value**

Return the root of a newly allocated N-ary tree with the same values, shape, and child ordering as the input. For the app-local representation, return an equal but independently allocated nested `[value, children]` structure. Return `None` for an empty tree.

### Examples
**Example 1**

- Input: `root = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Explanation: The clone preserves the root's child order `3, 2, 4` and the two children below node `3`, but every encoded node list is newly allocated.

**Example 2**

- Input: `root = [1, [[2, []], [3, [[6, []], [7, [[11, [[14, []]]]]]]], [4, [[8, [[12, []]]]]], [5, [[9, [[13, []]]], [10, []]]]]]`
- Output: `[1, [[2, []], [3, [[6, []], [7, [[11, [[14, []]]]]]]], [4, [[8, [[12, []]]]]], [5, [[9, [[13, []]]], [10, []]]]]]`
- Explanation: Different branching factors and depths are copied without flattening or reordering the tree.

**Example 3**

- Input: `root = None`
- Output: `None`
