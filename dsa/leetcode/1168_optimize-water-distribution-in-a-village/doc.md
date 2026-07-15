# Optimize Water Distribution in a Village

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1168 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) |

## Problem Description

### Goal

A village contains $n$ houses labeled from `1` through `n`, and every house must receive water. For house $i$, you may build a well directly inside it for cost `wells[i - 1]`. A house without its own well may instead receive water through pipes connected, possibly through other houses, to a house that has a well.

Each entry `pipes[j] = [house1, house2, cost]` offers a bidirectional pipe between two different houses for the stated cost. The same pair of houses may have several offers with different costs. Choose any combination of wells and offered pipes that supplies all houses, and return the minimum possible total cost.

### Function Contract

**Inputs**

- `n`: The number of houses, where $2 \le n \le 10^4$.
- `wells`: A length-$n$ array; `wells[i - 1]` is the cost, from `0` through $10^5$, of a well at house $i$.
- `pipes`: Between $1$ and $10^4$ entries `[house1, house2, cost]`, with distinct endpoints in `1..n` and cost from `0` through $10^5$.
- Let $p$ be the number of pipe offers and define $e=n+p$.

**Return value**

- The minimum total cost of wells and pipes that gives every house access to water.

### Examples

**Example 1**

- Input: `n = 3`, `wells = [1,2,2]`, `pipes = [[1,2,1],[2,3,1]]`
- Output: `3`

Build the cost-`1` well at house `1` and use both cost-`1` pipes.

**Example 2**

- Input: `n = 2`, `wells = [1,1]`, `pipes = [[1,2,1],[1,2,2]]`
- Output: `2`

### Required Complexity

- **Time:** $O(e \log e)$
- **Space:** $O(e)$

<details>
<summary>Approach</summary>

#### General

**Turn wells into graph edges.** Add a virtual water-source vertex `0`. For every house $i$, add an edge `(0, i)` weighted by `wells[i - 1]`; selecting it means building that well. Keep every offered pipe as its bidirectional edge between houses. Now every house receives water exactly when all vertices belong to the virtual source's connected component.

**Recognize a minimum spanning tree.** Any feasible selection is a connected subgraph on vertices `0..n`. If it contains a cycle, removing the most expensive edge on that cycle preserves connectivity and cannot increase cost. Therefore, an optimal selection can be a spanning tree, and its minimum cost is precisely the augmented graph's minimum spanning tree cost.

**Apply Kruskal's cut rule.** Sort all $e$ edges by cost and scan them from cheapest to most expensive. A disjoint-set structure tracks connected components. Accept an edge only when its endpoints currently have different roots, then union those roots and add its cost. The accepted edge is the cheapest edge crossing the cut between those components, so the cut property guarantees it belongs to some minimum spanning tree. Stop after accepting $n$ edges, which connects all $n+1$ vertices.

#### Complexity detail

Creating the virtual well edges takes $O(n)$ time. Sorting all $e=n+p$ edges costs $O(e \log e)$; path compression and union by size add near-linear disjoint-set work within that bound. The edge list and disjoint-set arrays use $O(e)$ space in total.

#### Alternatives and edge cases

- **Prim's algorithm:** Growing the augmented graph from node `0` with an adjacency list and heap also finds the MST in $O(e \log e)$ time.
- **Adjacency-matrix Prim:** Scanning all vertices for every addition is correct but takes $O(n^2)$ time, which is wasteful for sparse pipe sets.
- **Build the cheapest well only:** Pipes may form disconnected groups or be more expensive than additional wells, so one well need not suffice optimally.
- **Build every well:** This is always feasible but can ignore much cheaper pipes.
- **Parallel pipes:** Kruskal naturally considers the cheaper offer first and rejects later redundant edges if their endpoints are already connected.
- **Zero-cost choices:** Zero-cost wells and pipes are valid and should be processed before positive-cost edges.

</details>
