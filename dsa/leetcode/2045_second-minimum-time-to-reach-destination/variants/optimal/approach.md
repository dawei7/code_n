## General
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

## Complexity detail
Each vertex stores at most two accepted hop counts, so each directed edge is
examined only a constant number of times. Graph construction and BFS take
$O(N+E)$ time. Simulating the resulting walk takes $O(N)$ time because the
second-shortest hop count in a connected undirected graph is at most the
shortest count plus two. Adjacency lists, two counts per vertex, and the queue
use $O(N+E)$ space.

## Alternatives and edge cases
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
