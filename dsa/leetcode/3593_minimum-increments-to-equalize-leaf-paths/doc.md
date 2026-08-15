# Minimum Increments to Equalize Leaf Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3593 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/) |

## Problem Description

### Goal

An undirected tree with `n` nodes is rooted at node `0`. Every node `i` has a positive traversal cost `cost[i]`, and the score of a root-to-leaf path is the sum of every node cost on that path, including both endpoints.

You may select any nodes and increase each selected cost by an arbitrary non-negative amount. Make all root-to-leaf path scores equal while selecting as few distinct nodes as possible. Return that minimum number of nodes; the magnitudes of their increases do not contribute to the answer.

### Function Contract

**Inputs**

- `n`: The number of nodes, with $2 \leq n \leq 10^5$.
- `edges`: The $n-1$ undirected edges of a valid tree. Each entry `[u, v]` has $0 \leq u,v < n$.
- `cost`: The node costs, where `cost.length == n` and $1 \leq \texttt{cost[i]} \leq 10^9$.

**Return value**

Return the minimum number of distinct nodes whose costs must be increased so that every path from root `0` to a leaf has the same score.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0, 1], [0, 2]], cost = [2, 1, 3]`
- **Output:** `1`
- **Explanation:** The two path scores are $3$ and $5$. Increasing node `1` by $2$ equalizes them.

#### Example 2

- **Input:** `n = 3, edges = [[0, 1], [1, 2]], cost = [5, 1, 4]`
- **Output:** `0`
- **Explanation:** A rooted chain has only one root-to-leaf path, so equality already holds.

#### Example 3

- **Input:** `n = 5, edges = [[0, 4], [0, 1], [1, 2], [1, 3]], cost = [3, 4, 1, 1, 7]`
- **Output:** `1`
- **Explanation:** Increasing node `1` by $2$ raises both paths through it from score $8$ to score $10$, matching the path through node `4`.
