## General
**Model prerequisites as reachability in a DAG**

Create an adjacency list with an edge from each prerequisite to the course that
depends on it. Then `u` is a prerequisite of `v` exactly when `v` is
reachable from `u`. Answering as many as $10^4$ queries by launching a new
search each time repeats the same reachability work, so compute the transitive
closure once.

Also record every node's indegree. Kahn's algorithm repeatedly removes a
zero-indegree course and lowers the indegrees of its outgoing neighbors. The
source guarantees no cycle, so this produces a topological order containing
all $C$ courses.

**Propagate descendants in reverse topological order**

For each course `u`, maintain `reachable[u]`, the set of courses known to
depend directly or indirectly on it. Process courses in reverse topological
order. Every outgoing neighbor `v` has already been processed, because
`u` appears before `v` in topological order.

For edge `u -> v`, add `v` itself and every member of `reachable[v]` to
`reachable[u]`. This records the direct dependency plus every path that can
continue beyond `v`. Multiple outgoing branches are combined by set union,
which automatically removes duplicate destinations reached along several
paths.

**Answer queries from the completed closure**

For query `[u, v]`, append whether `v in reachable[u]`. Membership is
constant expected time and preserves query order.

When `u` is processed, each possible first edge `u -> v` contributes
exactly `v` and all destinations reachable after that edge. Every nonempty
path from `u` starts with one such neighbor, so their union contains every
reachable course. Conversely, every inserted destination is supported by that
edge followed by either zero edges or a previously established path from
`v`. By reverse-topological induction, each set is therefore exact, making
every membership answer correct.

## Complexity detail
Building the graph and topological order takes $O(C+E)$. There are $E$ set
unions, each involving at most $C$ course labels, so closure construction is
$O(CE)$. The $Q$ membership queries take $O(Q)$ expected time. The adjacency
list uses $O(C+E)$ space and the reachability sets together use $O(C^2)$ in the
worst case.

## Alternatives and edge cases
- **Floyd-Warshall:** A boolean $C\times C$ matrix with triple-loop closure is
  simple and takes $O(C^3+Q)$ time and $O(C^2)$ space.
- **Search from every source:** DFS or BFS once per course also precomputes the
  closure in $O(C(C+E)+Q)$ time; it is competitive on sparse graphs.
- **Search for every query:** This uses only graph storage but can take
  $O(Q(C+E))$ time by repeating nearly identical traversals.
- **No prerequisites:** Every answer is `false`.
- **Direct edge:** A listed pair is immediately reachable and returns `true`.
- **Indirect chain:** Paths of any positive length count as prerequisite
  relationships.
- **Disconnected components:** A course cannot reach a course in another
  component.
- **Diamond paths:** A destination reached along multiple routes appears once
  in the set and still yields one boolean answer.
- **Query direction:** Reachability is directed; `u` preceding `v` says
  nothing about `v` preceding `u`.
- **No self queries:** The source guarantees distinct query endpoints, and
  reachability here represents paths of at least one edge.
