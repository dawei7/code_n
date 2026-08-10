## General

**Separate route length from traffic-signal timing**

Every edge takes the same `time` minutes, and every traffic signal changes in synchronization. Starting from time zero, the elapsed time after a given number of traversed edges is therefore the same for every route of that length.

At each intermediate arrival, whether the signal is red depends only on the global elapsed time, not on the vertex or path. Consequently:

- first find the second-smallest distinct number of edges in a walk from vertex one to vertex `n`;
- then simulate that many edge traversals to obtain the second-minimum elapsed time.

This is why the graph search can ignore clock time entirely.

**Store two distinct step counts per vertex**

`dist[v][0]` and `dist[v][1]` are used to retain the two smallest distinct positive walk lengths discovered for vertex `v`. The queue stores pairs `(vertex, step_count)`.

For a popped state `(u,d)`, every neighbor `v` is reachable in `d+1` steps. If that value is smaller than `dist[v][0]`, it becomes the first stored length and is enqueued. Otherwise, it is accepted as the second length only when

`dist[v][0] < d + 1 < dist[v][1]`.

Both inequalities are strict. An equal-length route does not count as a second minimum because the definition asks for the smallest value strictly larger than the minimum.

**The unusual source initialization**

The source places `(1,0)` in the queue but assigns `dist[1][1] = 0` rather than the conventional `dist[1][0] = 0`.

This means a later two-edge return to vertex one can enter `dist[1][0]` even though zero sits in the other slot. The two entries for the source are not kept in sorted order. Nevertheless, the queued zero state starts the breadth-first expansion correctly, and allowing a positive revisit to the source is necessary because valid second-minimum walks may pass through vertex one again.

For all ordinarily discovered vertices, the two acceptance tests retain increasing distinct positive lengths. The target's second slot is populated with the required second walk length.

**Why breadth-first queue order finds the two smallest lengths**

Every transition adds exactly one edge, so states enter the queue in nondecreasing step count. The first accepted length for a vertex is its smallest discovered positive walk length. The next strictly larger accepted value is its second distinct one.

A vertex is enqueued at most twice under these rules, aside from the explicitly seeded source state. Cycles are permitted and are important, but storing only two lengths prevents infinite exploration.

When a second distance to target `n` is discovered, the code does not enqueue that target state. It breaks out of the current neighbor loop because no expansion from the completed target is needed to compute its arrival. The already stored value remains available after the queue finishes.

**Convert the second edge count into minutes**

Let `L = dist[n][1]`. The source performs `L` iterations. In each iteration it first adds `time`, representing one completed edge traversal.

If this was the final edge, the journey has reached the destination and no departure is needed, so no signal wait is applied.

Otherwise, the traveler is at an intermediate vertex and must leave for the next edge. The signal phase is found with

`(ans // change) % 2`.

Phase zero is green, phase one is red, phase two is green again, and so on.

**Wait to the next green boundary only when red**

If the phase is red, the source sets

`ans = (ans + change) // change * change`.

Suppose the current red phase began at `q * change`. This expression advances time to `(q+1) * change`, the beginning of the next green phase.

If arrival occurs exactly when a red phase begins, the quotient is odd and the traveler waits the full `change` minutes. If the light is green, the source does not wait, correctly following the rule that voluntary waiting during green is forbidden.

**Trace the first example's second route length**

The shortest walk from one to five uses two edges. A distinct three-edge walk is `1 -> 3 -> 4 -> 5`, so `L=3`.

Starting at zero, the first traversal ends at time three and the signal is green. The second ends at time six, which lies in the red interval from five to ten, so the traveler waits until ten. The final edge ends at thirteen. No wait is added at the destination, giving the required result.

**Why second step count gives second time**

The timing function for a walk length is strictly increasing: adding another edge requires a positive traversal time and may also add a nonnegative wait. All walks with the same edge count have equal time because signals are synchronized.

Thus the smallest time comes from the smallest walk length, duplicate routes of that length do not create a distinct time, and the next distinct time comes from the second distinct walk length. The two-stage method exactly matches the problem's second-minimum definition.

## Complexity detail

Let $N$ be vertices and $E$ edges. Building the undirected adjacency sets takes expected $O(E)$ time and $O(N+E)$ space.

Each vertex length state is accepted at most twice and each accepted state scans its adjacency set, so graph search takes $O(N+E)$ time up to a constant factor. The second walk length is $O(N)$ for this connected unweighted setting, so the final timing simulation is $O(N)$. Total time is $O(N+E)$ and total space is $O(N+E)$.

## Alternatives and edge cases

- **Time-aware Dijkstra:** Store the two smallest arrival times directly; correct but more machinery than step-count BFS under synchronized equal edges.
- **Enumerate simple paths:** Incorrectly excludes useful revisits and is computationally infeasible.
- **Duplicate shortest routes:** They share one minimum time and do not count as the second distinct value.
- **Return through vertex one:** Explicitly permitted; the source's revisit handling supports it.
- **Single edge graph:** The second walk goes to the destination, back, and to it again.
- **Arrival during green:** Departure is immediate; voluntary waiting is not allowed.
- **Arrival during red:** Wait exactly until the next multiple of `change` that begins a green phase.
- **Arrival at destination during red:** No wait matters because the journey is complete.
- **Exact phase boundary:** A boundary into red requires waiting; a boundary into green permits immediate departure.
- **Cycles:** Needed to create a second walk when only one simple route exists.
- **Strict second distance:** Equal edge counts are rejected by the strict inequalities.
- **Synchronized signals:** This is what makes elapsed time a function only of edge count.
- **Input preservation:** The source builds separate adjacency sets.
