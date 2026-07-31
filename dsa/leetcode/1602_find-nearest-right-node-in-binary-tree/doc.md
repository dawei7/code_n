# Find Nearest Right Node in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1602 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree and a particular node `u` in that tree, find the node immediately to `u`'s right on the same depth level. “Nearest” refers to the ordinary left-to-right order of nodes at that level; the answer need not share a parent with `u`.

Return that neighboring node when it exists. If `u` is already the rightmost node on its level, return `null`. The target is identified by node identity, not by its stored value, so equal values elsewhere in the tree do not designate the same node.

### Function Contract
**Platform interface**

- `findNearestRightNode(root, u)` receives the binary-tree root and the actual target node object and returns the nearest same-level node to its right, or `null`.

**Inputs**

- `root`: the root node of a non-empty binary tree.
- `u`: the actual target `TreeNode` from the same tree as `root`. JSON fixtures preserve its identity with a `path_from_root` descriptor before the runner constructs both objects.

**Return value**

Return the nearest right tree node on the target's level, or `null` if no such node exists.

### Examples
**Example 1**

- Input: `root = [1,2,3,null,4,5,6]`, with `u` selecting node `4` by path `"LR"`.
- Output: the node `5`.

**Example 2**

- Input: `root = [3,null,4,2]`, with `u` selecting node `2` by path `"RL"`.
- Output: `null`.

**Example 3**

- Input: a single-node tree with `u` equal to `root`.
- Output: `null`.
