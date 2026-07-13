# Number Of Ways To Reconstruct A Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1719 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Graph Theory, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-to-reconstruct-a-tree](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/).

### Goal
Given unordered ancestor-descendant pairs from an unknown rooted tree, determine whether no tree, exactly one tree, or multiple trees could produce all given pairs.

### Function Contract
**Inputs**

- `pairs`: a list of distinct node pairs `[u, v]`.

**Return value**

Return `0` if reconstruction is impossible, `1` if the tree is unique, or `2` if multiple valid trees exist.

### Examples
**Example 1**

- Input: `pairs = [[1,2],[2,3]]`
- Output: `1`

**Example 2**

- Input: `pairs = [[1,2],[2,3],[1,3]]`
- Output: `2`

**Example 3**

- Input: `pairs = [[1,2],[2,3],[2,4],[1,5]]`
- Output: `0`

---

## Solution
### Approach
Build an undirected adjacency set for every node. A valid root must be connected to all other nodes. For each non-root node, its parent must be a neighbor with degree at least as large and minimal among such candidates. Every neighbor of the node except its parent must also be connected to the parent. Equal-degree parent-child choices indicate multiple reconstructions.

### Complexity Analysis
- **Time Complexity**: `O(V^2)` with adjacency-set checks
- **Space Complexity**: `O(V + E)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
