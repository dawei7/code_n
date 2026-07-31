## General

**Interpret favorites as a functional graph**

Draw one directed edge from every employee to their favorite. Each connected
component contains exactly one directed cycle, with directed trees feeding
into its cycle vertices. A valid circular seating has only two possible core
shapes.

A cycle of length at least three can be seated in its cycle order, but none of
its incoming chains can join: both neighboring seats of every cycle member are
already occupied by cycle members. Such a component contributes only its cycle
length, and cycles from different components cannot be joined without breaking
a required adjacency.

A two-cycle is different. If employees $a$ and $b$ favor each other, they need
only their shared adjacency. One incoming chain can extend outward from $a$,
and another can extend outward from $b$. Multiple extended two-cycles can then
be placed consecutively around the same table, so their contributions add.

**Prune trees and preserve their deepest chains**

Compute every vertex's indegree and place all indegree-zero vertices in a
queue. Let `depth[v]` be the longest chain ending at $v$, including $v$
itself. When pruning $u$, propagate `depth[u] + 1` to its favorite and then
decrease that favorite's indegree. This topological process removes every
non-cycle vertex. The maximum propagation into a cycle vertex is exactly the
one chain worth attaching there; two chains cannot both use the same outer
seat.

Vertices with positive indegree after pruning are precisely the cycle
vertices. Traverse each remaining cycle once. Record the largest cycle length.
For every two-cycle $(a,b)$, add `depth[a] + depth[b]`; these depths already
include the pair members and their best incoming chains. The answer is the
larger of the longest single cycle and the sum of all extended two-cycles.

Every construct counted this way has an explicit valid seating. Conversely,
following favorite edges from any valid attendee must reach its component's
cycle, and the two available neighbors impose exactly the long-cycle or
extended-two-cycle forms above. The comparison therefore covers every possible
optimal arrangement.

## Complexity detail

Let $n$ be the number of employees. Indegree construction, topological
pruning, and the final cycle traversals each process every vertex and edge a
constant number of times, for $O(n)$ time. The indegrees, chain depths, queue,
and cycle bookkeeping use $O(n)$ space.

## Alternatives and edge cases

- **Repeated traversal from every employee:** Following favorite links anew
  from every start can recover cycles and chain lengths, but takes $O(n^2)$
  time on long chains.
- **Recursive reverse-tree search:** DFS can compute incoming depths after
  cycles are identified, but recursion depth may reach $n$ and requires careful
  exclusion of the opposite member of a two-cycle.
- **Count only the largest cycle:** This misses the fact that every extended
  mutual-favorite pair can contribute to the same circular seating.
- A cycle of length at least three cannot accept an incoming chain because
  both adjacent seats of every cycle member are already committed.
- Only the longest incoming chain on each side of a two-cycle can be used.
- The minimum input is one mutual-favorite pair, whose answer is $2$.
