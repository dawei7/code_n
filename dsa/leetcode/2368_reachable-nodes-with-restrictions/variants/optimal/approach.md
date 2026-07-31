## General

**Remove forbidden vertices conceptually.** Put every restricted identifier in
a set. Build the undirected adjacency list, but never enter a node in that set.
The requested nodes are exactly the connected component of 0 in the remaining
graph.

Run an iterative depth-first traversal from 0. Mark nodes when pushing them,
count every visited node, and push each unvisited unrestricted neighbor.
Marking prevents following an undirected edge back to its parent.

Every visited node has an unrestricted path from 0 formed by traversal edges.
Conversely, traversal follows every unrestricted edge leaving the growing
component, so any node with such a path is eventually visited. The count is
therefore exactly the reachable maximum.

## Complexity detail

Building adjacency and traversing each node and edge at most once takes $O(n)$
time for a tree. The adjacency list, marks, restricted set, and stack use
$O(n)$ space.

## Alternatives and edge cases

- **Breadth-first search:** A queue visits the same unrestricted component with
  identical complexity.
- **Union find:** Union edges whose endpoints are unrestricted, then report
  node 0's component size; this also takes near-linear time.
- **Per-node reachability:** Searching from 0 separately for every candidate
  repeats work and can take $O(n^2)$ time.
- **Restricted parent:** Its descendants may be legal individually but remain
  unreachable when their unique path crosses it.
- **Root:** Node 0 is guaranteed unrestricted and always contributes one.
