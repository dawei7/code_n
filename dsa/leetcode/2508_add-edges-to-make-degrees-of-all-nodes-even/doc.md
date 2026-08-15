# Add Edges to Make Degrees of All Nodes Even

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2508 |
| Difficulty | Hard |
| Topics | Hash Table, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/) |

## Problem Description

### Goal

An undirected graph has `n` nodes numbered from `1` through `n`. Each pair `edges[i] = [a_i, b_i]` represents an edge between two nodes, and the graph is allowed to be disconnected.

You may add no more than two edges. Every added edge must join two different nodes, and it must not duplicate an edge already present or another edge added during the operation.

Determine whether the additions can make every node's degree even. A node's degree is the number of edges incident to it.

### Function Contract

**Inputs**

- `n`: The number of graph nodes, labeled from `1` through `n`.
- `edges`: A list of distinct undirected edges, each represented by two different endpoint labels.

The constraints are $3 \le n \le 10^5$, $2 \le \lvert\texttt{edges}\rvert \le 10^5$, and every endpoint lies in $[1,n]$.

**Return value**

`True` if adding at most two valid edges can make every node's degree even; otherwise, `False`.

### Examples

#### Example 1

- **Input:** `n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]`
- **Output:** `true`
- **Explanation:** Nodes `1` and `3` are the only odd-degree nodes and are not already adjacent, so adding their edge makes every degree even.

#### Example 2

- **Input:** `n = 4, edges = [[1,2],[3,4]]`
- **Output:** `true`
- **Explanation:** All four nodes have odd degree. Two missing edges can pair them so that every node receives one additional incident edge.

#### Example 3

- **Input:** `n = 4, edges = [[1,2],[1,3],[1,4]]`
- **Output:** `false`
- **Explanation:** All four nodes have odd degree, but every pairing would require joining node `1` to a leaf that is already adjacent to it.
