# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1379 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) |

## Problem Description

### Goal

A binary tree has been copied exactly. The root of the source tree is `original`, and `cloned` is the root of the separate cloned tree with the same structure and node values. A particular node object inside the source tree is supplied as `target`.

Return the node object in the cloned tree that occupies the same structural position as `target` occupies in the original. The answer must be a reference to the existing cloned node; do not modify either tree, and do not rely on node values being unique.

### Function Contract

**Inputs**

- `original`: the root node of the original binary tree containing $N$ nodes.
- `cloned`: the root node of a distinct tree that is an exact clone of `original`.
- `target`: a tree node object that belongs to the original tree.

**Return value**

- The existing tree node in `cloned` corresponding to the exact object `target` in `original`.

### Examples

**Example 1**

- Input: `original = [7,4,3,null,null,6,19], target = node 3`
- Output: `node 3 in cloned`

**Example 2**

- Input: `original = [7], target = node 7`
- Output: `node 7 in cloned`

**Example 3**

- Input: `original = [8,null,6,null,5,null,4], target = node 6`
- Output: `node 6 in cloned`
