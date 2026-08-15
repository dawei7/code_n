# Create Binary Tree From Descriptions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2196 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/) |

## Problem Description

### Goal

Each entry `[parent, child, isLeft]` describes one edge of a binary tree whose
node values are unique. When `isLeft` is `1`, `child` is the left child of
`parent`; when it is `0`, `child` is the right child.

Construct the single valid binary tree represented by all descriptions and
return its root node. Descriptions may arrive in any order, including before a
node's own relationship to its parent is listed.

### Function Contract

**Inputs**

- `descriptions`: an array of $m$ triples, where $1\le m\le10^4$, node values
  lie in $[1,10^5]$, and each direction flag is `0` or `1`.

The triples are guaranteed to describe one valid binary tree with unique node
values.

**Return value**

Return the root of the constructed binary tree.

### Examples

#### Example 1

- **Input:** `descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`
- **Output:** `[50,20,80,15,17,19]`

#### Example 2

- **Input:** `descriptions = [[1,2,1],[2,3,0],[3,4,1]]`
- **Output:** `[1,2,null,null,3,4]`

#### Example 3

- **Input:** `descriptions = [[7,9,0]]`
- **Output:** `[7,null,9]`
