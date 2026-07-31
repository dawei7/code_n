# Minimum Time to Reach Destination in Directed Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3604 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/) |

## Problem Description
### Goal
A directed graph has `n` nodes labeled from `0` through `n - 1`. Each entry `edges[i] = [u, v, start, end]` describes an edge from `u` to `v` whose departure window includes every integer time $t$ satisfying $\texttt{start} \le t \le \texttt{end}$.

Begin at node `0` at time `0`. During one unit of time, either wait at the current node or depart along an outgoing edge whose window contains the current time; traversing that edge advances the clock by exactly one. Waiting may be used for any number of time units, including before the first edge.

Return the earliest time at which node `n - 1` can be reached. Return `-1` when no sequence of waits and valid edge departures reaches the destination.

### Function Contract
**Inputs**

- `n`: the number of nodes in the directed graph
- `edges`: directed time-window edges represented as `[source, destination, start, end]`

The graph has at most $10^5$ nodes and at most $10^5$ edges. Edge endpoints are distinct, and every interval satisfies $0 \le \texttt{start} \le \texttt{end} \le 10^9$.

**Return value**

The minimum arrival time at node `n - 1`, or `-1` if that node is unreachable under the edge windows.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0,1,0,1],[1,2,2,5]]`
- Output: `3`

Depart immediately for node `1`, arrive at time `1`, wait until time `2`, then traverse to the destination.

**Example 2**

- Input: `n = 4, edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]]`
- Output: `5`

Waiting until time `1` before taking `0 -> 2`, then waiting until time `4` for `2 -> 3`, reaches node `3` at time `5`.

**Example 3**

- Input: `n = 3, edges = [[1,0,1,3],[1,2,3,5]]`
- Output: `-1`

Node `0` has no outgoing edge, so the destination cannot be reached.
