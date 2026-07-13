# Construct Binary Search Tree from Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1008 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-binary-search-tree-from-preorder-traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/).

### Goal
Given the preorder traversal of a binary search tree with distinct values, rebuild the tree.

### Function Contract
**Inputs**

- `preorder`: List[int]

**Return value**

TreeNode - root of the reconstructed BST

### Examples
**Example 1**

- Input: `preorder = [8, 5, 1, 7, 10, 12]`
- Output: tree with level order `[8, 5, 10, 1, 7, None, 12]`

**Example 2**

- Input: `preorder = [1, 3]`
- Output: tree with root `1` and right child `3`

**Example 3**

- Input: `preorder = [4, 2]`
- Output: tree with root `4` and left child `2`

---

## Solution
### Approach
Recursive preorder parsing with upper bounds.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)` recursion depth

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1008: Construct Binary Search Tree from Preorder Traversal."""

from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(preorder: list[int]) -> TreeNode | None:
    index = 0

    def build(upper: int) -> TreeNode | None:
        nonlocal index
        if index == len(preorder) or preorder[index] > upper:
            return None
        value = preorder[index]
        index += 1
        node = TreeNode(value)
        node.left = build(value)
        node.right = build(upper)
        return node

    return build(10**18)
```
</details>
