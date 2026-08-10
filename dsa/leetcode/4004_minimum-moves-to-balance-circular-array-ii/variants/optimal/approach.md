## General

**Total balance gives the feasibility test.**  A move transfers one unit from one person to a neighbor. It changes where a unit is located but does not change the sum of all balances.

If `sum(balance) < 0`, the circle has more total deficit than total supply. No sequence of transfers can make every entry non-negative, so the source returns `-1`.

If the total is non-negative, the positive entries contain at least enough units to fill every negative entry. Because the circle is connected, units can be moved along neighbor edges from any surplus position to any deficit position. Feasibility then follows.

The source also computes

`total_deficit = sum(-x for x in balance if x < 0)`.

This is exactly how many units must reach deficit positions. Extra positive balance may remain where it is; there is no requirement to make every final value zero. If `total_deficit == 0`, all entries are already non-negative and the answer is `0`.

**Model units as flow through the circle.**  The graph contains one node for every array position, plus a super-source and a super-sink.

- For every positive `balance[i]`, add a zero-cost edge from the source to `i` with capacity `balance[i]`. This is how many units that position can donate.
- For every negative `balance[i]`, add a zero-cost edge from `i` to the sink with capacity `-balance[i]`. Filling that capacity repairs the entire deficit.
- From every position `i`, add an unlimited-capacity edge to its right neighbor `(i + 1) % n` with cost `1`.
- Also add an unlimited-capacity edge from `i` to its left neighbor `(i - 1 + n) % n` with cost `1`.

Sending one unit across one circular edge costs one, exactly matching one allowed move. A flow path

`source -> surplus position -> ...neighbor edges... -> deficit position -> sink`

represents moving one unit from that surplus to that deficit. Its cost is the number of neighbor transfers along the route.

Sending `total_deficit` units of minimum-cost flow therefore gives the minimum number of moves. No flow is required for surplus units left over after all deficits are filled.

**Residual edges allow earlier choices to be corrected.**  The helper `add_edge` creates a forward edge with the requested capacity and cost and a reverse edge with initial capacity zero and negated cost. After flow is sent forward, the reverse edge gains capacity.

A later augmenting path may use such a reverse edge to cancel part of an earlier route and redirect it through a better combination. This is why the algorithm is not merely a greedy assignment of each deficit to its currently nearest surplus. Global competition for limited supply can require rerouting.

The fourth field of each edge stores the index of its reverse edge. During augmentation, the source subtracts `push_flow` from every forward residual capacity and adds it to the corresponding reverse capacity.

**Find one cheapest augmenting path at a time.**  The outer loop continues until `current_flow == total_deficit`. On each iteration, it finds a shortest residual path from the super-source to the super-sink.

The exact code uses a queue-based shortest-path procedure commonly called SPFA:

- `dist` begins at infinity except `dist[source] = 0`;
- `parent_node` and `parent_edge` remember how each improved node was reached;
- `in_queue` prevents duplicate queue entries while a node is already waiting;
- an edge is relaxed only when its residual `cap > 0`.

SPFA is relevant because reverse residual edges have negative costs. A plain unweighted BFS would not minimize cost, and Dijkstra without reduced-cost potentials would not be valid once negative reverse edges appear.

If the sink has no finite distance, no more flow can be sent and the loop stops. Under the non-negative-total feasibility condition, the connected ring and unlimited neighbor capacities should leave a path while any deficit remains.

**Push the largest safe amount along that path.**  The source begins `push_flow` with the remaining unmet deficit. It walks backward from sink to source through the parent arrays and takes the minimum residual capacity on the path. This is the largest amount that can be added without exceeding a supply edge, deficit edge, or residual rerouting edge.

After updating capacities, it adds:

- `push_flow` to `current_flow`;
- `push_flow * dist[sink]` to `total_cost`.

Capacities and balances are integers, so every augmentation sends an integer number of units. When all deficit capacity is filled, the recorded cost is the number of unit neighbor transfers.

**Why minimum-cost flow matches the original optimum in both directions.**  Take any legal sequence of moves that ends with all balances non-negative. Trace each donated unit from an original positive position through the neighbor edges it crosses until it fills a deficit. These traces form a feasible flow of `total_deficit` units, and the flow cost equals the move count.

