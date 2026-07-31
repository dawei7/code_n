# Maximize Sum of Weights after Edge Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3367 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/) |

## Problem Description

### Goal

An undirected weighted tree has $n$ nodes numbered from $0$ through $n-1$. Each row `[u, v, w]` in `edges` describes the unique edge between nodes `u` and `v` and its positive weight `w`. Because the input is a tree, the $n-1$ edges connect every node without a cycle.

Remove any number of edges so that every node is incident to at most `k` remaining edges. Among all edge subsets satisfying this degree limit, maximize the sum of the retained weights and return that maximum. Removing an edge separates its endpoints, but the remaining graph is not required to stay connected.

### Function Contract

**Inputs**

- `edges`: The $n-1$ weighted undirected edges, each encoded as `[u, v, w]`.
- `k`: The maximum allowed degree of every node after removals.

The constraints are $2\le n\le10^5$, $1\le k\le n-1$, $1\le w\le10^6$, and `edges` always forms a valid tree.

**Return value**

- The maximum total weight of a retained edge subset in which every node has degree at most `k`.

### Examples

**Example 1**

- Input: `edges = [[0,1,4],[0,2,2],[2,3,12],[2,4,6]]`, `k = 2`
- Output: `22`
- Explanation: Removing the weight-2 edge leaves weights 4, 12, and 6 while reducing node 2's degree to two.

**Example 2**

- Input: `edges = [[0,1,5],[1,2,10],[0,3,15],[3,4,20],[3,5,5],[0,6,10]]`, `k = 3`
- Output: `65`
- Explanation: Every original degree already respects the limit, so all edge weights remain.
