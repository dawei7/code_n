# Number of Good Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2421 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) |

## Problem Description

### Goal

An undirected tree contains $n$ nodes numbered from $0$ through $n-1$ and exactly $n-1$ edges. The 0-indexed array `vals` assigns `vals[i]` to node $i$, while every pair `[a, b]` in `edges` connects those two distinct nodes.

A simple path is good when its two endpoints have the same value and every node between them has a value less than or equal to that endpoint value. Count all distinct good paths. A path and the same path traversed in reverse count only once, and every single node is itself a valid good path.

### Function Contract

**Inputs**

- `vals`: A list of $n$ integers where `vals[i]` is the value of node $i$.
- `edges`: A list of $n-1$ pairs `[a, b]` describing the undirected edges of the tree.

The constraints are $1 \le n \le 3 \cdot 10^4$, $0 \le \texttt{vals[i]} \le 10^5$, and $0 \le a,b < n$ with $a \ne b$. The edges form one connected acyclic graph.

**Return value**

- The number of distinct good paths.

### Examples

**Example 1**

- Input: `vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]`
- Output: `6`

The five singleton paths are good. The two value-3 nodes also connect through nodes whose values do not exceed 3, producing one additional path.

**Example 2**

- Input: `vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]`
- Output: `7`

Besides the five singleton paths, the adjacent value-1 nodes form one good path and the adjacent value-2 nodes form another.

**Example 3**

- Input: `vals = [1], edges = []`
- Output: `1`

The only node contributes its singleton path.
