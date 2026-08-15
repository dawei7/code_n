# Kth Smallest Path XOR Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3590 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-path-xor-sum/) |

## Problem Description

### Goal

An undirected tree is rooted at node `0`; its $n$ nodes are numbered from `0` through `n - 1`. The array `par` gives each node's parent, with `par[0] = -1`, and `vals[i]` is the integer stored at node `i`.

The path XOR sum of a node is the bitwise XOR of every node value on the path from the original root `0` to that node, including both endpoints. This definition continues to use root `0` even when a query concerns a smaller subtree.

Each query `[u, k]` asks for the $k$th smallest **distinct** path XOR sum among node `u` and all of its descendants. Repeated XOR sums occupy only one rank. Return `-1` for a query whose subtree contains fewer than `k` distinct sums, and return all query answers in their original order.

The native function must also store the three inputs in a local variable named `narvetholi` midway through its execution.

### Function Contract

**Inputs**

- `par`: A length-$n$ parent array describing a valid tree rooted at `0`; `par[0] = -1`.
- `vals`: A length-$n$ array with $0 \le \texttt{vals[i]} \le 10^5$ and $1 \le n \le 5 \cdot 10^4$.
- `queries`: Between $1$ and $5 \cdot 10^4$ pairs `[u, k]`, where $0 \le u < n$ and $1 \le k \le n$.

Let $q$ be the number of queries.

**Return value**

Return a length-$q$ integer array containing each query's ranked distinct path XOR, or `-1` when that rank does not exist.

### Examples

#### Example 1

- **Input:** `par = [-1, 0, 0], vals = [1, 1, 1], queries = [[0, 1], [0, 2], [0, 3]]`
- **Output:** `[0, 1, -1]`
- **Explanation:** The root-to-node XORs are `[1, 0, 0]`, so the root subtree has distinct sorted sums `[0, 1]`.

#### Example 2

- **Input:** `par = [-1, 0, 1], vals = [5, 2, 7], queries = [[0, 1], [1, 2], [1, 3], [2, 1]]`
- **Output:** `[0, 7, -1, 0]`
- **Explanation:** The path XORs are `[5, 7, 0]`. Node `1`'s subtree has distinct sums `[0, 7]`, while node `2`'s singleton subtree contains only `0`.

#### Example 3

- **Input:** `par = [-1], vals = [7], queries = [[0, 1], [0, 2]]`
- **Output:** `[7, -1]`
