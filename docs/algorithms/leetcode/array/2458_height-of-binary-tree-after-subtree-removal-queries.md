# Height of Binary Tree After Subtree Removal Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2458 |
| Difficulty | Hard |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [height-of-binary-tree-after-subtree-removal-queries](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) |

## Problem Description & Examples
### Goal
Given a binary tree, we must process a series of queries. Each query specifies a node to be removed from the tree. After removing the subtree rooted at that node, we need to determine the height of the remaining tree (the maximum distance from the root to any leaf). The tree structure remains intact for subsequent queries.

### Function Contract
**Inputs**

- `root`: The root node of the binary tree.
- `queries`: A list of integers representing the values of the nodes whose subtrees are to be removed.

**Return value**

- A list of integers where each element corresponds to the height of the tree after the removal specified by the query.

### Examples
**Example 1**

- Input: `root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]`
- Output: `[2]`

**Example 2**

- Input: `root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]`
- Output: `[3,2,3,2]`

**Example 3**

- Input: `root = [1,null,5,3,null,2,4], queries = [3,5,4,2,4]`
- Output: `[1,0,3,3,3]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Depth-First Search (DFS) approach to pre-calculate the height of every node and the maximum height reachable at each depth level. By tracking the two largest heights at each depth, we can determine the new tree height after removing a subtree: if the removed node was on the path of the tallest branch at its depth, the height becomes the second-tallest branch at that depth; otherwise, it remains the tallest.

---

## Complexity Analysis
- **Time Complexity**: `O(N + Q)`, where `N` is the number of nodes in the tree and `Q` is the number of queries. We traverse the tree once to compute heights and then process each query in constant time.
- **Space Complexity**: `O(N)`, required to store the height and depth information for each node, as well as the pre-calculated results for each depth level.
