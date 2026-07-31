## General

Run a breadth-first search from any node and choose a farthest node `A`; in a tree, `A` is an endpoint of some diameter. A second search from `A` finds a farthest node `B`, so the distance $D$ from `A` to `B` is the diameter length.

For every node `v`, its greatest distance to any node equals `max(dist(A, v), dist(B, v))`. This standard tree-diameter property follows because every branch away from the chosen diameter can be extended farthest toward one of its two ends. Therefore, `v` is peripheral—and hence an endpoint of some diameter—exactly when that maximum equals $D$.

Run one final search from `B`. Mark node `v` with `'1'` when either endpoint is distance $D$ away; otherwise mark it with `'0'`. This criterion includes endpoints from every tied diameter, rather than only `A` and `B`.

## Complexity detail

Let $N$ be the number of nodes. Building the adjacency lists and performing three breadth-first searches take $O(N)$ time because a tree has $N-1$ edges. The graph, queues, and distance arrays use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **All-pairs distances:** Search from every node and retain endpoints of maximum-distance pairs. This is direct but takes $O(N^2)$ time.
- **Tree dynamic programming:** Downward heights plus rerooted upward heights can compute every eccentricity in linear time, but two diameter endpoints give a simpler characterization.
- **Two nodes:** Both ends of the only edge are special.
- **Several diameters:** Testing eccentricity against $D$ includes every tied endpoint, not only the two endpoints selected during the searches.
- **Leaf is not sufficient:** A leaf on a shorter branch may fail to be an endpoint of any diameter.
- **Node numbering:** Traversal and distance, not numeric order, determine the output bits.
