# Number of Good Leaf Nodes Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1530 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/) |

## Problem Description
### Goal

Given the root of a binary tree and an integer `distance`, consider every unordered pair of two different leaf nodes. A pair is good when the length of the shortest path between its leaves, measured in tree edges, is at most `distance`.

Return the number of good leaf-node pairs. Internal node values do not affect which pairs qualify; only the tree structure and the path-length limit matter.

### Function Contract
**Inputs**

- `root`: The root of a nonempty binary tree containing between 1 and $2^{10}$ nodes.
- Each node value lies between 1 and 100, inclusive.
- `distance`: An integer from 1 through 10.

**Return value**

Return the number of unordered pairs of distinct leaves whose shortest connecting path contains at most `distance` edges.

### Examples
**Example 1**

- Input: `root = [1, 2, 3, null, 4], distance = 3`
- Output: `1`
- Explanation: Leaves 3 and 4 are three edges apart, so their only pair is good.

**Example 2**

- Input: `root = [1, 2, 3, 4, 5, 6, 7], distance = 3`
- Output: `2`
- Explanation: The sibling pairs `(4, 5)` and `(6, 7)` have distance 2; cross-subtree leaf pairs have distance 4.

**Example 3**

- Input: `root = [7, 1, 4, 6, null, 5, 3, null, null, null, null, null, 2], distance = 3`
- Output: `1`
- Explanation: Only the pair formed by leaves 2 and 5 meets the limit.
