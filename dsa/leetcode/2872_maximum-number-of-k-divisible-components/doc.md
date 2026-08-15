# Maximum Number of K-Divisible Components

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2872 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of K-Divisible Components](https://leetcode.com/problems/maximum-number-of-k-divisible-components/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes labeled from $0$ through $n - 1$. Each pair `edges[i] = [a_i, b_i]` joins two nodes, and the 0-indexed array `values` assigns an integer value to every node.

You may remove any set of edges, including no edges. The remaining connected components form a valid split when the sum of the node values in every component is divisible by `k`.

Return the maximum number of components obtainable by a valid split. The total sum of `values` is guaranteed to be divisible by `k`, so at least the unsplit tree is valid.

### Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The $n - 1$ undirected edges; each entry contains two endpoint labels.
- `values`: The node values, where `values[i]` belongs to node `i`.
- `k`: The divisor required for every component sum.

The constraints are $1 \le n \le 3 \cdot 10^4$, $0 \le \texttt{values[i]} \le 10^9$, and $1 \le k \le 10^9$. The edges form a valid tree, and the sum of all node values is divisible by $k$.

**Return value**

- The maximum number of connected components whose individual node-value sums are all divisible by `k`.

### Examples

#### Example 1

- **Input:** `n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6`
- **Output:** `2`
- **Explanation:** Removing edge `[1,2]` produces component sums $12$ and $6$, both divisible by $6$.

#### Example 2

- **Input:** `n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3`
- **Output:** `3`
- **Explanation:** Cutting `[0,1]` and `[0,2]` produces component sums $3$, $6$, and $9$.
