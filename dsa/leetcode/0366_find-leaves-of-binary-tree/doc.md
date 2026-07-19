# Find Leaves of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 366 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-leaves-of-binary-tree/) |

## Problem Description
### Goal
Given a binary tree, repeatedly collect all current leaves and remove them simultaneously. A leaf in a given round is a node with no remaining children at the start of that round; removing lower nodes can cause their parents to become leaves later.

Return one list of node values per removal round, from the original leaves through the final root. Values within a round may appear in any order, but every node must occur exactly once in the round when it becomes a leaf. An empty tree returns an empty outer list, while a one-node tree produces one round containing its root value.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, represented as level-order values in app cases and as `TreeNode` objects during execution

**Return value**

- A list of removal rounds from first to last. Values within one round may appear in any order.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5]`
- Output: `[[4,5,3],[2],[1]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
