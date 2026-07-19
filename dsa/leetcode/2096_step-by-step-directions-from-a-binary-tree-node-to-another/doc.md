# Step-By-Step Directions From a Binary Tree Node to Another

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2096 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) |

## Problem Description

### Goal

You are given the root of a binary tree with $n$ nodes. Every node has a unique value from $1$ through $n$. Two different values identify a starting node and a destination node.

Return directions for the unique shortest path from start to destination. Each `"L"` moves to a left child, each `"R"` moves to a right child, and each `"U"` moves to a parent. The output string must list these moves in traversal order.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $n$ uniquely valued nodes, where $2 \le n \le 10^5$.
- `startValue`: the value of the starting node.
- `destValue`: the distinct value of the destination node.

Both requested values occur in the tree.

**Return value**

Return the shortest direction string over `"L"`, `"R"`, and `"U"` from `startValue` to `destValue`.

### Examples

**Example 1**

- Input: `root = [5,1,2,3,null,6,4]`, `startValue = 3`, `destValue = 6`
- Output: `"UURL"`
- Explanation: The node sequence is `3 -> 1 -> 5 -> 2 -> 6`.

**Example 2**

- Input: `root = [2,1]`, `startValue = 2`, `destValue = 1`
- Output: `"L"`
