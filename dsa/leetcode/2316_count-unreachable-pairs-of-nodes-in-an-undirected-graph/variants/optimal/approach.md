## General

**Reduce reachability to component sizes**

Build an undirected adjacency list, then start a graph traversal from every
node not previously visited. The traversal marks one entire connected
component and counts its nodes. Isolated nodes naturally produce components of
size one.

**Count each cross-component pair once**

Maintain the number of nodes not yet assigned to a completed component. After
discovering a component of size `size`, subtract it from `remaining`; the
product `size * remaining` counts pairs between this component and every
component that will be discovered later. Adding these products avoids both an
explicit list of sizes and double counting.

A graph traversal groups exactly the mutually reachable nodes. Thus a pair is
unreachable exactly when its endpoints occur in different discovered
components. When the earlier component is processed, its product counts that
pair once; later processing cannot count it again because the earlier nodes
are no longer in `remaining`.

## Complexity detail

Let $e$ be the number of edges. Constructing and traversing the adjacency list
touches every node and each undirected edge a constant number of times, for
$O(n+e)$ time. The adjacency list, visited flags, and traversal stack require
$O(n+e)$ auxiliary space.

## Alternatives and edge cases

- **Disjoint-set union:** Unioning edge endpoints and aggregating root sizes gives $O((n+e)\alpha(n))$ time and $O(n)$ space.
- **Breadth-first search:** A queue discovers the same components with the same asymptotic bounds.
- **Traversal from every node:** Recomputing reachability independently takes $O(n(n+e))$ time.
- **One node:** No pair of distinct nodes exists, so the result is zero.
- **No edges:** Every node is isolated and all $\binom{n}{2}$ pairs are unreachable.
- **Connected graph:** A single component leaves `remaining` equal to zero and contributes no pairs.
- **Large result:** The count can exceed 32-bit signed range, so the native return type is wide.
