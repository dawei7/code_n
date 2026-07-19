## General
**Build undirected adjacency lists.** Add both directions for every edge so a breadth-first traversal can move through the tree. If `edges` is empty, return zero immediately.

**Find one diameter endpoint.** Run BFS from any vertex, such as `0`, and remember a farthest reached vertex `a`. In a tree, a vertex farthest from an arbitrary start is an endpoint of some diameter: if a longest path extended farther in the relevant direction, the unique paths would contradict `a`'s maximal distance.

**Measure from that endpoint.** Run BFS again from `a`. The greatest distance discovered is the distance to an opposite diameter endpoint and therefore equals the diameter. BFS distances count traversed edges, exactly matching the requested unit. Each traversal visits every vertex and edge once.

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
