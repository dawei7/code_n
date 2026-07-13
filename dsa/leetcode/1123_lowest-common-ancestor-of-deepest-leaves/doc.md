# Lowest Common Ancestor of Deepest Leaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1123 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [lowest-common-ancestor-of-deepest-leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/).

### Goal
Find the lowest common ancestor of all deepest leaves in a binary tree.

### Function Contract
**Inputs**

- `root`: Root of a binary tree, represented in cOde(n) cases as a level-order list.

**Return value**

Root of the subtree whose root is the lowest common ancestor of every deepest leaf.

### Examples
**Example 1**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]`
- Output: `[2, 7, 4]`

**Example 2**

- Input: `root = [1]`
- Output: `[1]`

**Example 3**

- Input: `root = [0, 1, 3, null, 2]`
- Output: `[2]`

---

## Solution
### Approach
Use DFS that returns two pieces of information for each subtree: its maximum depth and the node that is the LCA of deepest leaves within that subtree.

If left and right depths are equal, the current node is the LCA for the deepest leaves below it. If one side is deeper, propagate that side's LCA upward.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
