## General

If the array sum is negative, conservation of balance makes the goal impossible. Otherwise, regard every positive entry as supply and every negative entry as demand. Only the total deficit must be transported; any unused supply may remain where it started.

Build a residual flow network with one node per person, a source, and a sink. Connect the source to each surplus position with its available balance as capacity and zero cost. Connect each deficit position to the sink with its required amount as capacity and zero cost. For every neighboring pair on the circle, add both directed edges with unit cost and enough capacity to carry the entire deficit. Sending one unit across one such edge represents exactly one permitted move.

An integral source-to-sink flow that covers every deficit specifies how balance units travel from surplus positions to deficit positions; its edge cost is exactly the number of neighbor-to-neighbor moves. Conversely, any successful transfer sequence can be decomposed into these source-to-sink unit paths after cycles and unused surplus are discarded. Minimum-cost flow therefore has precisely the same optimum as the original problem.

Repeatedly find the cheapest augmenting path in the residual network. Reverse residual edges have negative costs after earlier augmentations, so maintain feasible node potentials and run Dijkstra on reduced nonnegative edge costs. Update the potentials by the new shortest distances, push the largest possible amount along the selected path, and add its original edge cost to the answer. Standard residual cancellation lets later paths revise earlier routing choices, so the final flow is globally minimum-cost rather than a greedy nearest-pair assignment.

## Complexity detail

The residual network has $O(n)$ vertices and edges. A heap-based Dijkstra pass costs $O(n\log n)$. Every nonfinal augmentation exhausts at least one source-supply edge or one deficit-sink edge, and those terminal edges cannot be reopened by a later source-to-sink path. Thus there are $O(n)$ augmentations, for $O(n^2\log n)$ total time. The graph, potentials, distances, parent links, and heap use $O(n)$ space.

## Alternatives and edge cases

- **Full Bellman-Ford per augmentation:** It handles negative residual edges without potentials but can take $O(n^3)$ time on this sparse network.
- **Greedy nearest surplus:** Pairing each deficit with the currently closest supply can block a better global assignment and does not account for residual rerouting.
- **Linear prefix balancing:** The familiar prefix-sum formula assumes a fixed cut or exact final values; here the circle has no fixed cut and extra surplus may remain at any positions.
- **Negative total:** No redistribution can change the array sum, so a negative total must return `-1` immediately.
- **No deficits:** Every entry is already non-negative, and the required flow and answer are both zero.
- **Circular edge:** Indices `0` and `n - 1` must receive the same unit-cost adjacency as every consecutive pair.
- **Large magnitudes:** Flow is augmented by capacity rather than one unit at a time, so values up to $10^5$ do not multiply the iteration count.
