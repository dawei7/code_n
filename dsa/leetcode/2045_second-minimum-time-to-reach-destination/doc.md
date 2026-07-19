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

### Required Complexity

- **Time:** $O(N+E)$
- **Space:** $O(N+E)$

<details>
<summary>Approach</summary>

#### General

**Reduce arrival order to hop-count order**

All edges have the same duration, all signals are synchronized, and waiting is
not optional during green phases. Therefore every walk containing the same
number of edges encounters the same sequence of departure times, regardless of
which vertices it visits. Adding another edge always increases arrival time.
The second distinct travel time consequently comes from the second distinct
smallest hop count from `1` to `n`.

**Keep the two smallest distinct hop counts per vertex**

Run breadth-first search over states `(vertex, steps)`. For each vertex, retain
its smallest and second-smallest distinct step counts. A new count replaces
the first when smaller, or replaces the second only when it lies strictly
between the stored values. Enqueue a state only when it improves one of those
two positions.

Every prefix of either of the two shortest distinct walks to a vertex must
itself be among the two relevant counts for its endpoint; a third-or-later
prefix cannot produce a shorter final walk when every extension adds one.
Thus keeping two counts is sufficient, and BFS discovers the second count for
the destination without confusing equal-length routes with a new value.

**Simulate the signal schedule for the second hop count**

Starting at elapsed time `0`, process exactly the destination's second hop
count. Before each departure, the signal is red precisely when
`(elapsed // change) % 2 == 1`. In that case, advance to the next multiple of
`change`; otherwise depart immediately. Then add `time` for the edge.

The hop search supplies the correct second distinct length, and the simulation
applies the only legal departure time at every vertex. Their combination
therefore returns the second distinct minimum arrival time.

#### Complexity detail

Each vertex stores at most two accepted hop counts, so each directed edge is
examined only a constant number of times. Graph construction and BFS take
$O(N+E)$ time. Simulating the resulting walk takes $O(N)$ time because the
second-shortest hop count in a connected undirected graph is at most the
shortest count plus two. Adjacency lists, two counts per vertex, and the queue
use $O(N+E)$ space.

#### Alternatives and edge cases

- **Time-aware Dijkstra:** Store two distinct arrival times per vertex in a
  priority queue. This is correct but adds a logarithmic factor even though
  synchronized equal-duration edges allow ordinary BFS by hops.
- **Exact-length reachability:** Recompute all vertices reachable after each
  hop until the destination appears twice. This is correct but can rescan much
  of the graph for $O(N(N+E))$ work.
- Equal-hop routes produce the same time and do not constitute first and second
  distinct values.
- On a single-edge graph, revisiting both endpoints supplies the required
  second route.
- Arrival exactly when a phase changes observes the new color.
- Waiting during green is forbidden, so a traveler cannot manufacture an
  arbitrary second arrival on the shortest route.
- Reaching the destination ends the trip; its signal is irrelevant unless the
  walk leaves and later revisits it.

</details>
