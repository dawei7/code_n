# Binary Tree Pruning

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 814 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-pruning/) |

## Problem Description

### Goal

You are given the root of a binary tree in which every node stores either `0` or `1`. A subtree consists of a node together with all descendants reachable below it. Such a subtree is eligible for removal when none of those nodes contains `1`.

Prune every eligible subtree and return the root of what remains. Removing a subtree deletes its top node as well as all descendants, so pruning lower branches can make an all-zero ancestor removable too. The entire tree may disappear, in which case the returned root is `None`; surviving nodes keep their original relative structure.

### Function Contract

**Inputs**

- `root`: the root of a binary tree whose node values are `0` or `1`, or `None`.

**Return value**

- The root after pruning every all-zero subtree; this may be `None` when the whole tree is removed.

### Examples

**Example 1**

- Input: `root = [1,null,0,0,1]`
- Output: `[1,null,0,null,1]`
- Explanation: The zero leaf below the right child is removed, while the zero node with a `1` descendant remains.

**Example 2**

- Input: `root = [1,0,1,0,0,0,1]`
- Output: `[1,null,1,null,1]`
- Explanation: The entire left subtree and the zero leaf under the right subtree contain no `1` and are pruned.

**Example 3**

- Input: `root = [0,0,0]`
- Output: `[]`
- Explanation: No node in the tree has value `1`, so the root is also removed.
