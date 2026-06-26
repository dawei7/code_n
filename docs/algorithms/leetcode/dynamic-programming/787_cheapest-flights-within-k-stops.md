# Cheapest Flights Within K Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_170` |
| Frontend ID | 787 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [cheapest-flights-within-k-stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

## Problem Description & Examples
### Goal
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

### Function Contract
**Inputs**

- `n`: int
- `flights`: List[List[int]]
- `src`: int
- `dst`: int
- `k`: int

**Return value**

int - cheapest price, or -1

### Examples
**Example 1**

- Input: `n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1`
- Output: `200`

**Example 2**

- Input: `n = 3, flights = [[0, 1, 2], [1, 2, 2], [0, 2, 5]], src = 0, dst = 2, k = 0`
- Output: `5`

**Example 3**

- Input: `n = 3, flights = [[0, 1, 2]], src = 0, dst = 2, k = 1`
- Output: `-1`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
