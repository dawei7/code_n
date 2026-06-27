# Find Subtree Sizes After Changes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3331 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Tree, Depth-First Search |
| Official Link | [find-subtree-sizes-after-changes](https://leetcode.com/problems/find-subtree-sizes-after-changes/) |

## Problem Description & Examples
### Goal
Given a tree represented by a parent array and a string of characters, we perform a transformation: for every node, if its parent has the same character value, the node's parent is updated to the nearest ancestor that shares the same character. After these updates, we must calculate the size of the subtree for every node in the modified tree structure.

### Function Contract
**Inputs**

- `parent`: A list of integers where `parent[i]` is the parent of node `i` (root is 0 with `parent[0] = -1`).
- `s`: A string where `s[i]` is the character associated with node `i`.

**Return value**

- A list of integers representing the subtree size for each node in the modified tree.

### Examples
**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 1], s = "abaabc"`
- Output: `[6, 3, 1, 1, 1, 1]`

**Example 2**

- Input: `parent = [-1, 0, 0, 0], s = "aabc"`
- Output: `[4, 1, 1, 1]`

**Example 3**

- Input: `parent = [-1, 0, 1, 2], s = "abab"`
- Output: `[4, 3, 2, 1]`

---

## Underlying Base Algorithm(s)
The problem is solved using a two-pass Depth-First Search (DFS) approach. First, we build an adjacency list to represent the tree. We then perform a DFS to identify the "new" parent for each node by tracking the most recent ancestor for each character 'a'-'z'. After remapping the parent pointers, we perform a second DFS to compute the subtree sizes based on the new tree structure.

---

## Complexity Analysis
- **Time Complexity**: O(N), where N is the number of nodes. We traverse the tree twice: once to remap parents and once to calculate subtree sizes.
- **Space Complexity**: O(N) to store the adjacency list, the new parent mapping, and the recursion stack.
