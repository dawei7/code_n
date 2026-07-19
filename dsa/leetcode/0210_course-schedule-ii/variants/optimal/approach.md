## General
Build the prerequisite graph with edges from each prerequisite to the courses it unlocks. The indegree of a course is then exactly its number of unresolved prerequisites.

Initialize a queue with every zero-indegree course. Removing one from the queue represents taking it, so append it to the output. For each dependent, decrement the indegree; if that was its final unmet prerequisite, enqueue it.

The queue order need not be unique. If several courses are simultaneously available, any choice among them preserves validity, which is why multiple different output arrays can be correct.

For `num_courses = 4` and prerequisites `[[1,0],[2,0],[3,1],[3,2]]`, course `0` is first. Courses `1` and `2` then become available in either order, and course `3` becomes available only after both have been processed. Valid outputs include `[0,1,2,3]` and `[0,2,1,3]`.

After processing stops, compare the output length with `num_courses`. A partial list is not a valid partial answer: it proves some courses remain trapped behind a cycle, so the required return is an empty list.

Every emitted course has zero remaining indegree, so all its prerequisites were emitted earlier. Therefore, if all courses are emitted, the constructed sequence is a valid ordering. If fewer than `V` are emitted, every remaining vertex has an incoming edge from the remaining subgraph. Following such edges in a finite graph must repeat a vertex, yielding a directed cycle. No ordering can satisfy that cycle, so returning an empty list is necessary. These cases are exhaustive.

## Complexity detail
Constructing adjacency and indegrees takes $O(V + E)$. Each course is enqueued at most once and every edge is relaxed once, so the full algorithm remains $O(V + E)$ time. The graph, indegrees, queue, and result use $O(V + E)$ space.

## Alternatives and edge cases
- Depth-first postorder produces a reverse topological order, but needs three-state visitation to distinguish a back edge from a completed neighbor.
- Sorting course labels ignores dependency edges and is not generally valid.
- Trying permutations is factorial.
- With no prerequisites, any permutation containing all courses is valid.
- A self-loop or a cycle in one disconnected component forces an empty result; all acyclic disconnected components must appear in a successful ordering.
