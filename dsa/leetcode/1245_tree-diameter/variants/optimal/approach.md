## General
**Build undirected adjacency lists.** Add both directions for every edge so a breadth-first traversal can move through the tree. If `edges` is empty, return zero immediately.

**Find one diameter endpoint.** Run BFS from any vertex, such as `0`. BFS removes vertices in non-decreasing distance order, so the last removed vertex `a` has maximum distance from the start. A standard tree property makes `a` an endpoint of a diameter: for any diameter path, one of its endpoints is at least as far from the start as every vertex outside that path; otherwise the unique connecting paths would extend one side of the supposed diameter. Any vertex tied at that maximum distance is likewise a valid endpoint of some diameter.

**Measure from that endpoint.** Run BFS again from `a`. Because `a` is a diameter endpoint, its greatest distance is the distance to an opposite endpoint: no shorter value could describe the longest path, and no larger value could exist without forming a longer path. BFS distances count traversed edges, exactly matching the requested unit.

## Complexity detail
Building adjacency lists takes $O(n)$ time and space because a tree has $n-1$ edges. Two BFS traversals each take $O(n)$ time and use an $O(n)$ distance array and queue, so the total bounds remain $O(n)$ time and $O(n)$ space.

## Alternatives and edge cases
- **BFS from every vertex:** It finds every eccentricity and is correct, but takes $O(n^2)$ time on a tree.
- **One postorder depth-first search:** Combining the two greatest child depths at each vertex also runs in $O(n)$ time, but recursive implementations can exceed the call stack on a long path.
- **Repeated leaf removal:** Peeling layers locates the tree center, from which the diameter can be derived, though two traversals are more direct.
- **Single vertex:** With no edges, the diameter is `0`.
- **Path tree:** The two leaves are diameter endpoints and the result is $n-1$.
- **Star tree:** Any two leaves form a diameter of `2` when at least two leaves exist.
- **Input order:** Undirected adjacency makes edge orientation and ordering irrelevant.
