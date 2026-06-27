# Count Pairs of Connectable Servers in a Weighted Tree Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3067 |
| Difficulty | Medium |
| Topics | Array, Tree, Depth-First Search |
| Official Link | [count-pairs-of-connectable-servers-in-a-weighted-tree-network](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) |

## Problem Description & Examples
### Goal
Given a weighted tree representing a network of servers, identify for every server `i` the number of pairs of other servers `(a, b)` such that the paths from `a` to `i` and `b` to `i` are both divisible by a given integer `signalSpeed`, and these paths only intersect at server `i`.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `signalSpeed`: An integer representing the divisor for path weights.

**Return value**

- A list of integers where the `i`-th element is the count of valid server pairs for server `i`.

### Examples
**Example 1**

- Input: `edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1`
- Output: `[0,4,6,6,4,0]`

**Example 2**

- Input: `edges = [[0,6,3],[6,5,3],[6,1,1],[1,2,2],[2,3,4],[2,4,4]], signalSpeed = 3`
- Output: `[2,0,0,0,0,0,2]`

---

## Underlying Base Algorithm(s)
The problem is solved using Depth-First Search (DFS) on an adjacency list representation of the tree. For each node, we treat it as a root and explore its subtrees. If a subtree contains `k` nodes whose distance from the root is divisible by `signalSpeed`, these nodes can be paired with nodes from other subtrees of the same root that also satisfy the condition. The total count for a root is the sum of products of counts from distinct subtrees.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the number of servers. For each of the `n` nodes, we perform a DFS traversal of the tree, which takes `O(n)`.
- **Space Complexity**: `O(n)` to store the adjacency list and the recursion stack.
