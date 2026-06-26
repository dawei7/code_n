# Tree of Coprimes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1766 |
| Difficulty | Hard |
| Topics | Array, Math, Tree, Depth-First Search, Number Theory |
| Official Link | [tree-of-coprimes](https://leetcode.com/problems/tree-of-coprimes/) |

## Problem Description & Examples
### Goal
For each node in a tree, find the nearest ancestor whose value is coprime with the node's value. Node values are small positive integers.

### Function Contract
**Inputs**

- `nums`: value at each tree node.
- `edges`: undirected edges of the tree.

**Return value**

Return an array where each entry is the index of the closest coprime ancestor, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]`
- Output: `[-1,0,0,1]`

**Example 2**

- Input: `nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]`
- Output: `[-1,0,-1,0,0,0,-1]`

**Example 3**

- Input: `nums = [7], edges = []`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
Precompute which values from `1` to `50` are coprime. During DFS from the root, maintain for each possible value the deepest ancestor currently on the path that has that value. For a node, scan coprime values and choose the stored ancestor with greatest depth, then push the current node's value before visiting children and restore it when backtracking.

---

## Complexity Analysis
- **Time Complexity**: `O(n * V + V^2)`, where `V = 50`
- **Space Complexity**: `O(n + V)`
