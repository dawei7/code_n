# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1430 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) |

## Problem Description

### Goal

Given the root of a binary tree and an integer array `arr`, determine whether `arr` is exactly the sequence of node values along some path that starts at the root and ends at a leaf. Consecutive array entries must correspond to parent-child steps in the tree.

Matching only a prefix or reaching an internal node when the array ends is not sufficient: the last array value must match a node with no children. Likewise, a root-to-leaf path is invalid if it ends before every array value has been consumed.

### Function Contract

**Inputs**

- `root`: the root node of a nonempty binary tree containing $N$ nodes, where $1 \le N \le 5000$.
- `arr`: an integer array of length $k$, where $1 \le k \le 5000$.
- Every tree value and array value is between $0$ and $9$.
- Let $h$ be the height of the tree.

**Return value**

- `true` if one root-to-leaf path has exactly the values in `arr` in order; otherwise `false`.

### Examples

**Example 1**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]`
- Output: `true`

**Example 2**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]`
- Output: `false`

**Example 3**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]`
- Output: `false`
