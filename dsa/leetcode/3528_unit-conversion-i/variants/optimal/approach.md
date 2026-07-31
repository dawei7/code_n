## General

Treat every triple as a directed weighted edge from `source` to `target`. The guarantee gives a rooted directed tree at unit `0`, so each unit has exactly one relevant path from the base. The desired value for a child is therefore its parent's value multiplied by the edge factor.

Build adjacency lists without assuming that parent edges appear before child edges in the input. Start unit `0` with value `1`, then traverse outward with an explicit stack. Whenever an edge reaches `target`, assign `result[target] = result[source] * factor` modulo $10^9+7$. Because the forward path is unique, this is the only possible conversion product for that target, and the traversal reaches every unit once.

## Complexity detail

The directed tree has $n$ vertices and $n-1$ edges. Building the adjacency lists and traversing every vertex and edge once takes $O(n)$ time. The graph, result array, and traversal stack require $O(n)$ space.

## Alternatives and edge cases

- **Process triples in input order:** A child's source value may not be known yet because conversion entries are not guaranteed to be topologically ordered.
- **Search separately for every unit:** Following a new path from unit `0` for each target is correct but can take $O(n^2)$ on a chain.
- **Recursive depth-first search:** It has the same asymptotic work, but a chain of up to $10^5$ units can exceed Python's recursion limit; an explicit stack is safer.
- **Modulo reduction:** Reduce after each multiplication so path products never need to be materialized at full size.
- **Base unit:** Exactly one unit of type `0` equals itself, so `result[0]` is always `1`.
