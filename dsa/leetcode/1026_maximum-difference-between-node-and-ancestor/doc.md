# Maximum Difference Between Node and Ancestor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1026 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-difference-between-node-and-ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/).

### Goal
Find the largest absolute difference between the values of two nodes where one node is an ancestor of the other.

### Function Contract
**Inputs**

- `root`: Root node of a binary tree, represented in cOde(n) cases as a level-order list.

**Return value**

Maximum absolute difference between an ancestor value and a descendant value.

### Examples
**Example 1**

- Input: `root = [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]`
- Output: `7`

**Example 2**

- Input: `root = [1, null, 2, null, 0, 3]`
- Output: `3`

**Example 3**

- Input: `root = [5]`
- Output: `0`

---

## Solution
### Approach
During DFS, keep the minimum and maximum values seen on the path from the root to the current node. For each node, the best ancestor difference involving that node is the larger of `abs(node.val - path_min)` and `abs(node.val - path_max)`.

Update the path minimum and maximum before recursing into children. The global answer is the largest difference found across all nodes.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
