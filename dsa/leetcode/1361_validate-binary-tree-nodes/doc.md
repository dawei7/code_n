# Validate Binary Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1361 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/validate-binary-tree-nodes/) |

## Problem Description

### Goal

Nodes are labeled from $0$ through $n-1$. Parallel arrays `leftChild` and `rightChild` describe directed child links: value `-1` means that side has no child, while any other value is the label of the corresponding left or right child.

Determine whether these links form exactly one valid binary tree containing all $n$ nodes. Thus one node must be the root, every other node must have exactly one parent, no node may have multiple parents, and following child links must reach every node without a cycle or disconnected component. Return a boolean result.

### Function Contract

**Inputs**

- `n`: the number of labeled nodes.
- `leftChild` and `rightChild`: length-$n$ arrays containing child labels or `-1`.

**Return value**

- `true` exactly when the described links form one binary tree over all $n$ nodes; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]`
- Output: `true`

**Example 2**

- Input: `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]`
- Output: `false`
- Explanation: node `3` is assigned to two parents.

**Example 3**

- Input: `n = 2, leftChild = [1,0], rightChild = [-1,-1]`
- Output: `false`
- Explanation: the two links form a cycle, leaving no root.
