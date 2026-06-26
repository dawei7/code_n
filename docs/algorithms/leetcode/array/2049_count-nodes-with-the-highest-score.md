# Count Nodes With the Highest Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2049 |
| Difficulty | Medium |
| Topics | Array, Tree, Depth-First Search, Binary Tree |
| Official Link | [count-nodes-with-the-highest-score](https://leetcode.com/problems/count-nodes-with-the-highest-score/) |

## Problem Description & Examples
### Goal
For each node, remove it from the rooted tree and multiply the sizes of every remaining connected component. Count how many nodes achieve the highest such score.

### Function Contract
**Inputs**

- `parents`: parent index for each node, with `-1` for the root.

**Return value**

Return the number of nodes whose removal score is maximal.

### Examples
**Example 1**

- Input: `parents = [-1,2,0,2,0]`
- Output: `3`

**Example 2**

- Input: `parents = [-1,2,0]`
- Output: `2`

**Example 3**

- Input: `parents = [-1,0,0,1,1,2]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Build child lists and compute subtree sizes with DFS. For node `u`, multiply each child subtree size and, when `u` is not the root, also multiply by the size of the parent-side component `n - subtree_size[u]`. Track the maximum score and its frequency.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
