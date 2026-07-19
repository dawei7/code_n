# Construct Quad Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 427 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Tree, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-quad-tree/) |

## Problem Description
### Goal
Given an $n \times n$ binary grid where `n` is a power of two, represent its complete area as a quad tree. A region containing one uniform value becomes a leaf storing that Boolean value; a mixed region must be divided into four equally sized quadrants.

Return the root `Node` of the representation. Internal children must appear in top-left, top-right, bottom-left, and bottom-right order, with the same uniformity rule applied recursively. A leaf has no meaningful children, while an internal node's `val` does not describe the mixed region. Preserve every grid cell through the hierarchical partition without merging nonuniform areas.

### Function Contract
**Inputs**

- `grid`: an `n`-by-`n` matrix of zeros and ones, where `n` is a power of two

**Return value**

- Return the constructed Node object. A leaf stores its region's Boolean value; an internal node stores its children in top-left, top-right, bottom-left, bottom-right order.

### Examples
**Example 1**

- Input: `grid = [[0, 1], [1, 0]]`
- Output: `{"leaf": false, "children": [{"leaf": true, "value": 0}, {"leaf": true, "value": 1}, {"leaf": true, "value": 1}, {"leaf": true, "value": 0}]}`

**Example 2**

- Input: `grid = [[1, 1], [1, 1]]`
- Output: `{"leaf": true, "value": 1}`

**Example 3**

- Input: `grid = [[0]]`
- Output: `{"leaf": true, "value": 0}`
