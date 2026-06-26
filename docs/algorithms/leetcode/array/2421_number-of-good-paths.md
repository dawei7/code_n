# Number of Good Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2421 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Tree, Union-Find, Graph Theory, Sorting |
| Official Link | [number-of-good-paths](https://leetcode.com/problems/number-of-good-paths/) |

## Problem Description & Examples
### Goal
Given an undirected tree where each node has an associated value, identify the total number of "good paths." A path between two nodes is considered "good" if the starting node and the ending node share the same value, and every node along the simple path between them has a value less than or equal to that shared value.

### Function Contract
**Inputs**

- `vals`: A list of integers where `vals[i]` represents the value at node `i`.
- `edges`: A list of pairs `[u, v]` representing an undirected edge between nodes `u` and `v`.

**Return value**

- An integer representing the total count of good paths in the tree.

### Examples
**Example 1**

- Input: `vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]`
- Output: `6`

**Example 2**

- Input: `vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]`
- Output: `7`

**Example 3**

- Input: `vals = [1], edges = []`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Disjoint Set Union (DSU)** data structure combined with a **sorting-based processing strategy**. By sorting nodes by their values, we can incrementally build the graph. For each unique value, we unite nodes connected by edges whose endpoints have values less than or equal to the current value. Within each connected component, we track the frequency of the current value to calculate the number of valid pairs (good paths) that can be formed.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of nodes. This is dominated by sorting the nodes by their values. The DSU operations take nearly constant time, `O(N α(N))`, where `α` is the inverse Ackermann function.
- **Space Complexity**: `O(N)` to store the adjacency list, the DSU parent/size arrays, and the frequency maps for each component.
