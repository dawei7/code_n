## General

**Translate prerequisites into directed edges in the useful direction**

Treat each course as a vertex in a directed graph. A pair `[a, b]` says that
course `b` must be completed before course `a`, so the graph needs the edge
`b -> a`. The direction matters: once `b` has been taken, that edge tells the
algorithm which dependent course may have become available.

The exact solution stores these outgoing edges in `g`, a `defaultdict(list)`.
For every pair `[a, b]`, it appends `a` to `g[b]`. At the same time,
`indeg[a]` is incremented. The indegree of a course is the number of its
prerequisites that have not yet been removed from consideration. Initially no
course has been processed, so the constructed value is simply its total number
of prerequisite edges.

Reversing the edge would break both structures' meaning. If `[a, b]` were
stored as `a -> b`, processing `a` would appear to unlock `b`, even though the
contract requires `b` first. The chosen `b -> a` direction makes each later
indegree decrement correspond to satisfying one real prerequisite.

**The next legal course always has indegree zero**

A course can be placed next in the answer only when none of its prerequisites
remain unprocessed. In the graph, that condition is exactly indegree zero.
The solution initializes a `deque` named `q` with every course whose entry in
`indeg` is zero, including isolated courses that do not appear in any pair.

There can be several zero-indegree courses at once. Their relative order does
not matter because none currently depends on another through an unprocessed
incoming edge. The problem permits any valid ordering, so the deque's order is
acceptable. With the exact initialization, courses are inserted in increasing
numeric order, while newly unlocked courses are appended as they become
available; this determines one possible result but is not a requirement of the
problem.

The algorithm is Kahn's topological-sort algorithm. While the deque is not
empty, it removes one course `i` from the front and appends it to `ans`. At that
moment, `i` has no remaining prerequisite, so placing it after the courses
already in `ans` is legal. Processing `i` conceptually removes `i` and all of
its outgoing edges from the remaining graph.

For every dependent course `j` in `g[i]`, removing edge `i -> j` satisfies one
of `j`'s prerequisites, so the solution decrements `indeg[j]`. If the new value
is zero, every prerequisite of `j` has now been processed, and `j` is appended
to the deque. If the value remains positive, at least one required course is
still missing, so enqueuing `j` would be premature.

**Why a course is never emitted twice**

Each input pair is distinct, and every directed edge is processed once, when
its source is removed from the deque. A course enters the deque initially if
its indegree begins at zero. Otherwise, it enters exactly on the one decrement
that changes its indegree from one to zero. Later decrements cannot happen for
a valid count after it reaches zero because those would correspond to other
incoming edges that should already have kept the count above zero. Thus each
course is queued and appended to `ans` at most once.

The array `indeg` is deliberately mutated. It no longer represents original
prerequisite counts after processing starts; it represents counts in the
remaining, not-yet-emitted graph. That evolving meaning is what makes the
constant-time availability test possible.

**Trace through a graph with two valid middle orders**

For `numCourses = 4` and
`prerequisites = [[1,0],[2,0],[3,1],[3,2]]`, the edges are `0 -> 1`,
`0 -> 2`, `1 -> 3`, and `2 -> 3`. Initial indegrees are `[0, 1, 1, 2]`, so
only course 0 enters the deque.

Removing 0 first is legal. Its two outgoing edges are removed, decreasing the
indegrees of courses 1 and 2 to zero. Both enter the deque. If 1 is removed
next, processing edge `1 -> 3` lowers course 3's indegree from two to one, so 3
must still wait. Removing 2 then lowers it from one to zero, allowing 3 to
enter. The resulting answer is `[0, 1, 2, 3]`.

If adjacency or queue order causes 2 to be processed before 1, the answer can
instead be `[0, 2, 1, 3]`. Both are correct: 0 precedes both middle courses,
and both middle courses precede 3. A topological order need not be unique.

**Why the emitted list respects every prerequisite**

