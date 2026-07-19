# Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 113 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-sum-ii/) |

## Problem Description
### Goal
Given the root of a binary tree and an integer `targetSum`, find every complete downward path whose node values add to that total. Each path must start at the root, follow child links, and end at a leaf; stopping at an internal node with the desired partial sum is not enough.

Return the qualifying paths as lists of values in root-to-leaf order. Different branches may produce identical value sequences and still represent distinct valid paths, so retain every occurrence. The paths may be returned in any outer order, values may be negative or zero, and an empty tree or a tree with no matching leaf produces an empty list.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases
- `targetSum`: the required sum for each complete path

**Return value**

A list of qualifying root-to-leaf value paths. The outer path order does not matter; value order inside each path does.

### Examples
**Example 1**

- Input: `root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22`
- Output: `[[5, 4, 11, 2], [5, 8, 4, 5]]`

**Example 2**

- Input: `root = [1, 2, 3], targetSum = 5`
- Output: `[]`

**Example 3**

- Input: `root = [1, 2], targetSum = 3`
- Output: `[[1, 2]]`
