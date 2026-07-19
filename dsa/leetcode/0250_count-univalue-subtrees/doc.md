# Count Univalue Subtrees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 250 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-univalue-subtrees/) |

## Problem Description
### Goal
Given the root of a binary tree, consider the complete subtree rooted at every existing node. A rooted subtree is univalue when that node and every descendant contained beneath it all store the same value.

Return the number of nodes whose full rooted subtree satisfies this condition. Every leaf contributes one because it contains only its own value. A parent does not qualify merely because its immediate children match if a deeper descendant differs, while an empty tree contributes zero subtrees. Count overlapping qualifying subtrees independently, such as qualifying children inside a larger qualifying parent subtree.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

The number of nodes whose complete rooted subtree is univalue.

### Examples
**Example 1**

- Input: `root = [5,1,5,5,5,null,5]`
- Output: `4`

**Example 2**

- Input: `root = []`
- Output: `0`

**Example 3**

- Input: `root = [1,1,1]`
- Output: `3`
