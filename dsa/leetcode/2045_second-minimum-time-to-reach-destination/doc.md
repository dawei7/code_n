# Second Minimum Time to Reach Destination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2045 |
| Difficulty | Hard |
| Topics | Breadth-First Search, Graph Theory, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) |

## Problem Description

### Goal

A connected undirected graph represents a city with vertices numbered from `1`
through `n`. Every edge takes exactly `time` minutes to traverse. Each vertex
has a synchronized traffic signal: all signals start green, switch color every
`change` minutes, and alternate between green and red.

You may enter a vertex at any time but may leave only during a green interval.
If the signal is red, waiting until green is mandatory; if it is green, waiting
is forbidden. Vertices and edges may be revisited. Return the smallest travel
time from vertex `1` to vertex `n` that is strictly greater than the minimum
travel time, treating duplicate equal arrival times as one value.

### Function Contract

Let $E$ be the number of edges.

**Inputs**

- `n`: the number of vertices, with $2 \le n \le 10^4$.
- `edges`: between $n-1$ and $2\cdot10^4$ distinct undirected edges forming a
  connected graph without self-loops.
- `time`: the common positive edge traversal duration.
- `change`: the positive duration of each green or red signal phase.

Both timing values are at most $10^3$.

**Return value**

- The second distinct minimum time needed to travel from vertex `1` to vertex
  `n`.

### Examples

**Example 1**

- Input: `n = 5, edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time = 3, change = 5`
- Output: `13`
- Explanation: A two-edge route arrives in `6` minutes. A three-edge route
  reaches a red signal after `6` minutes, waits until `10`, and arrives at
  `13`.

**Example 2**

- Input: `n = 2, edges = [[1, 2]], time = 3, change = 2`
- Output: `11`
- Explanation: The second route is the walk `1 -> 2 -> 1 -> 2`.

**Example 3**

- Input: `n = 3, edges = [[1, 2], [2, 3], [1, 3]], time = 2, change = 3`
- Output: `4`
- Explanation: The direct edge is minimum; the two-edge route is the second
  distinct arrival.
