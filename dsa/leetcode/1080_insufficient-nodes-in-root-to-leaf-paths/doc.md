# Insufficient Nodes in Root to Leaf Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1080 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [insufficient-nodes-in-root-to-leaf-paths](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/).

### Goal
Remove every node that is not part of any root-to-leaf path whose sum is at least `limit`. Return the root of the pruned tree.

### Function Contract
**Inputs**

- `root`: Root of a binary tree, represented in cOde(n) cases as a level-order list.
- `limit`: Minimum acceptable root-to-leaf path sum.

**Return value**

Root of the tree after all insufficient nodes are removed.

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, 5, 6, 7], limit = 7`
- Output: `[1, 2, 3, 4, 5, 6, 7]`

**Example 2**

- Input: `root = [1, 2, -3, -5, null, 4, null], limit = -1`
- Output: `[1, null, -3, 4]`

**Example 3**

- Input: `root = [5, 4, 8, 11, null, 17, 4, 7, 1, null, null, 5, 3], limit = 22`
- Output: `[5, 4, 8, 11, null, 17, 4, 7, null, null, null, 5]`

---

## Solution
### Approach
Use postorder DFS. At each node, subtract the node's value from `limit` and recursively prune its children. After pruning, if the node has become a leaf, keep it only when its root-to-leaf sum reaches the original limit.

The postorder order is important because whether an internal node survives depends on whether at least one child subtree survives.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
