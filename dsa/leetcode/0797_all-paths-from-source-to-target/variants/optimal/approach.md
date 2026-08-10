## General

**Treat each queue entry as one unfinished path**

The task asks for paths, not merely reachable vertices. Two different routes that arrive at the same vertex must remain separate because each may produce a different final answer.

The queue therefore stores complete path lists. It begins with `[0]`, the one path containing only the source. For a queued path, its last element is the current vertex:

`u = path[-1]`.

Every earlier list element records the exact route used to reach `u`.

**Expand a path by one directed edge**

If `u` is not the target, the algorithm visits every outgoing neighbor `v` in `graph[u]`. The extended path is:

`path + [v]`.

Python list concatenation creates a new list. That copy is essential: all queue entries must own independent path histories. Mutating and reusing one list would let later extensions corrupt paths already waiting in the queue.

Each appended entry represents exactly one additional directed edge from its previous last vertex to `v`, so every queued list is always a valid source-originating path.

**Recognize completed paths**

The target vertex is `n - 1`. When the dequeued path ends there, the method appends that list to `ans` and executes `continue`.

There is no need to explore outgoing edges from the target. The requested path ends on its first arrival at that vertex. Even if an input representation listed target neighbors, extending beyond the target would no longer be a source-to-target path of the requested form.

The target-ending list can be stored directly because that queue entry will never be mutated. Every extension elsewhere is created through concatenation.

**Why no visited set is used**

A normal reachability traversal often marks each vertex visited once. That would be incorrect here.

Suppose paths `0 -> 1 -> 3` and `0 -> 2 -> 3` both reach vertex three. Marking three visited after the first path would discard every answer beginning with the second prefix. The identity of a path includes its whole prefix, not only its endpoint.

The queue may therefore contain many paths ending at the same vertex. They represent different valid choices and must all be expanded.

**Why the DAG guarantee prevents infinite expansion**

The graph is directed and acyclic. A path can never return to a vertex already on that path, because doing so would form a directed cycle.

Consequently every queued path contains at most `n` vertices. Expansion must eventually reach the target or a vertex with no outgoing neighbors. The queue therefore empties after finitely many path prefixes without needing cycle detection.

If cycles were allowed, omitting a path-local visited check could generate endlessly longer walks. The exact algorithm relies on the stated DAG contract.

**Breadth-first order does not affect correctness**

Using a deque and `popleft` explores shorter path prefixes before longer ones. The problem permits answers in any order, so breadth-first ordering is not required for output semantics.

Depth-first backtracking would enumerate the same set in a different order and often use less frontier memory. The exact solution's breadth-first organization is nevertheless correct because it systematically expands every pending valid prefix once.

**Trace the first example**

For `graph = [[1,2],[3],[3],[]]`:

1. The queue starts with `[0]`.
2. Expanding zero creates `[0,1]` and `[0,2]`.
3. Expanding `[0,1]` creates `[0,1,3]`.
4. Expanding `[0,2]` creates `[0,2,3]`.
5. Each remaining path ends at target three and is appended to `ans`.

The result contains exactly the two expected paths.

**Dead ends are discarded naturally**

If a path ends at a non-target vertex whose adjacency list is empty, the neighbor loop performs no append. That path leaves the queue and contributes no answer.

No explicit “dead end” condition is necessary. Only target-ending prefixes enter `ans`.

**Every reported list is a valid path**

The initial list starts at source zero. An extension adds only a vertex named in the adjacency list of the current endpoint, so every consecutive pair is a real directed edge.

A list is reported only when its endpoint equals `n - 1`. Therefore every result is a valid directed path from source to target.

**Every valid source-to-target path is reported**

Consider any valid path `0 = p0, p1, ..., pm = n - 1`. The queue initially contains prefix `[p0]`.

Whenever it contains prefix `[p0,...,pi]`, expansion examines every neighbor of `pi`, including the next path vertex `p(i+1)`. It therefore enqueues the next prefix. Induction shows that the complete path is eventually queued and then appended.

Unique adjacency entries prevent the same next edge from being generated twice from one prefix. In a DAG, a complete vertex sequence has a unique chain of prefix expansions, so the algorithm reports each valid path once.

**Output size determines the unavoidable work**

A DAG can contain exponentially many source-to-target paths. Since the method must return every path explicitly, no algorithm can have running time or result storage bounded only by `V + E` in the worst case.

The queue makes this output-sensitive behavior visible: a separate list exists for every live prefix that may become an answer.

## Complexity detail

Let $V$ be the number of vertices, $P$ the number of returned paths, and $R$ the number of source-originating path prefixes actually dequeued, including prefixes that end at dead ends. Let $L$ be the sum of the lengths of all generated prefixes.

Copying `path + [v]` costs proportional to the new path length. Scanning adjacency lists also happens once per path prefix ending at that vertex, not merely once per vertex. A precise source-level bound is $O(L+\text{all repeated neighbor scans})$, which is safely $O(R(V+E))$ but usually much tighter.

When every explored prefix can be extended to some returned path, the customary output-sensitive description is $O(V+E+P\cdot V)$ time and $O(V+E+P\cdot V)$ including output, matching the manifest. In a DAG with exponentially many source-to-dead-end prefixes but few target paths, `P` alone does not describe the exact work; `R` or `L` is the honest parameter.

The returned lists occupy $\Theta(P\cdot V)$ in the worst case. The breadth-first queue can simultaneously hold many partial paths and may also require $O(L)$ path-list storage in the worst frontier. The graph itself is input, not newly allocated by the method.

## Alternatives and edge cases

- **Depth-first backtracking:** Maintain one mutable path, copy it only at the target, and undo each choice. It has the same unavoidable output cost but usually smaller frontier memory.

- **Memoized paths from each vertex:** Reuse suffix paths in the DAG, but constructing prefixed copies still incurs output-sized work and may store many intermediate lists.

- **Vertex-level visited set:** Incorrect because different prefixes reaching the same vertex represent different answers.

- **Single direct edge:** The queue extends `[0]` once and reports `[0,n-1]`.

- **No route to the target:** All prefixes end at dead ends, the queue empties, and the answer is empty.

- **Shared downstream subgraph:** Every distinct upstream prefix must traverse it separately in this queue-of-paths implementation.

- **Target reached:** Record the path and do not extend it further.

- **DAG guarantee:** It supplies termination without cycle checks.

- **Answer order:** Breadth-first order is acceptable because any order is allowed.
