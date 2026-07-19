# House Robber III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 337 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/house-robber-iii/) |

## Problem Description
### Goal
Houses occupy the nodes of a binary tree, and each node value gives the money available there. Robbing two directly connected houses triggers an alarm, so a chosen node forbids choosing its parent and either immediate child.

Return the maximum total value obtainable from any valid set of nodes. Grandchildren and more distant descendants may still be selected when their connecting parent is skipped, and choices in separate branches can be combined. You may choose no node when appropriate, and an empty tree returns `0`. The function returns only the optimal amount rather than the selected nodes or a modified tree.

### Function Contract
**Inputs**

- `root`: the binary-tree root, represented by a level-order list in app cases

**Return value**

The maximum sum obtainable from a set of pairwise nonadjacent parent-child nodes.

### Examples
**Example 1**

- Input: `root = [3,2,3,null,3,null,1]`
- Output: `7`

**Example 2**

- Input: `root = [3,4,5,1,3,null,1]`
- Output: `9`

**Example 3**

- Input: `root = [13]`
- Output: `13`
