# Closest Nodes Queries in a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2476 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [closest-nodes-queries-in-a-binary-search-tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) |

## Problem Description & Examples
### Goal
Given the root of a binary search tree (BST) and a list of integer queries, determine for each query the largest value in the tree that is less than or equal to the query (the floor) and the smallest value in the tree that is greater than or equal to the query (the ceiling). If no such value exists for a specific bound, return -1.

### Function Contract
**Inputs**

- `root`: The root node of a Binary Search Tree.
- `queries`: A list of integers representing the values to search for in the BST.

**Return value**

- A list of lists, where each inner list contains two integers `[min_val, max_val]` corresponding to the floor and ceiling for the respective query.

### Examples
**Example 1**

- Input: `root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]`
- Output: `[[2,2],[4,6],[15,-1]]`

**Example 2**

- Input: `root = [4,null,9], queries = [3]`
- Output: `[[-1,4]]`

**Example 3**

- Input: `root = [1], queries = [1]`
- Output: `[[1,1]]`

---

## Underlying Base Algorithm(s)
The solution utilizes an In-order Traversal to extract the BST values into a sorted array. Once the values are sorted, the problem reduces to performing Binary Search (specifically `bisect_left` and `bisect_right`) on the array for each query to efficiently locate the floor and ceiling values.

---

## Complexity Analysis
- **Time Complexity**: O(N + Q log N), where N is the number of nodes in the BST and Q is the number of queries. The in-order traversal takes O(N), and each of the Q queries takes O(log N) using binary search.
- **Space Complexity**: O(N), required to store the sorted list of node values extracted from the BST.
