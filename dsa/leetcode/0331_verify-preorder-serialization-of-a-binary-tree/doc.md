# Verify Preorder Serialization of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 331 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) |

## Problem Description
### Goal
Given a comma-separated preorder serialization, integer tokens represent non-null binary-tree nodes and `#` tokens represent null child positions. Preorder records a node first, then the complete serialization of its left subtree, followed by its right subtree.

Return `True` only when every token fills one valid pending position and the final token completes exactly one whole tree. Missing null markers leave unfinished children, while extra tokens after all positions are filled are invalid. A lone `#` correctly represents an empty tree. Validate the sequence without constructing node objects or treating a numeric token as a leaf unless its two children are also represented.

### Function Contract
**Inputs**

- `preorder`: comma-separated integer and `#` tokens in preorder order

**Return value**

`True` when every token fills a valid child position and the serialization finishes with no missing or extra tokens; otherwise `False`.

### Examples
**Example 1**

- Input: `preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"`
- Output: `True`

**Example 2**

- Input: `preorder = "1,#"`
- Output: `False`

**Example 3**

- Input: `preorder = "9,#,#,1"`
- Output: `False`
