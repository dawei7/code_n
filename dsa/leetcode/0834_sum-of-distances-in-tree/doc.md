# Sum of Distances in Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 834 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Tree, Depth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-distances-in-tree/) |

## Problem Description
### Goal
An undirected connected tree contains `n` nodes labeled from `0` through `n - 1` and exactly `n - 1` edges. Each pair `edges[i] = [a_i, b_i]` connects the two indicated nodes. Because the graph is a tree, exactly one simple path joins every pair of nodes, and its edge count is their distance.

Return an array `answer` of length `n`. For every node $i$, `answer[i]` must equal the sum of the distances from $i$ to all other nodes in the tree. The input is guaranteed to describe a valid tree.

### Function Contract
**Inputs**

- `n`: the number of nodes, with $1 \leq n \leq 3 \cdot 10^4$.
- `edges`: exactly `n - 1` pairs of distinct node labels; every label lies in $[0,n-1]$.

**Return value**

Return an integer array of length `n` whose entry at index $i$ is

$$
\texttt{answer}[i] = \sum_{j=0}^{n-1} \operatorname{dist}(i,j),
$$

where $\operatorname{dist}(i,j)$ is the number of edges on the unique path between nodes $i$ and $j$.

### Examples
**Example 1**

- Input: `n = 6, edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]`
- Output: `[8, 12, 6, 10, 10, 10]`

For node `0`, the five nonzero distances are $1,1,2,2,2$, whose sum is $8$.

**Example 2**

- Input: `n = 1, edges = []`
- Output: `[0]`

**Example 3**

- Input: `n = 2, edges = [[1, 0]]`
- Output: `[1, 1]`
