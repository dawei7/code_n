## General

Between two different houses on a circle, a route that does not repeat edges is either the forward arc or the backward arc. All road lengths are positive, so adding a complete extra loop can only increase travel time. The minimum cost of one requested move is therefore the smaller of those two directed arc lengths, and choices for different queries are independent once the current house is known.

Build `forward_prefix`, where the difference between two prefix entries gives a non-wrapping sum of forward edges. The clockwise distance from `current` to `target` is `(forward_prefix[target] - forward_prefix[current]) % forward_total`: a negative difference is corrected by adding the full-circle length. Build an analogous prefix sum over `backward`. Because a backward edge is indexed by its source, the counterclockwise distance is `(backward_prefix[current + 1] - backward_prefix[target + 1]) % backward_total`.

For each target, add the smaller directed distance and make that target the new current house. Each prefix expression exactly sums one of the only two simple arcs, and positivity rules out any route containing additional cycles, so every chosen minimum is optimal. Summing these independently optimal legs minimizes the complete ordered visit.

## Complexity detail

Let $Q$ be the number of queries. Constructing the two prefix arrays takes $O(n)$ time, and each requested move takes $O(1)$ time, for $O(n+Q)$ total time. The prefix arrays use $O(n)$ space.

## Alternatives and edge cases

- **Walk both arcs for every query:** Direct summation is correct but can require $O(nQ)$ time when targets repeatedly cross half the circle.
- **Use only one road array:** Forward and backward lengths are independent; reversing a forward edge does not give the corresponding backward cost.
- **Dijkstra's algorithm per target:** The graph has only two simple candidate arcs between houses, so general shortest-path search repeats unnecessary work.
- **Wraparound:** A target with a smaller label may be close in the forward direction through the edge from `n - 1` to `0`.
- **Two houses:** Both directions connect the same pair but can have different costs, so the minimum still must be taken.
- **Large totals:** The answer can exceed 32-bit range when both the road and query counts are large.
