# Smallest Missing Genetic Value in Each Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2003 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search, Union-Find |
| Official Link | [smallest-missing-genetic-value-in-each-subtree](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/) |

## Problem Description & Examples
### Goal
For every node in a rooted tree, find the smallest positive genetic value that does not appear anywhere in that node's subtree.

### Function Contract
**Inputs**

- `parents`: parent index for each node, with `-1` for the root.
- `nums`: distinct genetic values assigned to nodes.

**Return value**

Return an array where answer `i` is the smallest missing positive value in node `i`'s subtree.

### Examples
**Example 1**

- Input: `parents = [-1,0,0,2], nums = [1,2,3,4]`
- Output: `[5,1,1,1]`

**Example 2**

- Input: `parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]`
- Output: `[7,1,1,4,2,1]`

**Example 3**

- Input: `parents = [-1,0,0], nums = [2,3,4]`
- Output: `[1,1,1]`

---

## Underlying Base Algorithm(s)
Only subtrees on the ancestor path of the node containing genetic value `1` can have an answer greater than `1`. Walk that path upward, adding each newly covered subtree's values to a seen set, and advance the smallest missing pointer.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
