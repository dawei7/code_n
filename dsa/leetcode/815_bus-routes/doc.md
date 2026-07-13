# Bus Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 815 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bus-routes/) |

## Problem Description

### Goal

You are given several bus routes. Route `i` repeatedly cycles through every stop in `routes[i]`, so after boarding that bus at any one of its stops, a passenger may ride to any other stop listed on the same route. A transfer is possible wherever two routes share a stop.

The trip begins at `source` while the passenger is not on a bus and ends upon reaching `target`. Determine the fewest buses that must be boarded; the number of intermediate stops traveled does not affect this cost. If the endpoints are identical, no bus is needed. If the route network cannot connect distinct endpoints, return `-1`.

### Function Contract

**Inputs**

- `routes`: a list in which `routes[i]` contains the distinct stops served by bus route `i`.
- `source`: the stop where the trip begins.
- `target`: the destination stop.

**Return value**

- The minimum number of buses that must be boarded, or `-1` when the destination is unreachable.

### Examples

**Example 1**

- Input: `routes = [[1,2,7],[3,6,7]], source = 1, target = 6`
- Output: `2`
- Explanation: Take the first route to stop `7`, then transfer to the second route.

**Example 2**

- Input: `routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12`
- Output: `-1`
- Explanation: The routes containing `15` and those containing `12` lie in disconnected groups.

**Example 3**

- Input: `routes = [[5,8,11]], source = 8, target = 8`
- Output: `0`
- Explanation: No bus is needed when the trip already starts at its destination.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Model transfers without constructing every route pair**

Let `S` be the total number of stop occurrences across all routes. Build a reverse index from each stop to the route indices serving it. This incidence map reveals every bus that can be boarded at a stop without comparing that bus against all other routes or explicitly constructing a dense route graph.

**Make one breadth-first layer equal one boarded bus**

Start a breadth-first search with the `source` stop at distance zero. For one BFS layer, inspect every route serving the stops in the current queue. Boarding any such route uses one additional bus, and every stop on that route becomes reachable at that same bus count. If one of those stops is `target`, that layer number is the answer.

Mark a route when it is first boarded and never expand it again. Also enqueue each stop only once. Consequently, each reverse-index entry and each stop occurrence in a route is processed a constant number of times.

Breadth-first search explores states in nondecreasing bus count. Before layer `b`, the queue contains exactly stops reachable with $b - 1$ buses; expanding every newly available route produces all stops reachable with `b` buses. Therefore, the first discovery of `target` uses the minimum possible number of buses. If the queue empties first, no transfer sequence connects the two stops.

**Handle the zero-bus trip before searching**

When `source = target`, return `0` even if no listed route contains that stop. The BFS otherwise counts the first boarded route as one bus.

#### Complexity detail

Building the stop-to-routes index takes $O(S)$ time and space. Each route is expanded once and each of its stop occurrences is scanned once, so the BFS also takes $O(S)$ time. The reverse index, visited sets, and queue together use $O(S)$ space.

#### Alternatives and edge cases

- **BFS over route nodes:** Initialize all routes containing `source` and transfer between routes sharing a stop. It is equally efficient when adjacency is generated through the stop index, but precomputing all pairwise route intersections can take quadratic time.
- **Bidirectional search:** Searching from routes containing both endpoints can reduce practical work on large sparse networks, at the cost of more state and bookkeeping.
- **Pairwise intersection scans:** Testing every unvisited route against each dequeued route is correct but takes $O(R^2 L)$ in a chain-like network of `R` routes with typical route length `L`.
- **Identical endpoints:** Return `0` without boarding a route.
- **Endpoint absent from the network:** If the endpoints differ and either belongs to no route, the search returns `-1`.
- **Cycles and repeated transfer opportunities:** Visited-route and visited-stop sets prevent repeated expansion.
- **Several possible journeys:** BFS returns the route sequence using the fewest boarded buses, not the one visiting the fewest stops.

</details>
