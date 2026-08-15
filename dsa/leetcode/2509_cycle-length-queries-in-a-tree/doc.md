# Cycle Length Queries in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2509 |
| Difficulty | Hard |
| Topics | Array, Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/cycle-length-queries-in-a-tree/) |

## Problem Description

### Goal

You are given the height parameter `n` for a complete binary tree containing $2^n-1$ nodes. The root is labeled `1`. Every node labeled `val` before the last level has left child `2 * val` and right child `2 * val + 1`.

Each pair `queries[i] = [a_i, b_i]` describes an independent operation. Temporarily add an edge between those two nodes, determine the length of the cycle this creates, and then remove the added edge before processing the next query. The temporary edge may be parallel to an existing tree edge.

A cycle starts and ends at the same node without reusing an edge, and its length is the number of edges it traverses. Return one cycle length for every query in the original order.

### Function Contract

**Inputs**

- `n`: The tree parameter, producing node labels from `1` through $2^n-1$.
- `queries`: A list of $m$ pairs `[a, b]` whose distinct endpoints identify the temporary edge.

The constraints are $2 \le n \le 30$, $1 \le m \le 10^5$, and $1 \le a,b \le 2^n-1$ with $a \ne b$.

**Return value**

A list of $m$ integers where each entry is the cycle length for the corresponding query.

### Examples

#### Example 1

- **Input:** `n = 3, queries = [[5,3],[4,7],[2,3]]`
- **Output:** `[4,5,3]`
- **Explanation:** The original paths contain `3`, `4`, and `2` edges respectively. The temporary edge closes each path, producing cycle lengths `4`, `5`, and `3`.

#### Example 2

- **Input:** `n = 2, queries = [[1,2]]`
- **Output:** `[2]`
- **Explanation:** Nodes `1` and `2` already share a tree edge. The added parallel edge forms a cycle using those two edges.
