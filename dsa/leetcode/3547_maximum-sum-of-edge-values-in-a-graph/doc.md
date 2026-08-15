# Maximum Sum of Edge Values in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3547 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Greedy, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/) |

## Problem Description

### Goal

An undirected connected graph has `n` nodes numbered from `0` through `n - 1`. Every node has degree at most two, and each pair in `edges` identifies two distinct nodes joined by one edge. No edge occurs more than once.

Assign the distinct integers from $1$ through $n$ to the nodes, using every value exactly once. An edge contributes the product of the values placed at its endpoints, and the total score is the sum of those products over all edges.

Return the largest score obtainable by any valid assignment. Only the graph's adjacency structure determines which assigned values are multiplied together; the original node numbers do not contribute to the score.

### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: The undirected graph edges, with each edge represented as a two-element node pair.

Let $m = \lvert\texttt{edges}\rvert$. The constraints are $1 \le n \le 5 \cdot 10^4$, $1 \le m \le n$, the graph is connected, every endpoint lies in $[0,n-1]$, no edge is repeated or self-directed, and every node has degree at most two.

**Return value**

Return the maximum possible sum of edge-endpoint products after assigning the unique values $1,2,\ldots,n$ to the nodes.

### Examples

#### Example 1

- **Input:** `n = 4, edges = [[0,1],[1,2],[2,3]]`
- **Output:** `23`
- **Explanation:** Along the path, the assignment order `1, 3, 4, 2` produces $1\cdot3+3\cdot4+4\cdot2=23$.

#### Example 2

- **Input:** `n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]`
- **Output:** `82`
- **Explanation:** The edges form a cycle. A cyclic ordering such as `1, 2, 4, 6, 5, 3` yields a total score of $82$.

---
