# Closest Binary Search Tree Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 270 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value/) |

## Problem Description
### Goal
Given the nonempty root of a binary search tree and a floating-point `target`, compare the absolute distance between the target and every stored node value. The target does not need to be an integer or occur in the tree.

Return the tree value with the smallest absolute difference from `target`. Use the binary-search ordering to avoid exploring irrelevant branches. If two values are equally close under the app contract, choose the smaller value so the result is deterministic. Return the node's integer value rather than the node object, its depth, or the numerical distance itself.

### Function Contract
**Inputs**

- `root`: the nonempty root of a binary search tree
- `target`: the value to approximate

**Return value**

The tree value with minimum absolute distance from `target`, choosing the smaller value on a tie.

### Examples
**Example 1**

- Input: `root = [4,2,5,1,3], target = 3.714286`
- Output: `4`

**Example 2**

- Input: `root = [1], target = 4.428571`
- Output: `1`

**Example 3**

- Input: `root = [2,1,3], target = 1.2`
- Output: `1`
