# Maximum Star Sum of a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2497 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Graph Theory, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-star-sum-of-a-graph/) |

## Problem Description

### Goal

An undirected graph has `n` nodes numbered from `0` through `n - 1`. The integer `vals[i]` is the value assigned to node `i`, and each pair in `edges` connects two distinct nodes in both directions.

A star is a subgraph formed by choosing one center node and zero or more edges incident to that center. Its nodes are the center together with the selected neighbors, and its star sum is the sum of their values. The selected star may use at most `k` edges; it is not required to include every neighbor or to use exactly `k` edges.

Return the largest star sum obtainable anywhere in the graph. Choosing no incident edge is always legal, so an isolated node—or any node by itself—also forms a candidate star.

### Function Contract

**Inputs**

- `vals`: A list of `n` node values, where $1 \leq n \leq 10^5$ and every value lies from $-10^4$ through $10^4$.
- `edges`: A list of `m` undirected edges `[u, v]` between distinct node indices, where $0 \leq m \leq 10^5$.
- `k`: The maximum number of incident edges selected for one star, with $0 \leq k \leq n - 1$.

**Return value**

Return an integer equal to the maximum sum of a center value and the values of at most `k` of its neighbors.

### Examples

#### Example 1

- **Input:** `vals = [1, 2, 3, 4, 10, -10, -20]`, `edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]`, `k = 2`
- **Output:** `16`
- **Explanation:** Center `3` contributes `4`; choosing neighbors `1` and `4` contributes `2 + 10` more.

#### Example 2

- **Input:** `vals = [-5]`, `edges = []`, `k = 0`
- **Output:** `-5`
- **Explanation:** The only possible star consists of node `0` alone.

#### Example 3

- **Input:** `vals = [-8, 7, 6, -20]`, `edges = [[0, 1], [0, 2], [1, 3]]`, `k = 2`
- **Output:** `7`
- **Explanation:** Although center `0` can take two positive neighbors for sum `5`, node `1` alone is better because selecting a negative neighbor is optional.
