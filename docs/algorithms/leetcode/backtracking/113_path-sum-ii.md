# Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 113 |
| Difficulty | Medium |
| Topics | Backtracking, Tree, Depth-First Search, Binary Tree |
| Official Link | [path-sum-ii](https://leetcode.com/problems/path-sum-ii/) |

## Problem Description & Examples
### Goal
Given a binary tree and a target sum, return every root-to-leaf path whose node values add exactly to the target.

### Function Contract
**Inputs**

- `root`: TreeNode or nested tree representation
- `targetSum`: int

**Return value**

List[List[int]] - each inner list is one valid root-to-leaf value path

### Examples
**Example 1**

- Input: `root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22`
- Output: `[[5, 4, 11, 2], [5, 8, 4, 5]]`

**Example 2**

- Input: `root = [1,2,3], targetSum = 5`
- Output: `[]`

**Example 3**

- Input: `root = [1,2], targetSum = 3`
- Output: `[[1, 2]]`

---

## Underlying Base Algorithm(s)
Depth-first tree traversal with backtracking path state.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)` auxiliary recursion space, plus output paths
