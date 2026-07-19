# N-ary Tree Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 429 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) |

## Problem Description
### Goal
Given the root of an N-ary tree, group its node values by distance from the root. The root forms the first level, all of its children form the next, and later levels contain children of the preceding level.

Return one list per occupied depth from top to bottom. Within a level, preserve natural left-to-right order induced by each parent's original child list and by parent order on the prior level. Missing or empty child lists add no placeholders. An empty tree returns an empty outer list, while every existing node appears exactly once.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- Return a list of levels, where each level contains node values in their original child order.

### Examples
**Example 1**

- Input: `root = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[[1], [3, 2, 4], [5, 6]]`

**Example 2**

- Input: `root = [7, []]`
- Output: `[[7]]`

**Example 3**

- Input: `root = None`
- Output: `[]`
