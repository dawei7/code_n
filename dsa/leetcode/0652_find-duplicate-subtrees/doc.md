# Find Duplicate Subtrees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 652 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-duplicate-subtrees/) |

## Problem Description
### Goal
Given the root of a binary tree, find every kind of subtree that occurs at least twice. Two subtrees are duplicates only when they have the same structure and the same node values, including the placement of null children.

Return the root node of any one occurrence for each kind of duplicate subtree. A kind that appears three or more times still contributes only one representative, and representatives may be returned in any order. Occurrences may be rooted at different depths and may overlap through ancestor-descendant relationships.

### Function Contract
**Inputs**

- `root`: the root node of a binary tree, or `None` for an empty tree

**Return value**

- A list containing one representative node for each duplicated subtree; representatives may appear in any order

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, null, 2, 4, null, null, 4]`
- Output: `[[2, 4], [4]]`

**Example 2**

- Input: `root = [2, 1, 1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = [2, 2, 2, 3, null, 3, null]`
- Output: `[[2, 3], [3]]`
