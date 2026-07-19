## General
**Represent both directions explicitly**

Build an adjacency list with one entry from `u` to `v` and another from `v`
to `u` for every edge `[u, v]`. Begin breadth-first search at `source`, marking
it visited before placing it in the queue.

Repeatedly remove one queued vertex and inspect its neighbors. Enqueue only
neighbors that have not been visited before. Return `true` as soon as
`destination` is removed from the queue. If the queue empties first, return
`false`.

**Why the search answers reachability exactly**

Every vertex placed in the queue is connected to `source`: the source itself
has a zero-edge path, and each later vertex extends the established path to
its predecessor by one real graph edge. Thus reaching `destination` proves a
valid path.

Conversely, consider any path from `source`. Once the search visits one vertex
of that path, it examines the edge to the next vertex and visits that vertex
unless it was already discovered. Repeating this argument along the path
eventually discovers `destination`. Queue exhaustion therefore proves that no
such path exists.

## Complexity detail
The graph has $V$ vertices and $E$ edges. Building the adjacency lists stores
two entries per edge. Breadth-first search visits each reachable vertex once
and examines each incident adjacency entry once, for $O(V+E)$ time. The
adjacency lists, visited array, and queue use $O(V+E)$ space.

## Alternatives and edge cases
- **Depth-first search:** An iterative stack gives the same $O(V+E)$ bounds.
  Recursive DFS risks exceeding the language call-stack limit on a long path.
- **Union-find:** Union every edge and compare the final representatives of
  `source` and `destination`. This is effective when many connectivity queries
  share one graph, but a single BFS can stop after exploring only the source
  component.
- **Repeated edge scanning:** Expanding the reachable set by rescanning every
  edge can take $O(VE)$ time on an adversarially ordered chain.
- If `source == destination`, the zero-edge path is valid even when that vertex
  is isolated.
- An empty edge list connects no distinct pair of vertices.
- Because edges are undirected, either endpoint may lead to the other; storing
  only the input orientation would change the graph's semantics.
