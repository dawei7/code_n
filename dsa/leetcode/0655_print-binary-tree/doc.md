# Print Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 655 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/print-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree with height `height`, construct a zero-indexed string matrix `res` that displays the tree. Use `height + 1` rows and `2 ** ((height + 1)) - 1` columns, place the root's value in the middle cell of the top row, and fill unused cells with the empty string.

For a node placed at row `r` and column `c`, put its left child at column `c - 2 ** ((height - r - 1))` and its right child at `c + 2 ** ((height - r - 1))` on row $r + 1$. Continue until every node is represented, storing values as strings. Return the complete centered matrix, including its empty spacing cells.

### Function Contract
**Inputs**

- `root`: the non-null root node of a binary tree

**Return value**

- A string matrix with one row per tree level and $2^{R} - 1$ columns for `R` rows; node values occupy their prescribed centers and all unused cells contain `""`

### Examples
**Example 1**

- Input: `root = [1, 2]`
- Output: `[["", "1", ""], ["2", "", ""]]`

**Example 2**

- Input: `root = [1, 2, 3, null, 4]`
- Output: `[["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]`

**Example 3**

- Input: `root = [1]`
- Output: `[["1"]]`
