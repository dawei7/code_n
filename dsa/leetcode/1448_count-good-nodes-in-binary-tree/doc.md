# Count Good Nodes in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1448 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-good-nodes-in-binary-tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-good-nodes-in-binary-tree/).

### Goal
Given a binary tree (level-order array), count nodes where the path from root to that node has no value greater than the node's value.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - count of good nodes

### Examples
**Example 1**

- Input: `root = [3, 1, 4, 3, None, 1, 5]`
- Output: `4`

**Example 2**

- Input: `root = [7]`
- Output: `1`

**Example 3**

- Input: `root = [3, 10]`
- Output: `2`

---

## Solution
### Approach
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