Whenever a course is appended to `ans`, its current indegree is zero. Every
original incoming edge must therefore already have been removed. An incoming
edge is removed only while processing its source course, and processing a
course includes appending it to `ans`. Hence every prerequisite of the newly
appended course already appears earlier in the answer. Repeating this argument
for each emitted vertex proves that every edge points forward in `ans`.

**Why answer length detects impossibility**

If all `numCourses` vertices are emitted, `ans` contains every course exactly
once and respects every prerequisite, so it is a valid requested ordering.

If the deque becomes empty while some courses remain, every remaining course
has positive indegree within the remaining graph. Starting from any remaining
course and repeatedly following an incoming edge must eventually revisit a
vertex because the graph is finite. That repetition forms a directed cycle.
Courses on the cycle can never become available: each waits for another course
on the same cycle. Any courses depending on that cycle are blocked as well.
Therefore no ordering containing every course exists.

The final expression returns `ans` only when `len(ans) == numCourses`;
otherwise it returns `[]`. It does not need a separate DFS cycle detector
because failure to process every vertex is already exact evidence that the
topological sort was obstructed.

The source expects `defaultdict`, `deque`, and `List` to be supplied or
imported by its execution environment; this file references them without local
imports.

## Complexity detail

Let $V$ be `numCourses` and $E$ be `len(prerequisites)`. Building `g` and
`indeg` visits every edge once, taking $O(E)$ time. Scanning `indeg` to
initialize the deque takes $O(V)$ time. Every course is enqueued and removed at
most once, and iterating all adjacency lists across the complete run visits
each edge exactly once. Total time is therefore $O(V+E)$.

The adjacency lists contain $E$ destinations. The indegree array, deque, and
answer can each contain $O(V)$ entries. Consequently auxiliary space is
$O(V+E)$. The output list itself accounts for $O(V)$ of that total; even if
output space is excluded by convention, the graph and bookkeeping still use
$O(V+E)$ in the worst case.

## Alternatives and edge cases

- **DFS with three colors:** Mark each course unvisited, active, or complete; an edge to an active course reveals a cycle, and courses appended after exploring descendants form a reverse postorder. It has the same $O(V+E)$ bounds but recursive Python implementations can reach depth $V$ and require careful reversal and cycle-state handling.
- **Stack instead of deque:** Kahn's algorithm remains correct if an available course is removed last-in-first-out. It merely selects a different valid topological ordering. The exact solution uses FIFO order with `popleft()`.
- **Repeatedly scan for an available course:** It avoids a queue but can rescan many blocked vertices after every removal, degrading toward $O(V^2+E)$. Maintaining the zero-indegree frontier makes each availability transition explicit.
- **No prerequisites:** Every course begins with indegree zero. The exact initialization queues courses `0` through `numCourses - 1`, and the returned list contains them all in that order.
- **One course:** With no self-edge allowed by the contract, course 0 begins available and the method returns `[0]`.
- **Several disconnected components:** Initial zero-indegree vertices from all components may be interleaved. This is valid because there are no prerequisite edges constraining the relative order of separate components.
- **A directed cycle:** No vertex in a closed cycle can reach indegree zero after outside prerequisites are removed. The final length check rejects the partial order and returns an empty list, as required.
- **A cycle plus independent courses:** Independent courses may appear in `ans` before the queue stalls. The method still returns `[]`, not that partial list, because the contract requires an ordering of every course.
- **Multiple prerequisites for one course:** Its indegree decreases once per prerequisite edge, and it is queued only after the last one is processed. This prevents a course from appearing after merely some of its requirements.
- **Distinct-pair guarantee:** The reference says prerequisite pairs are distinct. If duplicate edges were accepted without normalization, both the initial count and later decrements would be duplicated consistently, so this implementation would often still balance them, but relying on duplicates as separate requirements would be an unnecessary representation of invalid input.
- **Input preservation:** The algorithm mutates only its newly created graph, indegree array, deque, and answer. It reads but does not alter `prerequisites` or its pairs.
