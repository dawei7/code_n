# Minimum Weighted Subgraph With the Required Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2203 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) |

## Problem Description

### Goal

A weighted directed graph has `n` nodes numbered from `0` through `n - 1`. Each entry `[from, to, weight]` is a directed edge with positive weight; parallel edges may occur. The three nodes `src1`, `src2`, and `dest` are pairwise distinct.

Choose a subgraph whose edges allow both source nodes to reach `dest`. Its weight is the sum of its distinct included edge weights, so a shared suffix used by both routes is paid for once. Return the minimum possible subgraph weight, or `-1` when no qualifying subgraph exists.

### Function Contract

**Inputs**

- `n`: the node count, where $3 \le n \le 10^5$.
- `edges`: up to $10^5$ directed triples `[from, to, weight]`, with positive weights at most $10^5$.
- `src1`, `src2`, `dest`: three distinct in-bounds node IDs.

Let $m$ be the number of edges.

**Return value**

Return the minimum total edge weight of a subgraph containing a path from each source to `dest`, or `-1` if either required route is impossible.

### Examples

#### Example 1

- **Input:** `n = 6`, `edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]`, `src1 = 0`, `src2 = 1`, `dest = 5`
- **Output:** `9`

The two routes can share edges after meeting, and an optimal qualifying subgraph has total weight `9`.

#### Example 2

- **Input:** `n = 3`, `edges = [[0,1,1],[2,1,1]]`, `src1 = 0`, `src2 = 1`, `dest = 2`
- **Output:** `-1`

There is no directed route from the second source to the destination.
