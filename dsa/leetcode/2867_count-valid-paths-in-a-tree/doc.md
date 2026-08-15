# Count Valid Paths in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2867 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Tree, Depth-First Search, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Valid Paths in a Tree](https://leetcode.com/problems/count-valid-paths-in-a-tree/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes labeled with the integers from $1$ through $n$. The array `edges` contains its $n-1$ undirected edges, with each pair `[u, v]` joining the two named nodes.

For two distinct nodes `a` and `b`, consider the unique simple path between them. The path is valid when exactly one node label appearing anywhere on that path is a prime number. The endpoints are included when counting prime labels.

Paths are unordered: `(a, b)` and `(b, a)` describe the same path and must be counted only once. Return the total number of valid paths in the tree.

### Function Contract

**Inputs**

- `n`: The number of nodes, labeled from $1$ through $n$.
- `edges`: A list of $n-1$ pairs `[u, v]` representing the edges of a valid undirected tree.

The input satisfies $1 \le n \le 10^5$, every endpoint lies between $1$ and $n$, and every edge contains exactly two endpoints.

**Return value**

- The number of unordered paths between distinct nodes whose labels contain exactly one prime number.

### Examples

#### Example 1

- **Input:** `n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]`
- **Output:** `4`
- **Explanation:** The valid endpoint pairs are `(1,2)`, `(1,3)`, `(1,4)`, and `(2,4)`.

#### Example 2

- **Input:** `n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]`
- **Output:** `6`
- **Explanation:** The six valid pairs are `(1,2)`, `(1,3)`, `(1,4)`, `(1,6)`, `(2,4)`, and `(3,6)`.

#### Example 3

- **Input:** `n = 1, edges = []`
- **Output:** `0`
- **Explanation:** There are no paths between two distinct nodes.
