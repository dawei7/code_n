# Same Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 100 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/same-tree/) |

## Problem Description
### Goal
You are given roots `p` and `q` of two binary trees. Compare them recursively by position: corresponding nodes must either both be absent or both exist with equal stored values.

Return `True` only when the trees have identical shapes and every corresponding value matches. Equal traversal value sequences are insufficient if child placements differ. Two empty trees are the same, while one empty and one nonempty tree are different.

### Function Contract
**Inputs**

- `p`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases
- `q`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` when the trees are identical in both shape and values; otherwise `False`.

### Examples
**Example 1**

- Input: `p = [1, 2, 3], q = [1, 2, 3]`
- Output: `True`

**Example 2**

- Input: `p = [1, 2], q = [1, null, 2]`
- Output: `False`

**Example 3**

- Input: `p = [1, 2, 1], q = [1, 1, 2]`
- Output: `False`
