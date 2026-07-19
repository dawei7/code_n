# Maximum Average Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-average-subtree/) |

## Problem Description

### Goal

You are given the root of a nonempty binary tree whose node values are nonnegative. For any node, its subtree consists of that node together with every descendant reachable through its left and right children.

The average value of a subtree is the sum of all values in that subtree divided by its number of nodes. Consider the subtree rooted at every node and return the greatest of those averages. The answer is accepted within the platform's floating-point tolerance.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes; cOde(n) fixtures serialize it in level order with `null` for absent children.

**Return value**

- The maximum arithmetic mean among all $N$ rooted subtrees, as a floating-point number.

### Examples

**Example 1**

- Input: `root = [5,6,1]`
- Output: `6.0`

The leaf containing `6` has average 6, while the entire tree has average 4.

**Example 2**

- Input: `root = [0,null,1]`
- Output: `1.0`
