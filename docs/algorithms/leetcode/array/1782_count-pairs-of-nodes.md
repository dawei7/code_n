# Count Pairs Of Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1782 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Graph Theory, Sorting, Counting |
| Official Link | [count-pairs-of-nodes](https://leetcode.com/problems/count-pairs-of-nodes/) |

## Problem Description & Examples
### Goal
For each query value, count unordered node pairs whose combined degrees are greater than the query. Multiple edges between the same pair count toward degrees, but pair counting may need correction for those shared edges.

### Function Contract
**Inputs**

- `n`: number of nodes labeled `1..n`.
- `edges`: undirected edges, possibly with duplicates.
- `queries`: degree-sum thresholds.

**Return value**

Return one count per query.

### Examples
**Example 1**

- Input: `n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]`
- Output: `[6,5]`

**Example 2**

- Input: `n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]`
- Output: `[10,10,9,8,6]`

**Example 3**

- Input: `n = 3, edges = [[1,2],[2,3]], queries = [1,2,3]`
- Output: `[3,2,0]`

---

## Underlying Base Algorithm(s)
Compute every node degree and sort the degree list. For each query, use two pointers to count pairs with degree sum above the threshold. Then correct overcounted pairs connected by duplicate edges: if `degree[u] + degree[v] > query` but `degree[u] + degree[v] - shared_edges(u, v) <= query`, subtract that pair once.

---

## Complexity Analysis
- **Time Complexity**: `O((n + e) + q * (n + p))`, where `p` is the number of distinct connected pairs
- **Space Complexity**: `O(n + p)`
