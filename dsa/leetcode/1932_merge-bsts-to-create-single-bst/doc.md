# Merge BSTs to Create Single BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1932 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [merge-bsts-to-create-single-bst](https://leetcode.com/problems/merge-bsts-to-create-single-bst/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/merge-bsts-to-create-single-bst/).

### Goal
Several small BSTs are given. A tree can be merged into another by replacing a leaf whose value equals the root value of another tree. Determine whether all trees can merge into one valid BST.

### Function Contract
**Inputs**

- `trees`: a list of BST roots.

**Return value**

Return the root of the merged BST if possible, otherwise `null`.

### Examples
**Example 1**

- Input: `trees = [[2,1],[3,2,5],[5,4]]`
- Output: `[3,2,5,1,null,4]`

**Example 2**

- Input: `trees = [[5,3,8],[3,2,6]]`
- Output: `null`

**Example 3**

- Input: `trees = [[5,4],[3]]`
- Output: `null`

---

## Solution
### Approach
Map root values to tree roots and count leaf values. The final root must be the only root value that never appears as a leaf. Perform a DFS with BST lower and upper bounds; whenever a leaf value matches an unused root, graft that tree and continue. The merge is valid only if all trees are used and the final traversal respects BST bounds.

### Complexity Analysis
- **Time Complexity**: `O(total nodes)`
- **Space Complexity**: `O(number of trees + tree height)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
