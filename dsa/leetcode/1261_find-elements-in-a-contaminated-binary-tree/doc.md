# Find Elements in a Contaminated Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1261 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) |

## Problem Description

### Goal

A binary tree has been contaminated so that every node value is `-1`, but its shape is unchanged. Recover its intended values using these rules: the root has value `0`; a node with value `x` gives its left child `2 * x + 1` and its right child `2 * x + 2` whenever those children exist.

Design `FindElements` to recover the tree during construction and answer whether a requested `target` value occurs in the recovered tree. The app-local contract receives the contaminated root plus a sequence of targets and returns the result of each `find` query in order.

### Function Contract

**Inputs**

- `root`: the nonempty root of a contaminated binary tree containing $N$ nodes and height at most `20`.
- `queries`: $Q$ nonnegative target values, each at most $10^6$.

**Return value**

- Return a Boolean list of length $Q$ indicating whether each target occurs after recovery.

### Examples

**Example 1**

- Input: `root = [-1, null, -1]`, `queries = [1, 2]`
- Output: `[false, true]`

**Example 2**

- Input: `root = [-1, -1, -1, -1, -1]`, `queries = [1, 3, 5]`
- Output: `[true, true, false]`

**Example 3**

- Input: `root = [-1, null, -1, -1, null, -1]`, `queries = [2, 3, 4, 5]`
- Output: `[true, false, false, true]`
