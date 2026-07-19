# All Nodes Distance K in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 863 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, a target node in that tree, and a nonnegative integer `k`, find every node whose distance from the target is exactly `k`. The distance between two nodes is the number of edges on their unique connecting path, which may travel through children, through parents, or in both directions.

Return the values of all qualifying nodes in any order. Every node value is unique, so the serialized target value identifies exactly one node. The target is guaranteed to belong to the tree; if no node is far enough away, return an empty array.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, where $1 \leq n \leq 500$.
- `target`: the target node. Authored app cases identify it by its unique value; the native LeetCode entrypoint receives the corresponding `TreeNode` object.
- `k`: the required edge distance, where $0 \leq k \leq 1000$.

Every node value is unique and lies in $[0,500]$.

**Return value**

Return an array containing the values of exactly the nodes at distance `k` from `target`. The values may appear in any order.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`
- Output: `[7,4,1]`

The nodes with values `7` and `4` are two edges below the target, while `1` is reached through the target's parent.

**Example 2**

- Input: `root = [1], target = 1, k = 3`
- Output: `[]`

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 0`
- Output: `[5]`