Conversely, decompose any integral source-to-sink flow into unit paths. Execute each path as neighbor transfers from its surplus start to its deficit end. Source capacities prevent over-donation, sink capacities fill exactly the deficits, and each graph edge costs one per physical move. Thus a flow of cost `C` produces a legal sequence of `C` moves.

The standard successive-shortest-augmenting-path theorem says that repeatedly adding flow along a shortest residual source-to-sink path yields a minimum-cost flow of the requested value. Reverse edges are what let the residual shortest paths undo previously committed portions when needed.

For `balance = [4, -1, -2]`, node zero supplies four units. Nodes one and two demand one and two units. Each deficit node is one circular edge from node zero, so sending three required units costs `3`. One surplus unit remains unused.

**Important source and manifest mismatches.**  The exact file omits all of these required names:

- `List` for the method annotation;
- `inf` for capacities and distances;
- `deque` for the shortest-path queue.

Without an injected environment, class definition first raises `NameError` for `List`. Supplying `List` exposes the missing `inf`, and supplying that exposes the missing `deque`.

The manifest summary also says the solution uses “potentials and heap-based shortest augmenting paths.” The stored code uses neither potentials nor a heap. It uses `deque`, `in_queue`, and SPFA-style relaxation. That difference materially affects the defensible worst-case time bound.

## Complexity detail

Let `n` be the array length, and let

$$
F = \sum_{\texttt{balance}[i] < 0} -\texttt{balance}[i]
$$

be the total deficit.

The residual graph has `O(n)` vertices and `O(n)` edges, including reverse edges. One SPFA run has a worst-case bound of `O(VE) = O(n^2)`. Because capacities are integral, every successful augmentation pushes at least one unit, so there are at most `F` augmentations.

A safe worst-case bound for the exact stored implementation is therefore:

- Time complexity `O(Fn^2)`.
- Auxiliary space complexity `O(n)`.

This time bound is conservative; one augmentation often pushes many units, so practical iteration counts can be much smaller than `F`. Nevertheless, the manifest's `O(n^2 \log n)` claim would correspond to a different heap-and-potentials implementation and is not established by this queue-based source.

The graph, residual edges, distance arrays, parent arrays, queue flags, and queue all use linear space. Flow units are represented by capacities rather than individual objects, so space does not depend on `F`.

## Alternatives and edge cases

- **Greedily use the nearest surplus:** Local nearest choices can consume supply needed more efficiently elsewhere. Residual min-cost flow supports global reassignment.
- **Expand every unit into a graph node:** This makes the graph depend on balance magnitudes. Capacities represent many identical units compactly.
- **Dijkstra without potentials:** Negative reverse-edge costs appear after augmentation, so ordinary Dijkstra is not valid on the residual graph.
- **Heap Dijkstra with reduced-cost potentials:** This is a standard faster min-cost-flow implementation and resembles the manifest summary, but it is not the algorithm in the exact source.
- **Specialized circular transport mathematics:** The ring structure may permit a more specialized optimization, but the stored solution uses a general residual flow network.
- **Negative total balance:** Conservation makes success impossible, and the early `-1` return avoids graph construction.
- **No deficits:** Positive and zero entries already satisfy the goal, so the answer is zero even if total balance is large.
- **Extra total supply:** Only `total_deficit` units are sent. Unused positive balance does not need to move.
- **Zero balances:** They create neither source nor sink edges but may carry flow through their neighbor edges.
- **One-element array:** A negative value fails the total check; a non-negative value has zero deficit. Both outcomes occur before circular self-edges matter.
- **Two-element circle:** Left and right neighbors are the same person, so the source creates parallel cost-one edges. They do not change the minimum cost.
- **Large balance magnitudes:** Capacities aggregate units, but the safe SPFA iteration bound still depends on total deficit `F`.
- **Reverse residual edges:** Their negative costs do not represent negative physical moves. They represent canceling previously sent flow during optimization.
- **Disconnected-path check:** With sufficient total supply and the fully connected circle, a path should exist until every deficit is filled. The final conditional still returns `-1` if the requested flow was not achieved.
- **Missing dependencies:** Actual execution requires `List`, `inf`, and `deque` to be defined or imported.
- **Manifest complexity:** `O(n^2 \log n)` should not be attributed to this exact SPFA implementation; its worst-case analysis must include `F` and SPFA's `O(VE)` behavior.
