## General
A feasible course order is a topological ordering of the prerequisite graph. For each pair `[course, prerequisite]`, direct an edge from the prerequisite to the course: completing the first unlocks the second. Increment the course's indegree for each required incoming edge.

Kahn's algorithm begins with every zero-indegree course, because it currently has no unmet prerequisite. Repeatedly remove one such course, count it as completed, and decrement the indegree of every dependent. A dependent whose indegree reaches zero has now had all prerequisites processed and joins the queue.

For `[[1,0],[2,0],[2,1]]`, only course `0` begins available. Completing it unlocks `1` but not yet `2`; completing `1` removes `2`'s final unmet prerequisite and unlocks it. For `[[1,0],[0,1]]`, no course begins with indegree zero, so processing cannot start.

The final processed count is the decisive test. A valid ordering need not be returned, but counting removed vertices tells whether the algorithm found one covering all courses.

At all times, a course's indegree equals its number of prerequisites not yet processed. Therefore every queued course is safe to take, and the removal sequence respects all edges. If all `V` courses are removed, that sequence proves feasibility. If fewer are removed, every remaining vertex has positive indegree within the remaining subgraph. Following incoming edges in this finite subgraph must eventually repeat a vertex, revealing a directed cycle. Courses on that cycle depend on one another indefinitely, so completing all courses is impossible.

## Complexity detail
Building adjacency lists and indegrees visits `V` vertices and `E` prerequisite pairs. Each vertex enters the queue at most once and each edge causes one decrement, so time is $O(V + E)$. The adjacency representation, indegrees, and queue use $O(V + E)$ space.

## Alternatives and edge cases
- Depth-first search with unvisited/visiting/finished colors detects a back edge with the same bounds, but recursion depth can be an implementation concern.
- Repeatedly rescanning all prerequisites to find available courses can become quadratic.
- Union-find detects undirected connectivity cycles, not the directed cycles relevant to prerequisite order.
- No prerequisites always succeeds. A self-loop fails immediately in principle, and a cycle in any disconnected component makes the complete schedule impossible.
