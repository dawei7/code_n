# Network Delay Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 743 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/network-delay-time/) |

## Problem Description
### Goal
A directed network contains `n` nodes labeled `1` through `n`. Every entry `[u, v, w]` in `times` means a signal needs `w` time units to travel from source `u` to target `v`.

Send a signal from node `k` and return the minimum time by which all `n` nodes have received it, assuming the signal can follow directed paths and reaches each node by its fastest route. If even one node is unreachable from `k`, return `-1`.

### Function Contract
**Inputs**

- `times`: directed edges `[source, destination, travel_time]` with positive travel times
- `n`: the number of nodes labeled from `1` through `n`
- `k`: the node where the signal starts at time zero

**Return value**

- The earliest time by which all nodes have received the signal, equal to the largest shortest-path distance from `k`, or `-1` if any node cannot be reached

### Examples
**Example 1**

- Input: `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`
- Output: `2`

**Example 2**

- Input: `times = [], n = 2, k = 2`
- Output: `-1`

**Example 3**

- Input: `times = [[1,2,49],[2,1,8]], n = 2, k = 2`
- Output: `8`

### Required Complexity

- **Time:** $O((n+e) \log n)$
- **Space:** $O(n+e)$

<details>
<summary>Approach</summary>

#### General

**Reduce signal arrival to single-source shortest paths**

The signal may follow any directed route, and a node first receives it along the route with minimum total travel time. Build an adjacency list of outgoing `(neighbor, weight)` edges for each node. Once all shortest arrival times are known, the last node to receive the signal determines the answer.

**Process the next earliest arrival with a min-heap**

Initialize the source distance to zero and push it into a priority queue. Repeatedly pop the smallest proposed distance. If it is stale because a shorter route was already recorded, discard it. Otherwise relax every outgoing edge: when `distance + weight` improves the neighbor, record and push that candidate.

**Use positive weights to finalize progress safely**

All travel times are positive. Therefore a popped minimum candidate cannot later be improved through an unprocessed node with an equal or greater current distance. Stale entries can remain in the heap without affecting correctness, which avoids needing decrease-key support.

**Why the final maximum is the network delay**

Dijkstra relaxation records exactly the shortest travel time from `k` to every reachable node. Signals propagate simultaneously, so every node has received the signal precisely when the largest of those arrival times has elapsed. An infinite distance identifies a node with no directed route from `k`, making complete delivery impossible and requiring `-1`.

#### Complexity detail

Let `e = len(times)`. Building adjacency lists takes $O(n+e)$ space. Each successful relaxation can add a heap entry, and heap operations cost $O(\log n)$ up to the usual sparse-graph bound, giving $O((n+e) \log n)$ time and $O(n+e)$ space.

#### Alternatives and edge cases

- **Bellman-Ford relaxation:** scan every edge up to $n-1$ times; it handles negative weights but costs $O(ne)$ time and is unnecessary here.
- **Array-based Dijkstra:** repeatedly scan all unvisited nodes for the smallest distance in $O(n^2+e)$ time, which can be competitive only on dense graphs.
- **Plain breadth-first search:** it is correct only when every edge has the same weight.
- **One node and no edges:** the source already has the signal, so the delay is zero.
- **Unreachable node:** any infinite final distance forces `-1`.
- **Parallel edges:** relaxation naturally keeps the cheapest resulting route.
- **Directed edges:** an edge permits travel only from its source to its destination.
- **Cycles:** positive weights and distance checks prevent cycles from improving a shortest path indefinitely.

</details>
