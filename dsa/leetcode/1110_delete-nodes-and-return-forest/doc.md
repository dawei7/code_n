# Delete Nodes And Return Forest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1110 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [delete-nodes-and-return-forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/delete-nodes-and-return-forest/).

### Goal
Remove every tree node whose value appears in `to_delete`. Return the roots of all remaining connected components.

### Function Contract
**Inputs**

- `root`: root of a binary tree with unique node values.
- `to_delete`: values of nodes to remove.

**Return value**

A list of root nodes for the forest left after deletion. The order is not important.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,6,7]`, `to_delete = [3,5]`
- Output: roots representing `[[1,2,null,4],[6],[7]]`

**Example 2**

- Input: `root = [1,2,4,null,3]`, `to_delete = [2]`
- Output: roots representing `[[1,null,4],[3]]`

**Example 3**

- Input: `root = [1]`, `to_delete = [1]`
- Output: `[]`

---

## Solution
### Approach
Postorder depth-first search with set membership.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for recursion depth, delete set, and output in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1110: Delete Nodes And Return Forest."""

from __future__ import annotations

from typing import Any


def solve(root: Any | None, to_delete: list[int]) -> list[Any]:
    deleted = set(to_delete)
    forest: list[Any] = []

    def dfs(node: Any | None, is_root: bool) -> Any | None:
        if node is None:
            return None
        remove = node.val in deleted
        if is_root and not remove:
            forest.append(node)
        node.left = dfs(node.left, remove)
        node.right = dfs(node.right, remove)
        return None if remove else node

    dfs(root, True)
    return forest
```
</details>
