# Logical OR of Two Binary Grids Represented as Quad-Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 558 |
| Difficulty | Medium |
| Topics | Divide and Conquer, Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/) |

## Problem Description
### Goal
Two quad trees represent binary grids of exactly the same dimensions. A leaf represents a uniform region with Boolean value `0` or `1`, while an internal node divides its region into top-left, top-right, bottom-left, and bottom-right quadrants.

Compute the cell-by-cell logical OR of the represented grids and return a quad tree for the result. A result region should be compressed into one leaf whenever all of its cells share a value; otherwise preserve its four recursive quadrants. The returned tree must represent every grid cell correctly, regardless of whether the two inputs use different subdivision depths.

### Function Contract
**Inputs**

- `quadTree1`: the first quad-tree root
- `quadTree2`: the second quad-tree root

**Return value**

- A quad-tree root representing the logical OR of both grids

### Examples
**Example 1**

- Input: a false leaf and a true leaf
- Output: a true leaf

**Example 2**

- Input: a false leaf and a divided quad-tree
- Output: the divided quad-tree

**Example 3**

- Input: two divided trees whose combined quadrants are all true
- Output: one compressed true leaf
